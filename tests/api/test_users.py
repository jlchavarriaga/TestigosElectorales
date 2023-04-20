from tests.api.base_test import BaseTest
from urllib.parse import quote

ENDPOINT = '/api/v1/users'


class TestUsers(BaseTest):
    test_name = 'Test users endpoints.'

    def test_get_items(self):
        response = self.client.get(
            f'{ENDPOINT}',
            headers={'Authorization': f'Bearer {self.token}'}
        )

        assert response.status_code == 200
        assert response.json()
        assert len(response.json()) == 2

    def test_create_item(self):
        data = {
            'username': 'test',
            'email': 'test@mailinator.com',
            'password': 'foo',
            'is_admin': False,
            'is_active': True
        }
        response = self.client.post(
            f'{ENDPOINT}',
            headers={'Authorization': f'Bearer {self.token}'},
            json=data
        )

        assert response.status_code == 200
        assert response.json() == data

    def test_delete_item(self):
        response = self.client.delete(
            quote(f'{ENDPOINT}/user1@mail.com'),
            headers={'Authorization': f'Bearer {self.token}'}
        )

        assert response.status_code == 200

    def test_update_item(self):
        data = {
            'username': 'test',
            'email': 'foo@mailinator.com',
            'password': 'new_pass',
            'is_admin': False,
            'is_active': True
        }
        response = self.client.put(
            quote(f'{ENDPOINT}/test@mailinator.com'),
            headers={'Authorization': f'Bearer {self.token}'},
            json=data
        )

        assert response.status_code == 200
        assert response.json() == data
