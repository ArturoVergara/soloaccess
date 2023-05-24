# Django Imports
from django.urls import reverse_lazy

# 3rd Party Libraries
import pytest

# Soloaccess Libraries
from apps.console.models import AccessUser

user_list_url = reverse_lazy("console:user_list")
pytestmark = pytest.mark.django_db


@pytest.fixture
def custom_user():
    user = AccessUser.objects.create_user(email="test@localhost", password="test123")
    user.is_active = True
    user.save()

    return user


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
