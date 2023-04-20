from tests.api.base_test import BaseTest

ENDPOINT = '/api/v1/orders'


class TestOrders(BaseTest):
    test_name = 'Test orders endpoints.'

    def test_get_items(self):
        response = self.client.get(
            f'{ENDPOINT}',
            headers={'Authorization': f'Bearer {self.token}'}
        )
        assert response.status_code == 200
        assert not response.json()

    def test_create_item(self):
        data = {
            'name': 'Books order',
            'description': 'Order of coding books',
            'products': [{'id': 3}, {'id': 4}]
        }
        response = self.client.post(
            f'{ENDPOINT}',
            headers={'Authorization': f'Bearer {self.token}'},
            json=data
        )
        assert response.status_code == 200
        assert len(response.json()['products']) == 2

    def test_delete_item(self):
        response = self.client.delete(
            f'{ENDPOINT}/1',
            headers={'Authorization': f'Bearer {self.token}'}
        )
        assert response.status_code == 200
