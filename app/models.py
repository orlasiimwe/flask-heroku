from app import db
from datetime import datetime
from flask import json

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, unique=True)
    content = db.Column(db.String(120), index=True, unique=True)
    
    # def __repr__(self):
    #     return '<User {}>'.format(self.title)

    def __init__(self,title, content):               
        self.title = title        
        self.content = content       
     
    #Method to show data as dictionary object
    def json(self):        
        return {'id':self.id, 'Title': self.title, 'Content': self.content}        
 
    #Method to find the query movie is existing or not
    @classmethod    
    def find_by_id(cls, id):        
        return cls.query.filter_by(id=id).first()#Method to save data to database

    def save_to(self):        
        db.session.add(self)        
        db.session.commit()#Method to delete data from database
        
    def delete_(self):        
        db.session.delete(self)        
        db.session.commit()
