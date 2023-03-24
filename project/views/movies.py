from flask import request
from flask_restx import Resource, Namespace
from project.dao.model.movie import MovieSchema
from project.container import movie_service
from project.decorater import auth_required

movie_ns = Namespace('movie')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    @auth_required
    def get(self):
        status = request.args.get("status")
        page = request.args.get('page')
        filters = {
            "status": status,
            "page": page,
        }
        all_movies = movie_service.get_all(filters)
        return movies_schema.dump(all_movies), 200

    @auth_required
    def post(self):
        req_json = request.json
        movie_service.create(req_json)
        return 'Added', 201


@movie_ns.route('/<int:rid>')
class MovieView(Resource):
    @auth_required
    def get(self, rid):
        movie = movie_service.get_one(rid)
        return movie_schema.dump(movie), 200

    @auth_required
    def put(self, rid):
        req_json = request.json
        if 'id' not in req_json:
            req_json['id'] = rid
        movie_service.update(req_json)
        return 'Updated', 204

    @auth_required
    def delete(self, rid):
        movie_service.delete(rid)
        return 'Deleted', 204
