from project.dao.model.genre import Genre


class GenreDao:
    def __init__(self, session):
        self.session = session

    def get_one(self, aid):
        return self.session.query(Genre).get(aid)

    def get_all(self):
        return self.session.query(Genre).all()

    def create(self, data):
        genre = Genre(**data)
        self.session.add(genre)
        self.session.commit()
        return genre

    def update(self, genre):
        self.session.add(genre)
        self.session.commit()
        return genre

    def delete(self, aid):
        genre = self.get_one(aid)
        self.session.delete(genre)
        self.session.commit()
        return genre
