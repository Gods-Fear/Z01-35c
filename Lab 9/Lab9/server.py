from flask import Flask
from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy
from safrs import SAFRSAPI, SAFRSBase
from sqlalchemy.orm import Session

host = "localhost"
dbAl = SQLAlchemy()

messages = ""
id_i = ""
passwords = ""
destination = ""
new_user_name, new_user_password = "", ""


class ClientSent(Resource):
    def get(self, id, password, message, destination):
        global id_i, messages, passwords, destinations
        id_i, messages, passwords, destinations = id, message, password, destination
        user = User(name=id_i, password=passwords, message=messages, destination=destinations, new_name=new_user_name, new_password=new_user_password)
        dbAl.session(user)
        dbAl.session.commit()
        User.query.all()

        return {"name": id_i, "password": passwords, "message": messages, "destination": destinations}

    # def post(self):
    #     return "logIn successful"


class ClientSentNew(Resource):
    def get(self, new_name, new_password):
        global new_user_name, new_user_password
        new_user_name, new_user_password = new_name, new_password
        user = User(name="", password="", message="", destination="", new_name=new_user_name, new_password=new_user_password)
        dbAl.session(user)
        dbAl.session.commit()
        User.query.all()
        return {"new_user": new_user_name, "new_password": new_user_password}


class User(SAFRSBase, dbAl.Model):
    __tablename__ = "Users"

    name = dbAl.Column(dbAl.String, primary_key=True)
    password = dbAl.Column(dbAl.String)
    message = dbAl.Column(dbAl.String)
    destination = dbAl.Column(dbAl.String)

    new_name = dbAl.Column(dbAl.String)
    new_password = dbAl.Column(dbAl.String)


def create_api(app, HOST="localhost", PORT=5000):
    api = SAFRSAPI(app, host=HOST, port=PORT)
    api.add_resource(ClientSent, "/server/<string:id>/<string:password>/<string:message>/<string:destination>")
    api.add_resource(ClientSentNew, "/server_new/<string:new_name>/<string:new_password>")
    api.expose_object(User)
    print("Starting API: http://{}:{}".format(HOST, PORT))


def create_app(config_filename=None, host="localhost"):
    app = Flask("demo_app")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config.update(SQLALCHEMY_DATABASE_URI="sqlite://")
    dbAl.init_app(app)
    with app.app_context():
        dbAl.create_all()
        create_api(app, host)
    return app


app = create_app(host=host)

if __name__ == "__main__":
    app.run(host=host)
    Session.close()