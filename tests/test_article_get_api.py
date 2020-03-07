from tests.base import BaseCase


class TestArticleGetApi(BaseCase):

    def test_successful_get_article(self):
        login_token = self.getLoginToken()

        self.createCategory('test1', login_token)

        article_change_payload = {
            "name": "hello2",
            "description": "Use this with extreme caution2",
            "link": "http://example.com/hello2",
            "categories": ["test1"]
        }

        article_id = self.createArticle(login_token, article_change_payload)

        response = self.app.get('/api/article/{0}'.format(article_id),
                                   headers={"Authorization": f"Bearer {login_token}"})

        self.assertEqual(200, response.status_code)
        self.assertEqual(article_change_payload["name"], response.json['name'])
        self.assertEqual(article_change_payload["description"], response.json['description'])
        self.assertEqual(article_change_payload["link"], response.json['link'])
        self.assertEqual(article_change_payload["categories"].sort(), response.json['categories'].sort())

    def test_invalid_get_article_id_invalid(self):
        login_token = self.getLoginToken()

        self.createCategory('test1', login_token)

        article_id = "None"

        response = self.app.get('/api/article/{0}'.format(article_id),
                                   headers={"Authorization": f"Bearer {login_token}"})

        self.assertEqual(400, response.status_code)
        self.assertEqual('Invalid Id', response.json['message'])

    def test_invalid_get_article_non_exist(self):
        login_token = self.getLoginToken()

        self.createCategory('test1', login_token)

        article_id = "5e612a71be8f89cb1914e9ba"

        response = self.app.get('/api/article/{0}'.format(article_id),
                                   headers={"Authorization": f"Bearer {login_token}"})

        self.assertEqual(400, response.status_code)
        self.assertEqual('Article not exists', response.json['message'])