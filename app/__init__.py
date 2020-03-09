from flask_restful import Api
from flask import Flask
from .config import config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    api = Api(app, prefix="/api")

    from app.controle_usuario.user import User
    api.add_resource(User, "/user")
    
    return app