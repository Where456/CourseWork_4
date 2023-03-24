from project.dao.model.director import Director


class DirectorDao:
    def __init__(self, session):
        self.session = session

    def get_one(self, aid):
        return self.session.query(Director).get(aid)

    def get_all(self):
        return self.session.query(Director).all()

    def create(self, data):
        director = Director(**data)
        self.session.add(director)
        self.session.commit()
        return director

    def update(self, director):
        self.session.add(director)
        self.session.commit()
        return director

    def delete(self, aid):
        director = self.get_one(aid)
        self.session.delete(director)
        self.session.commit()
        return director
