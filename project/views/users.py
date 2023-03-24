from flask import request
from flask_restx import Resource, Namespace
from project.container import user_service
from project.dao.model.user import UserSchema
from project.decorater import auth_required

user_ns = Namespace('user')
user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route('/')
class UsersView(Resource):
    @auth_required
    def get(self):
        return users_schema.dump(user_service.get_all()), 200

    @auth_required
    def post(self):
        req_data = request.json
        user_service.create(req_data)
        return "Added", 201


@user_ns.route('/<int:rid>')
class UserView(Resource):
    @auth_required
    def get(self, rid):
        user = user_service.get_one(rid)
        return user_schema.dump(user), 200

    @auth_required
    def patch(self, bid):
        req_data = request.json
        user_service.update(req_data, bid)
        return "Updated", 201


@user_ns.route('/password/<int:rid>')
class UserPassword(Resource):
    @auth_required
    def put(self, rid):
        req_data = request.json
        user_service.update(req_data, rid)
        return "Updated", 204
