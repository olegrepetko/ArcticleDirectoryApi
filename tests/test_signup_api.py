import json

from tests.base import BaseCase


class TestSignUpApi(BaseCase):

    def test_successful_signup(self):
        user_payload = {
            "email": "test@mail.com",
            "password": "password"
        }

        response = self.app.post("/api/auth/signup", headers={"Content-Type": "application/json"},
                                 data=json.dumps(user_payload))

        self.assertEqual(str, type(response.json['id']))
        self.assertEqual(200, response.status_code)

    def test_invalid_signup_with_non_existing_field(self):
        user_payload = {
            "email": "test@mail.com",
            "password": "password",
            "about_me": "info about me"
        }

        response = self.app.post("/api/auth/signup", headers={"Content-Type": "application/json"},
                                 data=json.dumps(user_payload))

        self.assertEqual('Fields do not exist on the document', response.json['message'])
        self.assertEqual(400, response.status_code)

    def test_invalid_signup_without_email(self):
        user_payload = {
            "password": "password"
        }

        response = self.app.post("/api/auth/signup", headers={"Content-Type": "application/json"},
                                 data=json.dumps(user_payload))

        self.assertEqual('Validation error or missing required fields', response.json['message'])
        self.assertEqual(400, response.status_code)

    def test_invalid_signup_without_password(self):
        user_payload = {
            "email": "test@mail.com"
        }

        response = self.app.post("/api/auth/signup", headers={"Content-Type": "application/json"},
                                 data=json.dumps(user_payload))

        self.assertEqual('Validation error or missing required fields', response.json['message'])
        self.assertEqual(400, response.status_code)

    def test_invalid_signup_already_existing_user(self):
        user_payload = {
            "email": "test@mail.com",
            "password": "password"
        }

        self.app.post("/api/auth/signup", headers={"Content-Type": "application/json"},
                                 data=json.dumps(user_payload))

        response = self.app.post("/api/auth/signup", headers={"Content-Type": "application/json"},
                                 data=json.dumps(user_payload))

        self.assertEqual(400, response.status_code)
        self.assertEqual('Email already exists', response.json['message'])

    def test_invalid_signup_with_wrong_email(self):
        user_payload = {
            "email": "test",
            "password": "password"
        }

        response = self.app.post("/api/auth/signup", headers={"Content-Type": "application/json"},
                                 data=json.dumps(user_payload))

        self.assertEqual(400, response.status_code)
        self.assertEqual('Validation error or missing required fields', response.json['message'])

    def test_invalid_signup_with_wrong_password(self):
        user_payload = {
            "email": "test@test.com",
            "password": "0"
        }

        response = self.app.post("/api/auth/signup", headers={"Content-Type": "application/json"},
                                 data=json.dumps(user_payload))

        self.assertEqual(400, response.status_code)
        self.assertEqual('Validation error or missing required fields', response.json['message'])
