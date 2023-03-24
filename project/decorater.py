import jwt
from flask import abort, request
from project.constants import SECRET_HERE, ALG0

def auth_required(func):
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401)

        data = request.headers["Authorization"]
        token = data.split("Bearer ")[-1]

        try:
            jwt.decode(token, SECRET_HERE, algorithms=[ALG0])
        except Exception:
            abort(401)

        return func(*args, **kwargs)

    return wrapper