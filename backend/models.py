import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

database_name = "trivia"
# setup database path and use student as the user and owner of the database
# Have reset categories id to 0 using the code UPDATE public.categories SET id = id - 1;

database_path = "postgresql://{}:{}@{}/{}".format(
    "student", "student", "localhost:5432", database_name
)


db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

'''
Question

'''
class Question(db.Model):  
  __tablename__ = 'questions'

  id = Column(Integer, primary_key=True)
  question = Column(String)
  answer = Column(String)
  category = Column(String)
  difficulty = Column(Integer)

  def __init__(self, question, answer, category, difficulty):
    self.question = question
    self.answer = answer
    self.category = category
    self.difficulty = difficulty

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'question': self.question,
      'answer': self.answer,
      'category': self.category,
      'difficulty': self.difficulty
    }

'''
Category

'''
class Category(db.Model):  
  __tablename__ = 'categories'

  id = Column(Integer, primary_key=True)
  type = Column(String)

  def __init__(self, type):
    self.type = type
  

  def format(self):
    return {
      'id': self.id,
      'type': self.type
    }

# class Category_Question_List(db.Model):
#   __tablename__ = 'category_question_list'

#   id = Column(Integer, primary_key=True)
#   category_id = Column(Integer)
#   question_id = Column(Integer)

#   def __init__(self, category_id, question_id):
#     self.category_id = category_id
#     self.question_id = question_id

#   def format(self):
#     return {
#       'id': self.id,
#       'category_id': self.category_id,
#       'question_id': self.question_id
#     }