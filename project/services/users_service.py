import base64
import hashlib
import hmac

from project.constants import SALT, ITERATION
from project.dao.user import UserDao


class UserService:
    def __init__(self, dao: UserDao):
        self.dao = dao

    def get_one(self, aid):
        return self.dao.get_one(aid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def get_by_email(self, email):
        return self.dao.get_by_email(email)

    def generate_password(self, password):
        return base64.b64encode(hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            SALT,
            ITERATION
        ))

    def create_user(self, data):
        return self.dao.create(data)

    def compare_passwords(self, password_hash, other_password) -> bool:
        return hmac.compare_digest(
            base64.b64decode(password_hash),
            hashlib.pbkdf2_hmac('sha256', other_password.encode(), SALT, ITERATION)
        )

    def update(self, data):
        aid = data.get("id")
        user = self.get_one(aid)

        if "email" in data:
            user.email = data.get("email")
        if "password" in data:
            user.email = data.get("password")
        if "name" in data:
            user.email = data.get("name")
        if "surname" in data:
            user.email = data.get("surname")
        if "favorite_genre" in data:
            user.email = data.get("favorite_genre")
        self.dao.update(user)

    def delete(self, aid):
        return self.dao.delete(aid)
