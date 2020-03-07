from tests.base import BaseCase


class TestCategoryGetApi(BaseCase):

    def test_successful_get_category(self):
        category_name="category1"
        login_token = self.getLoginToken()

        category_id = self.createCategory(name=category_name,login_token=login_token)

        response = self.app.get('/api/category/{0}'.format(category_id),
                                headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"})

        self.assertEqual(200, response.status_code)
        self.assertEqual(category_id, response.json["id"])
        self.assertEqual(category_name, response.json["name"])

    def test_invalid_get_category_id_invalid(self):
        login_token = self.getLoginToken()

        category_id = "none"

        response = self.app.get('/api/category/{0}'.format(category_id),
                                headers={"Authorization": f"Bearer {login_token}"})

        self.assertEqual(400, response.status_code)
        self.assertEqual('Invalid Id', response.json['message'])

    def test_invalid_edit_category_non_exist(self):
        login_token = self.getLoginToken()

        category_id = "5e612a71be8f89cb1914e9ba"

        response = self.app.get('/api/category/{0}'.format(category_id),
                                headers={"Authorization": f"Bearer {login_token}"})

        self.assertEqual(400, response.status_code)
        self.assertEqual('Category not exists', response.json['message'])