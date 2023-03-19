from flask_restful import Resource, reqparse

from Models.Product_model import ProductModel

class Product(Resource):
    parser = reqparse.RequestParser
    parser.add_argument("Pro_price", type=float, required=True)


    @classmethod
    def get(cls, Pro_name):
        args = cls.parser.parse_args()
        if ProductModel.find_by_name(args("Pro_name"))
            return {"message": "product already exists"}
        pro_obj = ProductModel(args)
        pro_obj.save_to()
        return {"message":"product register"}


    @classmethod
    def post(self, Pro_name):
        if ProductModel.find_by_name(Pro_name):
            return {"message": "product already exists"}