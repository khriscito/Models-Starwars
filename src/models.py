import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class user(Base):
    __tablename__ = 'user'
    id= Column(Integer,primary_key=True)
    username= Column(String(20), nullable=False)
    email= Column(String(30), nullable=False)
    password= Column(String(20), nullable=False)
    profile = relationship('profile')

class profile(Base):
    __tablename__ = 'profile'
    id= Column(Integer,primary_key=True)
    name= Column(String(20), nullable=False)
    following=Column(String(50), nullable=False)
    followers=Column(String(50), nullable=False)
    profile_photo= Column(String(50), nullable=True)
    profile_description=Column(String(50), nullable=True)
    publications = Column(String(50), nullable=True)
    add_publication= Column(String(100), nullable=False)
    user=relationship(user)
    user_id= Column(Integer,ForeignKey('user.id'),nullable=False)
    followers= relationship('followers')
    posts = relationship('post')
    comment = relationship('comment')

class followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer,primary_key=True)
    user_from_id= Column(Integer,nullable=False)
    user_to_id= Column(Integer,nullable=False)
    user=relationship(user)
    user_id= Column(Integer,ForeignKey('user.id'), nullable=False)

class posts (Base):
    __tablename__='posts'
    id= Column(Integer,primary_key=True)
    post_id= Column(Integer,nullable=False)
    url = Column(String(50),nullable=False)
    user=relationship(user)
    user_id= Column(Integer,ForeignKey('user.id'), nullable=False)
    comment= relationship('comment')

class comment (Base):
    __tablename__= "comment"
    id= Column(Integer,primary_key=True)
    comment_id= Column(Integer,nullable=False)
    comment_text= Column(String(200),nullable=False)
    user=relationship(user)
    user_id= Column(Integer,ForeignKey('user.id'), nullable=False)
    posts = relationship('post')



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
