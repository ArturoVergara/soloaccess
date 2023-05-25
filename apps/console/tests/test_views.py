# Django Imports
from django.urls import reverse_lazy

# 3rd Party Libraries
import pytest

# Soloaccess Libraries
from apps.console.models import Access, AccessUser

home_url = reverse_lazy("console:home")
access_list_url = reverse_lazy("console:access_list")
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


class TestAccessListView:
    def test_home_view_redirects_to_access_list_view(self, client, custom_user):
        client.force_login(custom_user)
        response = client.get(home_url)

        assert response.status_code == 302
        assert response["Location"] == access_list_url

    def test_get_method_without_data(self, client, custom_user):
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

    def test_get_method_display_right_data(
        self, client, custom_user, http_access, ssh_access
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


class TestAccessCreateView:
    url = reverse_lazy("console:access_create")

    def test_get_method_renders_right_form(self, client, custom_user):
        client.force_login(custom_user)
        response = client.get(self.url)
        response_content = str(response.content)

        assert response.status_code == 200
        assert response.template_name[0] == "console/access_form.html"
        assert 'name="name"' in response_content
        assert 'name="type"' in response_content
        assert 'name="observation"' in response_content
        assert 'name="image"' in response_content
        assert 'name="is_disable"' in response_content

    def test_post_method_with_right_data_creates_an_access(self, client, custom_user):
        data = {
            "name": "Example Access",
            "type": Access.Types.HTTP,
            "observation": "Example Observation",
        }
        client.force_login(custom_user)
        response = client.post(self.url, data=data, follow=True)
        created_access = Access.objects.first()

        assert response.status_code == 200
        assert Access.objects.count() == 1
        assert created_access.name == "Example Access"
        assert created_access.type == Access.Types.HTTP
        assert created_access.observation == "Example Observation"


class TestAccessDeleteView:
    def test_get_method_is_disable(self, client, custom_user, http_access):
        client.force_login(custom_user)
        response = client.get(
            reverse_lazy("console:access_delete", args=(http_access.id,))
        )

        assert response.status_code == 404
        assert response.context["exception"] == "Only POST method available"

    def test_post_method_delete_data_model(
        self, client, custom_user, http_access, ssh_access
    ):
        client.force_login(custom_user)

        assert Access.objects.count() == 2

        response = client.post(
            reverse_lazy("console:access_delete", args=(http_access.id,)), follow=True
        )

        assert response.status_code == 200
        assert response.redirect_chain[0][1] == 302
        assert response.redirect_chain[0][0] == access_list_url

        assert Access.objects.count() == 1
        assert Access.objects.filter(id=http_access.id).count() == 0
        assert Access.objects.filter(id=ssh_access.id).count() == 1


class TestAccessUpdateView:
    def test_get_method_renders_right_form(self, client, custom_user, http_access):
        client.force_login(custom_user)
        response = client.get(
            reverse_lazy("console:access_update", args=(http_access.id,))
        )
        response_content = str(response.content)

        assert response.status_code == 200
        assert response.template_name[0] == "console/access_form.html"
        assert 'name="name"' in response_content
        assert 'name="type"' in response_content
        assert 'name="observation"' in response_content
        assert 'name="image"' in response_content
        assert 'name="is_disable"' in response_content

        assert http_access.name in response_content
        assert http_access.get_type_display() in response_content
        assert http_access.observation in response_content

    def test_post_method_with_right_data_updates_an_access(
        self, client, custom_user, http_access
    ):
        data = {
            "name": "New Access Name",
            "type": http_access.type,
            "observation": http_access.observation,
        }
        client.force_login(custom_user)
        response = client.post(
            reverse_lazy("console:access_update", args=(http_access.id,)),
            data=data,
            follow=True,
        )
        updated_access = Access.objects.first()

        assert response.status_code == 200
        assert updated_access.name == "New Access Name"


class TestUserListView:
    url = reverse_lazy("console:user_list")

    def test_get_method_display_right_data(self, client, custom_user):
        client.force_login(custom_user)
        response = client.get(self.url)
        response_content = str(response.content)

        assert response.status_code == 200
        assert response.template_name[0] == "console/accessuser_list.html"
        assert "<th>#</th>" in response_content
        assert "<th>Email</th>" in response_content
        assert "<th>Active</th>" in response_content
        assert "<th>Staff</th>" in response_content
        assert '<th class="text-right">Actions</th>' in response_content

        assert custom_user.email in response_content
