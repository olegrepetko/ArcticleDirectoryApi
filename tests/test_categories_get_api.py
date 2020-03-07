from tests.base import BaseCase


class TestCategoriesGetApi(BaseCase):

    def test_successful_get_categories(self):
        login_token = self.getLoginToken()

        self.createCategory(name="category1",login_token=login_token)
        self.createCategory(name="category2", login_token=login_token)
        self.createCategory(name="category3", login_token=login_token)

        response = self.app.get('/api/categories')

        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.json), 3)