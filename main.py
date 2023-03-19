from flask import Flask
from flask_restful import Api
from Resources.user import ClientRegister, Delete
from Resources.product import Product


app = Flask(__name__)
api = Api(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite///My_data_base.sqlite3"




@app.before_first_request
def before_first_request():
    db.create_all()
#end points

api.add_resource(ClientRegister, "/register")
api.add_resource(Delete, "/delete")
api.add_resource(Product, "/product")

if __name__ == "__main__":
    app.run(debug=True)