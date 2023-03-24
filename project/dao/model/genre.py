from marshmallow import Schema, fields

from project.setup import db


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()