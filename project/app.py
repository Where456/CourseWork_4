from flask import Flask
from flask_restx import Api

from project.setup import db
from project.views.auth import auth_ns
from project.views.directors import director_ns
from project.views.genres import genre_ns
from project.views.movies import movie_ns
from project.views.users import user_ns
from project.config import Config


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)
    create_data(app, db)


def create_data(app, db):
    with app.app_context():
        db.drop_all()
        db.create_all()


config = Config()
app = create_app(config)
app.debug = True

if __name__ == '__main__':
    app.run()
