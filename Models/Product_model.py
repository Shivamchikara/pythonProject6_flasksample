from db import db

class ProductModel(db.Model):
    __tablename__ = "products"

    Pro_id = db.Column(db.Integer, primery_key=True)
    Pro_name = db.Column(db.String(100))
    Pro_price = db.Column(db.Float)

    def __init__(self, Pro_name, Pro_price):
        self.Pro_name = Pro_name
        self.Pro_price = Pro_price


    def json(self):
        return {"Pro_id": self.Pro_id,
                "Pro_name": self.Pro_name,
                "Pro_price": self.Pro_price}


    @classmethod
    def find_by_name(cls, Pro_name):
        return cls.query.filter_by(name=Pro_name).first()

    def Seve_to_db(self):
        db.session.add(self)
        db.session.commit()