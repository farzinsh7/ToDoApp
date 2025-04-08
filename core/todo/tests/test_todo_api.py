from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from django.urls import reverse
import pytest


User = get_user_model()


@pytest.fixture
def api_client():
    """
    Fixture to provide a reusable API client for testing.
    """
    return APIClient()


@pytest.fixture
def authenticated_client(api_client):
    """
    Fixture to provide an authenticated API client.
    """
    user = User.objects.create_user(
        email="testuser@domain.com", password="test@1password"
    )
    api_client.force_authenticate(user=user)
    return api_client


@pytest.mark.django_db
class TestToDoAPI:
    def test_get_todo_response_200_status(self, authenticated_client):
        url = reverse("todo:api-v1:todo-list")
        response = authenticated_client.get(url)
        assert response.status_code == 200

    def test_post_todo_response_401_status(self, api_client):
        url = reverse("todo:api-v1:todo-list")
        data = {
            "title": "Test ToDo",
        }
        response = api_client.post(url, data=data)
        assert response.status_code == 401

    def test_create_todo_response_201_status(self, authenticated_client):
        url = reverse("todo:api-v1:todo-list")
        data = {
            "title": "Test ToDo",
        }
        response = authenticated_client.post(url, data=data)
        assert response.status_code == 201

    def test_create_post_invalid_data_response_400_status(self, authenticated_client):
        url = reverse("todo:api-v1:todo-list")
        data = {
            "title": "",
        }
        response = authenticated_client.post(url, data=data)
        assert response.status_code == 400

    def test_update_todo_response_200_status(self, authenticated_client):
        url = reverse("todo:api-v1:todo-list")
        data = {
            "title": "Test ToDo",
        }
        response = authenticated_client.post(url, data=data)
        todo_id = response.data["id"]

        update_url = reverse("todo:api-v1:todo-detail", args=[todo_id])
        update_data = {
            "title": "Updated ToDo",
        }
        response = authenticated_client.put(update_url, data=update_data)
        assert response.status_code == 200

    def test_update_todo_invalid_data_response_400_status(self, authenticated_client):
        url = reverse("todo:api-v1:todo-list")
        data = {
            "title": "Test ToDo",
        }
        response = authenticated_client.post(url, data=data)
        todo_id = response.data["id"]

        update_url = reverse("todo:api-v1:todo-detail", args=[todo_id])
        update_data = {
            "title": "",
        }
        response = authenticated_client.put(update_url, data=update_data)
        assert response.status_code == 400
