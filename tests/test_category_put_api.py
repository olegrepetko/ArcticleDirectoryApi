import json

from tests.base import BaseCase
from api.database.model import Category


class TestCategoryPutApi(BaseCase):

    def test_successful_put_category(self):
        login_token = self.getLoginToken()

        category_id = self.createCategory(name="category1",login_token=login_token)

        category_edit_payload = {
            "name": "new_category1"
        }

        response = self.app.put('/api/category/{0}'.format(category_id),
                                 headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
                                 data=json.dumps(category_edit_payload))

        self.assertEqual(200, response.status_code)

        category = Category.objects(id=category_id).get()
        self.assertEqual(category.name, category_edit_payload['name'])

    def test_invalid_put_category_id_invalid(self):
        login_token = self.getLoginToken()

        category_id = "none"

        category_edit_payload = {
            "name": "new_category1"
        }

        response = self.app.put('/api/category/{0}'.format(category_id),
                                headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
                                data=json.dumps(category_edit_payload))

        self.assertEqual(400, response.status_code)
        self.assertEqual('Invalid Id', response.json['message'])

    def test_invalid_put_category_with_non_existing_field(self):
        login_token = self.getLoginToken()

        category_id = self.createCategory(name="category1",login_token=login_token)

        category_edit_payload = {
            "name": "new_category1",
            "disc": "response"
        }

        response = self.app.put('/api/category/{0}'.format(category_id),
                                headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
                                data=json.dumps(category_edit_payload))

        self.assertEqual(400, response.status_code)
        self.assertEqual('Fields do not exist on the document', response.json['message'])

    def test_invalid_put_category_without_name_field(self):
        login_token = self.getLoginToken()

        category_id = self.createCategory(name="category1",login_token=login_token)

        category_edit_payload = {}

        response = self.app.put('/api/category/{0}'.format(category_id),
                                headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
                                data=json.dumps(category_edit_payload))

        self.assertEqual(400, response.status_code)
        self.assertEqual('Validation error or missing required fields', response.json['message'])

    def test_invalid_put_category_non_exist(self):
        login_token = self.getLoginToken()

        category_id = "5e612a71be8f89cb1914e9ba"

        category_edit_payload = {
            "name": "new_category1"
        }

        response = self.app.put('/api/category/{0}'.format(category_id),
                                headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
                                data=json.dumps(category_edit_payload))

        self.assertEqual(400, response.status_code)
        self.assertEqual('Category not exists', response.json['message'])
