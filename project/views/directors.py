from flask import request
from flask_restx import Resource, Namespace
from project.dao.model.director import DirectorSchema
from project.container import director_service
from project.decorater import auth_required

director_ns = Namespace('director')
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        all_directors = director_service.get_all()
        return directors_schema.dump(all_directors), 200

    @auth_required
    def post(self):
        req_json = request.json
        director_service.create(req_json)
        return 'Added', 201


@director_ns.route('/<int:rid>')
class DirectorView(Resource):
    @auth_required
    def get(self, rid):
        director = director_service.get_one(rid)
        return director_schema.dump(director), 200

    @auth_required
    def put(self, rid):
        req_json = request.json
        if 'id' not in req_json:
            req_json['id'] = rid
        director_service.update(req_json)
        return 'Updated', 204

    @auth_required
    def delete(self, rid):
        director_service.delete(rid)
        return 'Deleted', 204
