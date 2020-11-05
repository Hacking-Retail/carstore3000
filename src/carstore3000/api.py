"""Carstore3000 API"""
from flask import Flask

from carstore3000.extensions import api, db, migrate, ma, auth
from carstore3000.views.cars import CarsRoutes
from carstore3000.views.users import UsersRoutes
from carstore3000.models.users import UserModel


@auth.verify_password
def verify_password(username, password):
    username = UserModel.query.filter_by(username=username).first()
    if not username or not username.verify_password(password):
        return False
    g.username = username
    return True


app = Flask(__name__)
app.config.from_object("carstore3000.config.DevelopmentConfig")

# Add debug at init
for k, v in app.config.items():
    print(k, v)

db.init_app(app)
migrate.init_app(app)
ma.init_app(app)
api.add_resource(CarsRoutes, '/api/v1/cars')
api.add_resource(UsersRoutes, '/api/v1/users')
api.init_app(app)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
