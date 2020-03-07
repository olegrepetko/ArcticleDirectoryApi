import json

from tests.base import BaseCase
from api.database.model import Category, Article


class TestArticlesPostApi(BaseCase):

    def test_successful_post_article(self):
        login_token = self.getLoginToken()

        self.createCategory("test1", login_token)
        self.createCategory("test2", login_token)

        article_payload = {
            "name": "hello",
            "description": "Use this with extreme caution",
            "link": "http://example.com/hello",
            "categories": ["test1", "test2"]
        }

        response = self.app.post('/api/articles',
                                 headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
                                 data=json.dumps(article_payload))
        article_id = response.json['id']

        self.assertEqual(200, response.status_code)

        article = Article.objects(id=article_id).get()
        categories = [category.name for category in article.categories]
        self.assertEqual(article.name, article_payload['name'])
        self.assertEqual(article.description, article_payload['description'])
        self.assertEqual(article.link, article_payload['link'])
        self.assertEqual(categories.sort(), article_payload['categories'].sort())

    def test_invalid_post_article_with_non_existing_field(self):
        login_token = self.getLoginToken()

        self.createCategory("test1", login_token)
        self.createCategory("test2", login_token)

        article_payload = {
            "name": "hello",
            "description": "Use this with extreme caution",
            "link": "http://example.com/hello",
            "categories": ["test1", "test2"],
            "shop": "auchan"
        }

        response = self.app.post('/api/articles',
                                 headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
                                 data=json.dumps(article_payload))

        self.assertEqual(400, response.status_code)
        self.assertEqual('Fields do not exist on the document', response.json['message'])

    def test_invalid_post_article_without_category(self):
        login_token = self.getLoginToken()

        self.createCategory("test1", login_token)
        self.createCategory("test2", login_token)

        article_payload = {
            "name": "hello",
            "description": "Use this with extreme caution",
            "link": "http://example.com/hello",
        }

        response = self.app.post('/api/articles',
                                 headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
                                 data=json.dumps(article_payload))

        self.assertEqual(400, response.status_code)
        self.assertEqual('Validation error or missing required fields', response.json['message'])

    def test_invalid_post_article_without_fields(self):
        login_token = self.getLoginToken()

        self.createCategory("test1", login_token)
        self.createCategory("test2", login_token)

        article_payload = {
            "name": "hello",
            "categories": ["test1", "test2"]
        }

        response = self.app.post('/api/articles',
                                 headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
                                 data=json.dumps(article_payload))

        self.assertEqual(400, response.status_code)
        self.assertEqual('Validation error or missing required fields', response.json['message'])

    def test_invalid_post_article_non_exists_categories(self):
        login_token = self.getLoginToken()

        self.createCategory("test1", login_token)

        article_payload = {
            "name": "hello",
            "description": "Use this with extreme caution",
            "link": "http://example.com/hello",
            "categories": ["test1", "test2"]
        }

        response = self.app.post('/api/articles',
                                 headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
                                 data=json.dumps(article_payload))

        self.assertEqual(400, response.status_code)
        self.assertEqual('Category not exists', response.json['message'])

    def test_invalid_post_article_without_auth(self):
        login_token = self.getLoginToken()
        self.createCategory("test1", login_token)
        self.createCategory("test2", login_token)

        login_token_wrone = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODM0MTcyNDAsIm5iZiI6MTU4MzQxNzI0MCw" \
                      "ianRpIjoiNjVmNjU4ZmYtZmQxYS00NzUzLWE5ZjktNzFjZDcyZjQ4MTg4IiwiZXhwIjoxNTg0MDIyMDQwLCJ" \
                      "pZGVudGl0eSI6IjVlNjEwNmVhNWNiZGIzNTNiNTlmMGIwNiIsImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2V" \
                      "zcyJ9.xHQGA4KZjSXWNKKHIgIO7smXfS2mcLh8rYiXf58Pgbs"

        article_payload = {
            "name": "hello",
            "description": "Use this with extreme caution",
            "link": "http://example.com/hello",
            "categories": ["test1", "test2"]
        }

        response = self.app.post('/api/articles',
                                 headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token_wrone}"},
                                 data=json.dumps(article_payload))

        self.assertEqual(401, response.status_code)
        self.assertEqual('Invalid Authorization', response.json['message'])

    def test_invalid_post_article_already_existing(self):
        login_token = self.getLoginToken()

        self.createCategory("test1", login_token)
        self.createCategory("test2", login_token)

        article_payload = {
            "name": "hello",
            "description": "Use this with extreme caution",
            "link": "http://example.com/hello",
            "categories": ["test1", "test2"]
        }

        self.app.post('/api/articles',
                                 headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
                                 data=json.dumps(article_payload))

        article_payload = {
            "name": "hello",
            "description": "everything seems fine now",
            "link": "http://example.com/hello",
            "categories": ["test1"]
        }

        response = self.app.post('/api/articles',
                                 headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
                                 data=json.dumps(article_payload))
        self.assertEqual(400, response.status_code)
        self.assertEqual('Name or link of article already exists', response.json['message'])