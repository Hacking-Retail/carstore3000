from flask_httpauth import HTTPBasicAuth
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


api = Api()
auth = HTTPBasicAuth()
db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
