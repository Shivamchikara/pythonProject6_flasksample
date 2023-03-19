from db import db

class ClientUser(db.Model):
    __tablename__ = "Users"


    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(50))
    email = db.Column(db.String(50))


    def __init__(self, data):
        self.id = data["id"]
        self.username = data["username"]
        self.password = data["password"]
        self.email = data["email"]



    @classmethod
    def find_user_by_email(cls):
        return cls.query.filter_by(email=email)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()



    def delete_to_db(self):
        db.session.delete(self)
        db.session.commit()