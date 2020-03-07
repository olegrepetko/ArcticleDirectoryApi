from flask import Flask
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

from .errors import errors
from .database import initialize_db
from .routers import initialize_routers


app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')
api = Api(app, errors=errors)
b_crypt = Bcrypt(app)
jwt = JWTManager(app)

initialize_db(app)
initialize_routers(api)
