import json

from tests.base import BaseCase
from api.database.model import Article


class TestArticlesPutApi(BaseCase):

    def test_successful_put_article(self):
        login_token = self.getLoginToken()

        self.createCategory('test1', login_token)
        self.createCategory('test2', login_token)

        article_id = self.createArticle(login_token)

        article_change_payload = {
            "name": "hello2",
            "description": "Use this with extreme caution2",
            "link": "http://example.com/hello2",
            "categories": ["test2"]
        }

        response = self.app.put('/api/article/{0}'.format(article_id),
                                headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
                                data=json.dumps(article_change_payload))

        self.assertEqual(200, response.status_code)

        article = Article.objects(id=article_id).get()
        categories = [category.name for category in article.categories]
        self.assertEqual(article.name, article_change_payload['name'])
        self.assertEqual(article.description, article_change_payload['description'])
        self.assertEqual(article.link, article_change_payload['link'])
        self.assertEqual(categories.sort(), article_change_payload['categories'].sort())

    def test_invalid_put_article_id_invalid(self):
        login_token = self.getLoginToken()
        article_id = "None"

        article_change_payload = {
            "name": "hello2"
        }

        response = self.app.put('/api/article/{0}'.format(article_id),
                                headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
                                data=json.dumps(article_change_payload))

        self.assertEqual(400, response.status_code)
        self.assertEqual('Invalid Id', response.json['message'])

    def test_invalid_put_article_with_non_existing_field(self):
        login_token = self.getLoginToken()

        self.createCategory('test1', login_token)
        self.createCategory('test2', login_token)

        article_id = self.createArticle(login_token)

        article_change_payload = {
            "invalid_field": "hello"
        }

        response = self.app.put('/api/article/{0}'.format(article_id),
                                headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
                                data=json.dumps(article_change_payload))

        self.assertEqual(400, response.status_code)
        self.assertEqual('Fields do not exist on the document', response.json['message'])

    def test_invalid_put_article_with_non_existing_category(self):
        login_token = self.getLoginToken()

        self.createCategory('test1', login_token)

        article_id = self.createArticle(login_token)

        article_change_payload = {
            "categories": ["test2"]
        }

        response = self.app.put('/api/article/{0}'.format(article_id),
                                headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
                                data=json.dumps(article_change_payload))

        self.assertEqual(400, response.status_code)
        self.assertEqual('Category not exists', response.json['message'])

    def test_invalid_put_article_with_empty_body(self):
        login_token = self.getLoginToken()

        self.createCategory('test1', login_token)
        self.createCategory('test2', login_token)

        article_id = self.createArticle(login_token)

        article_change_payload = {}

        response = self.app.put('/api/article/{0}'.format(article_id),
                                headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
                                data=json.dumps(article_change_payload))

        self.assertEqual(400, response.status_code)
        self.assertEqual('Validation error or missing required fields', response.json['message'])

    def test_invalid_put_article_with_non_exist(self):
        login_token = self.getLoginToken()

        article_id = "5e612a71be8f89cb1914e9ba"

        article_change_payload = {
            "name": "hello2"
        }

        response = self.app.put('/api/article/{0}'.format(article_id),
                                headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
                                data=json.dumps(article_change_payload))

        self.assertEqual(400, response.status_code)
        self.assertEqual('Article not exists', response.json['message'])