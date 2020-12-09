from flask import Flask, request
from flask_restful import Api, Resource, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from safrs import SAFRSAPI, SAFRSBase


db = SQLAlchemy()

messages = ""
id_i = 10


class ClientSent(Resource):
    def get(self, id, message):
        global id_i
        id_i, messages = id, message
        User(id=id_i, message=messages)
        return {"id": id_i, "message" : messages}


class User(SAFRSBase, db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String)


def create_api(app, HOST="localhost", PORT=5000):
    api = SAFRSAPI(app, host=HOST, port=PORT)
    api.add_resource(ClientSent, "/server/<int:id>/<string:message>")
    api.expose_object(User)
    print("Starting API: http://{}:{}".format(HOST, PORT))


def create_app(config_filename=None, host="localhost"):
    app = Flask("demo_app")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config.update(SQLALCHEMY_DATABASE_URI="sqlite://")
    db.init_app(app)
    with app.app_context():
        db.create_all()
        create_api(app, host)
    return app


host = "localhost"
app = create_app(host=host)

if __name__ == "__main__":
    app.run(host=host)
