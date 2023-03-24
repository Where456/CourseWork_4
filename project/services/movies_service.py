from project.dao.movie import MovieDao


class MovieService:
    def __init__(self, dao: MovieDao):
        self.dao = dao

    def get_one(self, aid):
        return self.dao.get_one(aid)

    def get_all(self, movie_data):
        if movie_data.get("status") is not None and movie_data['status'] == 'new':
            movies = self.dao.get_by_status()
        else:
            movies = self.dao.get_all()
        if movie_data.get('page') is not None:
            return movies.limit(12).offset((int(movie_data.get('page')) - 1) * 12).all()
        return movies

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        aid = data.get("id")
        user = self.get_one(aid)

        if "title" in data:
            user.title = data.get("title")
        if "description" in data:
            user.description = data.get("description")
        if "trailer" in data:
            user.trailer = data.get("trailer")
        if "year" in data:
            user.year = data.get("year")
        if "rating" in data:
            user.rating = data.get("rating")
        if "genre_id" in data:
            user.genre_id = data.get("genre_id")
        if "director_id" in data:
            user.director_id = data.get("director_id")

        self.dao.update(user)

    def delete(self, aid):
       return self.dao.delete(aid)