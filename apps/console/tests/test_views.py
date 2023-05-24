# Django Imports
from django.urls import reverse_lazy

# 3rd Party Libraries
import pytest

# Soloaccess Libraries
from apps.console.models import Access, AccessUser

home_url = reverse_lazy("console:home")
access_list_url = reverse_lazy("console:access_list")
user_list_url = reverse_lazy("console:user_list")
pytestmark = pytest.mark.django_db


@pytest.fixture
def custom_user():
    user = AccessUser.objects.create_user(email="test@localhost", password="test123")
    user.is_active = True
    user.save()

    return user


@pytest.fixture
def http_access():
    return Access.objects.create(
        name="HTTP Access", type=Access.Types.HTTP, observation="This a HTTP example"
    )


@pytest.fixture
def ssh_access():
    return Access.objects.create(
        name="SSH Access", type=Access.Types.SSH, observation="This is a SSH Example"
    )


def test_home_view_redirects_to_access_list_view(client, custom_user):
    client.force_login(custom_user)
    response = client.get(home_url)

    assert response.status_code == 302
    assert response["Location"] == access_list_url


def test_access_list_view_without_data(client, custom_user):
    client.force_login(custom_user)
    response = client.get(access_list_url)
    response_content = str(response.content)

    assert response.status_code == 200
    assert response.template_name[0] == "console/access_list.html"
    assert "<th>#</th>" in response_content
    assert "<th>Name</th>" in response_content
    assert "<th>Type</th>" in response_content
    assert "<th>Observation</th>" in response_content
    assert "<th>Active</th>" in response_content
    assert '<th class="text-right">Actions</th>' in response_content


def test_access_list_view_display_right_data(
    client, custom_user, http_access, ssh_access
):
    client.force_login(custom_user)
    response = client.get(access_list_url)
    response_content = str(response.content)
    accesses = [http_access, ssh_access]

    assert response.status_code == 200
    assert response.template_name[0] == "console/access_list.html"

    for access in accesses:
        assert access.name in response_content
        assert access.get_type_display() in response_content
        assert access.observation in response_content


def test_user_list_view_display_right_data(client, custom_user):
    client.force_login(custom_user)
    response = client.get(user_list_url)
    response_content = str(response.content)

    assert response.status_code == 200
    assert response.template_name[0] == "console/accessuser_list.html"
    assert "<th>#</th>" in response_content
    assert "<th>Email</th>" in response_content
    assert "<th>Active</th>" in response_content
    assert "<th>Staff</th>" in response_content
    assert '<th class="text-right">Actions</th>' in response_content

    assert custom_user.email in response_content
