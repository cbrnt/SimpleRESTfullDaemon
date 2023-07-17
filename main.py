from flask import Flask
from flask_restful import Resource, Api, reqparse
import uuid


class GenerateUUID(Resource):
    def get(self):
        return {
            "uuid": f"{uuid.uuid4()}"
        }

    def post(self):
        pass


if __name__ == "__main__":
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(GenerateUUID, '/uuid/')
    app.run(debug=True)
