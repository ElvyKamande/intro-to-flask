from flask import Flask
from flask_migrate import Migrate
from models import db, User
from flask_restful import Api, Resource

app =  Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/about')
def about():
    return "This is the about page."
@app.route("/<username>")
def username(username):
    return f"Hello, {username}!"




if __name__ == '__main__':
    app.run(debug=True, port=5500, host='0.0.0.0')

    
    class PostEndpoint(Resource):
        def get(self):
            return {"message": "GET request received"}

        def post(self):
            return {"message": "POST request received"} 