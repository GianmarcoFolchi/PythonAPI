from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
names = {}
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

class PersonModel(db.Model): 
    email = db.Column(db.String(50), primary_key = True)
    name = db.Column(db.String(20))
    age = db.Column(db.Integer, nullable = False)
    gender = db.Column(db.String(10), nullable = False)


personPutArgs = reqparse.RequestParser() 
personPutArgs.add_argument("age", type = int, help = "Age of person is required", required = True) 
personPutArgs.add_argument("gender", type = str, help = "gender of person is required", required = True) 
personPutArgs.add_argument("email", type = str, help = "email of person is required", required = True) 

personPatchArgs = reqparse.RequestParser()
personPatchArgs.add_argument("age", type = int, help = "Age of person") 
personPatchArgs.add_argument("gender", type = str, help = "Gender of person") 
personPatchArgs.add_argument("email", type = str, help = "Email of person") 

resource_fields = {
    "name": fields.String, 
    "age": fields.Integer, 
    "gender": fields.String,
    "email": fields.String
}

def checkIfPersonExists(email):  
    result = PersonModel.query.filter_by(email = email).first()
    if result is not None:
        return True
    else: 
        return False

class HelloWorld(Resource): 
    @marshal_with(resource_fields)
    def get(self, name):  
        result = PersonModel.query.filter_by(name = name).first()
        if not result:
            abort(409, message = "Person does not exist.")
        return result
    
    @marshal_with(resource_fields)
    def post(self, name): 
        args = personPutArgs.parse_args()
        if checkIfPersonExists(args["email"]): 
            return PersonModel.query.get(args["email"]), 201
        person = PersonModel(name = name, age = args["age"], gender = args["gender"], email = args["email"])
        db.session.add(person)
        db.session.commit()
        return person, 201
    
    @marshal_with(resource_fields)
    def patch(self, name):
        args = personPatchArgs.parse_args()
        result = PersonModel.query.filter_by(name = name).first()
        if not result: 
            abort(404, message = "Person does not exist.")
            
        if args["age"]:
            result.age = args["age"]
        if args["email"]:
            result.email = args["email"]
        if args["gender"]:
            result.gender = args["gender"]
            
        db.session.commit()
        return result

api.add_resource(HelloWorld, "/helloworld/<string:name>")

if __name__ == "__main__": 
    app.run(debug = True)
    