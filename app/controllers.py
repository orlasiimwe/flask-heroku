from flask import Blueprint,json,request,jsonify
from app import db
from .models import Post
from flask_restful import Resource, reqparse, Api

# bp=Blueprint('bp' ,__name__)

# @bp.route('/add' , methods=['POST'])

# def create_post():

#     post_data= request.get_json()
#     new_post =Post( title=post_data['title'] ,content=post_data['content']) 

#     db.session.add(new_post)
#     db.session.commit()
#     return 'Done' ,201


# @bp.route('/pos' , methods=['GET'])

# def pos_list():
#     post_list=Post.query.all()
    
#     pos=[]
#     for post in post_list:
#         pos.append({ 'title':post.title})
#     return jsonify({'pos' : pos})

class Posts_List(Resource):    
    
#Instantiating a parser object to hold data from message payload
    parser = reqparse.RequestParser()                      
    parser.add_argument('title', type=str, required=False, help='Title of post')    
    parser.add_argument('content', type=str, required=False, help='About the post')    
    
#Creating the get method
    def get(self, movie):        
        item = Post.find_by_id(movie)        
        if item:            
            return item.json()        
        return {'Message': 'Movie is not found'}        
    
#Creating the post method
    def post(self, movie):        
        if Post.find_by_id(movie):            
            return {' Message': 'Movie with the  title {} already exists'.format(movie)}        
        
        args = Posts_List.parser.parse_args()        
        item = Post(movie, args['title'], args['content'])        
        
        item.save_to()        
        return item.json()            
    
#Creating the put method
    def put(self, movie):        
        args = Posts_List.parser.parse_args()        
        item = Post.find_by_id(movie)        
        if item:            
            item.collection = args['title']            
            item.save_to()            
            return {'Post': item.json()}        
        item = Post(movie, args['title'], args['content'])        
        item.save_to()        
        return item.json()
        
#Creating the delete method
    def delete(self, movie):        
        item  = Post.find_by_id(movie)        
        if item:            
            item.delete_()            
            return {'Message': '{} has been deleted from records'.format(movie)}        
        return {'Message': '{} is already not on the list'.format(movie)}



#Creating a class to get all the movies from the database.
class All_Posts(Resource):        #Defining the get method
    def get(self):        
        return {'Movies': list(map(lambda x: x.json(), Post.query.all()))}    
