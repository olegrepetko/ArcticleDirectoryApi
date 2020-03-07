import json

from tests.base import BaseCase
from api.database.model import Category


class TestCategoryPostApi(BaseCase):

    def test_successful_delete_category(self):
        login_token = self.getLoginToken()

        category_id = self.createCategory(name="category1", login_token=login_token)

        response = self.app.delete('/api/category/{0}'.format(category_id),
                                   headers={"Authorization": f"Bearer {login_token}"})

        self.assertEqual(200, response.status_code)
        self.assertEqual(Category.objects(id=category_id).count(), 0)

    def test_invalid_delete_category_id_invalid(self):
        login_token = self.getLoginToken()

        category_id = "none"

        response = self.app.delete('/api/category/{0}'.format(category_id),
                                   headers={"Authorization": f"Bearer {login_token}"})

        self.assertEqual(400, response.status_code)
        self.assertEqual('Invalid Id', response.json['message'])

    def test_invalid_delete_category_non_exist(self):
        login_token = self.getLoginToken()

        category_id = "5e612a71be8f89cb1914e9ba"

        response = self.app.delete('/api/category/{0}'.format(category_id),
                                   headers={"Authorization": f"Bearer {login_token}"})

        self.assertEqual(400, response.status_code)
        self.assertEqual('Category not exists', response.json['message'])
