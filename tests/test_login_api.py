import json

from tests.base import BaseCase


class TestLoginApi(BaseCase):

    def test_successful_login(self):
        email = "test@mail.com"
        password = "password"
        user_payload = {
            "email": email,
            "password": password
        }

        response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"},
                                 data=json.dumps(user_payload))

        self.assertEqual(200, response.status_code)
        response = self.app.post('/api/auth/login', headers={"Content-Type": "application/json"}, data=json.dumps(user_payload))

    def test_invalid_login_with_wrong_email(self):
        email = "test@mail.com"
        password = "password"
        user_payload = {
            "email": email,
            "password": password
        }

        self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"},
                      data=json.dumps(user_payload))

        user_payload["email"] = "wrong_email@mail.com"

        response = self.app.post('/api/auth/login', headers={"Content-Type": "application/json"}, data=json.dumps(user_payload))
        self.assertEqual(401, response.status_code)

    def test_invalid_login_with_wrong_password(self):
        user_payload = {
            "email": "test@mail.com",
            "password": "password"
        }

        self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"},
                      data=json.dumps(user_payload))

        user_payload["password"] = "wrong_password"

        response = self.app.post('/api/auth/login', headers={"Content-Type": "application/json"}, data=json.dumps(user_payload))
        self.assertEqual(401, response.status_code)
