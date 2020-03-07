import json

from tests.base import BaseCase
from api.database.model import Article


class TestArticleDeleteApi(BaseCase):

    def test_successful_delete_article(self):
        login_token = self.getLoginToken()

        self.createCategory('test1', login_token)

        article_id = self.createArticle(login_token)

        response = self.app.delete('/api/article/{0}'.format(article_id),
                                   headers={"Authorization": f"Bearer {login_token}"})

        self.assertEqual(200, response.status_code)
        self.assertEqual(Article.objects(id=article_id).count(), 0)

    def test_invalid_delete_article_id_invalid(self):
        login_token = self.getLoginToken()

        self.createCategory('test1', login_token)

        article_id = "None"

        response = self.app.delete('/api/article/{0}'.format(article_id),
                                   headers={"Authorization": f"Bearer {login_token}"})

        self.assertEqual(400, response.status_code)
        self.assertEqual('Invalid Id', response.json['message'])

    def test_invalid_delete_article_non_exist(self):
        login_token = self.getLoginToken()

        self.createCategory('test1', login_token)

        article_id = "5e612a71be8f89cb1914e9ba"

        response = self.app.delete('/api/article/{0}'.format(article_id),
                                   headers={"Authorization": f"Bearer {login_token}"})

        self.assertEqual(400, response.status_code)
        self.assertEqual('Article not exists', response.json['message'])