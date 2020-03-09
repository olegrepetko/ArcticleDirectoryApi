import re
from datetime import datetime
import mongoengine_goodjson as gj
from flask_bcrypt import generate_password_hash, check_password_hash
from mongoengine import ValidationError

from api.database import db


class User(gj.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True)

    def generate_password_hash(self):
        if self.password is None\
                or not isinstance(self.password, str)\
                or not re.match(r'[A-Za-z0-9@#$%^&+=]{6,64}', self.password):
            raise ValidationError

        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Category(gj.Document):
    name = db.StringField(required=True, unique=True, min_length=2)


class Article(gj.Document):
    name = db.StringField(required=True, unique=True, min_length=2)
    description = db.StringField(required=True, min_length=2)
    link = db.URLField(required=True, unique=True)
    create_datetime = db.DateTimeField(required=True, default=datetime.utcnow)
    modify_datetime = db.DateTimeField(required=True, default=datetime.utcnow)
    categories = db.ListField(gj.FollowReferenceField('Category', reverse_delete_rule=db.DENY))
    added_by = db.ReferenceField('User')
