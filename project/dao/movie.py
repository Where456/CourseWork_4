from project.dao.model.movie import Movie
from sqlalchemy import desc


class MovieDao:
    def __init__(self, session):
        self.session = session

    def get_one(self, aid):
        return self.session.query(Movie).get(aid)

    def get_all(self):
        return self.session.query(Movie).all()

    def get_by_status(self):
        return self.session.query(Movie).order_by(desc(Movie.year))

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()
        return movie

    def delete(self, aid):
        movie = self.get_one(aid)
        self.session.delete(movie)
        self.session.commit()
        return movie
