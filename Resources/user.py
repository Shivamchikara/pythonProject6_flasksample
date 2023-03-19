from flask_restful import Resource, reqparse
from Models.user_model import ClientUser

class ClientRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", required=True)
    parser.add_argument("password", required=True)
    parser.add_argument("email", required=True)



    @classmethod
    def post(cls):
        args = cls.parser.parse_args()
        if ClientUser.find_user_by_email(args("email")):
            return {"message": "user already exists"}
        user_obj = ClientUser(args)
        user_obj.save_to()
        return {"message": "user register"}


class Delete(Resource):

    def delete(self, email):
        user_obj= ClientUser.find_user_by_email(email=email)
        if user_obj:
            user_obj.delete_to()
        return {"message": "user deleted successfully"}