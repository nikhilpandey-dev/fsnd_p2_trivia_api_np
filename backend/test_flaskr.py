import os
from this import d
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category, db


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgresql://{}:{}@{}/{}".format("student", "student", "localhost:5432", self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    # Test for retrieving paginated questions
    def test_retrieve_questions(self):
        res = self.client().get("/questions")
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['questions'])
    
    def test_404_retrieve_questions_beyond_valida_page(self):
        res = self.client().get("/questions?page=1000")
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")
    
    # Test for retrieving categories
    def test_retrieve_categories(self):
        res = self.client().get("/categories")
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data["total_categories"])
        self.assertTrue(data["categories"])
    
    # Test for retrieving categories failure scenario
    # Based on this QA from the knowledge base: https://knowledge.udacity.com/questions/350483
    def test_failure_retrieve_categories(self):
        res = self.client().post("/categories")
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Method not allowed")
    
    # Test for retrieving questions by category
    def test_retrieve_questions_by_category(self):
        res = self.client().get("/categories/1/questions")
        data = json.loads(res.data)
        # Using db as SQLALchemy recommeds using db.sesssion.query(Model) instead of Model.query
        questions = db.session.query(Question).filter(Question.category == 1).all()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['total_questions'], len(questions))
        self.assertTrue(data['questions'])
    
    # Test for retrieving questions by category failure scenario
    def test_failure_retrieve_questions_by_category(self):
        res = self.client().get("/categories/1000/questions")
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "bad request")
    
    # Test for deleting Questions
    def test_delete_question(self):
        res = self.client().delete("/questions/27")
        question = db.session.query(Question).filter(Question.id == 27).one_or_none()
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["deleted"], 27)
        self.assertTrue(data["total_questions"])
    
    # Test for deleting Questions failure scenario
    def test_failure_delete_question(self):
        res = self.client().delete("/questions/1000")
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)


    # Test for creating new questions
    def test_create_new_question(self):
        res = self.client().post("/questions", json={"question": "What is the capital of France?", "answer": "Paris", "category": "3", "difficulty": "2"})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["created"])
        self.assertTrue(data["questions"])
        self.assertTrue(data["total_questions"])

    
    # Test for failure of create_questions
    def failure_create_new_question(self):
        res = self.client().post("/questions/5", json={"question": "Which country was the runner up of 2018 FIFA world cup?", "answer": "Croatia", "category": "5", "difficulty": "4"})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "bad request")



    


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()