import json

from tests.base import BaseCase
from api.database.model import Category


class TestCategoriesPostApi(BaseCase):

    def test_successful_post_category(self):
        login_token = self.getLoginToken()

        category_payload = {
            "name": "category1"
        }

        response = self.app.post('/api/categories',
                                 headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
                                 data=json.dumps(category_payload))
        category_id = response.json['id']

        self.assertEqual(200, response.status_code)

        category = Category.objects(id=category_id).get()
        self.assertEqual(category.name, category_payload['name'])

    def test_invalid_post_category_with_non_existing_field(self):
        login_token = self.getLoginToken()

        category_payload = {
            "name": "category1",
            "disc": "response"
        }

        response = self.app.post('/api/categories',
                                 headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
                                 data=json.dumps(category_payload))

        self.assertEqual(400, response.status_code)
        self.assertEqual('Fields do not exist on the document', response.json['message'])

    def test_invalid_post_category_without_name_field(self):
        login_token = self.getLoginToken()

        category_payload = {}

        response = self.app.post('/api/categories',
                                 headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
                                 data=json.dumps(category_payload))

        self.assertEqual(400, response.status_code)
        self.assertEqual('Validation error or missing required fields', response.json['message'])

    def test_invalid_post_category_already_existing(self):
        login_token = self.getLoginToken()

        category_payload = {
            "name": "category1"
        }

        self.app.post('/api/categories',
                                 headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
                                 data=json.dumps(category_payload))

        response = self.app.post('/api/categories',
                                 headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
                                 data=json.dumps(category_payload))

        self.assertEqual(400, response.status_code)
        self.assertEqual('Category already exists', response.json['message'])

