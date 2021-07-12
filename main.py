from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
names = {}
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

class NameModel(db.Model): 
    name = db.Column(db.String(20), primary_key = True)
    age = db.Column(db.Integer, nullable = False)
    email = db.Column(db.String(50), nullable = False)
    

namesPutArgs = reqparse.RequestParser() 
namesPutArgs.add_argument("age", type = int, help = "Age of person is required", required = True) 
namesPutArgs.add_argument("gender", type = str, help = "gender of person is required", required = True) 
namesPutArgs.add_argument("email", type = str, help = "email of person is required", required = True) 

def abortIfNameDNE(name):
    if name not in names: 
        abort(404, message = "Name not found")
        
def abortIfNameExists(name): 
    if name in names: 
        abort(409, message = "A person with that name already exists")

class HelloWorld(Resource): 
    def get(self, name):  
        abortIfNameDNE(name)
        return names[name]
    
    def put(self, name): 
        abortIfNameExists(name)
        args = namesPutArgs.parse_args()
        names[name] = args
        return names[name], 201
    
    def delete(self, name):
        abortIfNameDNE(name)
        del names[name]
        return "", 204
        

api.add_resource(HelloWorld, "/helloworld/<string:name>")

if __name__ == "__main__": 
    app.run(debug = True)
    