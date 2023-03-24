from project.dao.model.user import User


class UserDao:
    def __init__(self, session):
        self.session = session

    def get_one(self, aid):
        return self.session.query(User).get(aid)

    def get_all(self):
        return self.session.query(User).all()

    def get_by_email(self, email):
        return self.session.query(User).filter(User.email == email).first()

    def create(self, data):
        user = User(**data)
        self.session.add(user)
        self.session.commit()
        return user

    def update(self, user):
        self.session.add(user)
        self.session.commit()
        return user

    def delete(self, aid):
        user = self.get_one(aid)
        self.session.delete(user)
        self.session.commit()
        return user
