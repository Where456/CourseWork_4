from project.dao.director import DirectorDao
from project.dao.genre import GenreDao
from project.dao.movie import MovieDao
from project.dao.user import UserDao
from project.services.auth_service import AuthService
from project.services.directors_service import DirectorService
from project.services.genres_service import GenreService
from project.services.movies_service import MovieService
from project.services.users_service import UserService

from project.setup import db

# DAO
genre_dao = GenreDao(db.session)
director_dao = DirectorDao(db.session)
movie_dao = MovieDao(db.session)
user_dao = UserDao(db.session)

# Services
genre_service = GenreService(dao=genre_dao)
director_service = DirectorService(dao=director_dao)
movie_service = MovieService(dao=movie_dao)
user_service = UserService(dao=user_dao)
auth_service = AuthService(user_service)
