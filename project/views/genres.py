from flask import request
from flask_restx import Resource, Namespace
from project.dao.model.genre import GenreSchema
from project.container import genre_service
from project.decorater import auth_required

genre_ns = Namespace('genre')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        all_genres = genre_service.get_all()
        return genres_schema.dump(all_genres), 200

    @auth_required
    def post(self):
        req_json = request.json
        genre_service.create(req_json)
        return 'Added', 201


@genre_ns.route('/<int:rid>')
class GenreView(Resource):
    @auth_required
    def get(self, rid):
        genre = genre_service.get_one(rid)
        return genre_schema.dump(genre), 200

    @auth_required
    def put(self, rid):
        req_json = request.json
        if 'id' not in req_json:
            req_json['id'] = rid
        genre_service.update(req_json)
        return 'Updated', 204

    @auth_required
    def delete(self, rid):
        genre_service.delete(rid)
        return 'Deleted', 204
