import json
import unittest

from api import app
from api.database import db


class BaseCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.db = db.get_db()

    def tearDown(self):
        for collection in self.db.list_collection_names():
            self.db.drop_collection(collection)

    def getLoginToken(self, email="test@mail.com", password="password"):
        user_payload = {
            "email": email,
            "password": password
        }

        self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"},
                      data=json.dumps(user_payload))
        response = self.app.post('/api/auth/login', headers={"Content-Type": "application/json"},
                                 data=json.dumps(user_payload))
        return response.json['token']

    def createCategory(self, name, login_token):
        category_payload = {
            "name": name
        }

        response = self.app.post('/api/categories',
                                 headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
                                 data=json.dumps(category_payload))
        return response.json['id']

    def createArticle(self, login_token, article_body={
            "name": "hello1",
            "description": "Use this with extreme caution",
            "link": "http://example.com/hello1",
            "categories": ["test1"]
        }):
        response = self.app.post('/api/articles',
                                 headers={"Content-Type": "application/json", "Authorization": f"Bearer {login_token}"},
                                 data=json.dumps(article_body))
        return response.json['id']
