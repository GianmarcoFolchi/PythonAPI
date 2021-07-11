from flask import Flask
from flask_restful import Api, Resource, reqparse
#resqparse in not accesed

app = Flask(__name__)
api = Api(app)
name(kdfjjdk)
names = {}
editor.action.insertCursorAtEndOfEachLineSelected

# namesPutArgs = flask_restful.reqparse.RequestParser() 
# namesPutArgs = add_argument("age", type = int, help = "Age of person") 
# namesPutArgs = add_argument("gender", type = str, help = "gender of person") 
# namesPutArgs = add_argument("email", type = str, help = "email of person") 

class HelloWorld(Resource): 
    # def get(self, name):  
    #     return names[name]
    
    def put(self, name): 
        args = namesPutArgs.parse_args()
        return {name: args}

api.add_resource(HelloWorld, "/helloworld/<string:name>")

if __name__ == "__main__": 
    app.run(debug = True)
    