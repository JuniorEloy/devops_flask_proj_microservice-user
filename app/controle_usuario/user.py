from flask_restful import Resource

class User(Resource):
    def get(self):
        return {"usuario": "franloy",
                "senha": "123123"}
