"""Carstore3000 API"""
from flask import Flask
from carstore3000.extensions import db


app = Flask(__name__)
app.config.from_object("carstore3000.config.DevelopmentConfig")

# Add debug at init
for k, v in app.config.items():
    print(k, v)

db.init_app(app)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
