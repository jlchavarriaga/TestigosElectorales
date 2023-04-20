from tests.api.base_test import BaseTest

ENDPOINT = '/api/v1/products'


class TestProducts(BaseTest):
    test_name = 'Test products endpoints.'

    def test_get_items(self):
        response = self.client.get(
            f'{ENDPOINT}',
            headers={'Authorization': f'Bearer {self.token}'}
        )

        assert response.status_code == 200
        assert response.json()
        assert len(response.json()) == 2

    def test_create_items(self):
        data = [
            {
                'name': 'Javascript book',
                'description': 'Javascript cookbook',
                'price': 15
            }
        ]
        response = self.client.post(
            f'{ENDPOINT}',
            headers={'Authorization': f'Bearer {self.token}'},
            json=data
        )

        assert response.status_code == 200
        assert response.json() == data

    def test_delete_item(self):
        response = self.client.delete(
            f'{ENDPOINT}/1',
            headers={'Authorization': f'Bearer {self.token}'}
        )
        assert response.status_code == 200
