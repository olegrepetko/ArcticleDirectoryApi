from tests.base import BaseCase


class TestArticlesGetApi(BaseCase):

    def test_successful_get_articles(self):
        login_token = self.getLoginToken()

        self.createCategory('test1',login_token)
        self.createCategory('test2', login_token)

        article1 = {
            "name": "hello1",
            "description": "Use this with extreme caution",
            "link": "http://example.com/hello1",
            "categories": ["test1"]
        }
        article2 = {
            "name": "hello2",
            "description": "Use this with extreme caution",
            "link": "http://example.com/hello2",
            "categories": ["test2"]
        }
        article3 = {
            "name": "hello3",
            "description": "Use this with extreme caution",
            "link": "http://example.com/hello3",
            "categories": ["test1", "test2"]
        }
        self.createArticle(login_token, article1)
        self.createArticle(login_token, article2)
        self.createArticle(login_token, article3)

        response = self.app.get('/api/articles')

        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.json), 3)

        response = self.app.get('/api/articles', query_string={'category':'test2'})

        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.json), 2)

    def test_invalid_get_articles_non_exists_categories(self):
        response = self.app.get('/api/articles', query_string={'category': 'test2'})

        self.assertEqual(400, response.status_code)
        self.assertEqual('Category not exists', response.json['message'])
