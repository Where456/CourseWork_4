from project.dao.genre import GenreDao


class GenreService:
    def __init__(self, dao: GenreDao):
        self.dao = dao

    def get_one(self, aid):
        return self.dao.get_one(aid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        aid = data.get("id")
        user = self.get_one(aid)

        if "name" in data:
            user.email = data.get("name")
        self.dao.update(user)

    def delete(self, aid):
       return self.dao.delete(aid)