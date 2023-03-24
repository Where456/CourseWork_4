from flask import request, abort
from flask_restx import Namespace, Resource
from project.container import user_service, auth_service

auth_ns = Namespace('auth')


@auth_ns.route('/register')
class AuthView(Resource):
    def post(self):
        req_data = request.json
        user_service.create_user(req_data)
        return 'Registered', 201

@auth_ns.route('/login')
class AuthView(Resource):

    def post(self):
        req_data = request.json
        email = req_data.get('email')
        password = req_data.get('password')
        if email is None or password is None:
            return abort(400)
        tokens = auth_service.generate_token(email, password)
        return tokens, 201

    def put(self):
        req_data = request.json
        refresh_token = req_data.get('refresh_token')
        if refresh_token is None:
            return abort(401)

        tokens = auth_service.approve_refresh_token(refresh_token)
        return tokens, 201
