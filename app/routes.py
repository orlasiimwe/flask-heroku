from app import app 
from flask import render_template 
from flask_restful import Api
from .controllers import (All_Posts,Posts_List)


# @app.route('/add')
# def index():
#     return render_template('index.html')

api = Api(app)

api.add_resource(All_Posts, '/show')
api.add_resource(Posts_List, '/post/<string:movie>')

@app.route('/')
def temp():
    return 'Welcome page'



    