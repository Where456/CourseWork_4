import calendar
import datetime

import jwt
from flask import abort

from project.constants import SALT, ALG0, SECRET_HERE
from project.services.users_service import UserService


class AuthService:
    def __init__(self, service: UserService):
        self.service = service

    def generate_token(self, email, password, is_refresh=False):
        user = self.service.get_by_email(email)
        if user is None:
            abort(404)

        if not is_refresh:
            if not self.service.compare_passwords(user.password, password):
                abort(400)

        data = {
            "email": user.email,
            "name": user.name,
            "surname": user.surname,
            "favorite_genre": user.favorite_genre,
            "role": user.role
        }
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, SALT, algorithm=ALG0)
        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, SALT, algorithm=ALG0)
        tokens = {"access_token": access_token, "refresh_token": refresh_token}

        return tokens

    def approve_refresh_token(self, refresh_token):
        data = jwt.decode(jwt=refresh_token, key=SECRET_HERE, algorithms=[ALG0])
        email = data.get('email')
        return self.generate_token(email, None, True)