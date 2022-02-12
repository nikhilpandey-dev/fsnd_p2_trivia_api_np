- [Full Stack API Trivia App](#full-stack-api-trivia-app)
  - [Project Title : Trivia App](#project-title--trivia-app)
    - [Project Description](#project-description)
    - [Project Requirements](#project-requirements)
    - [Key Asks](#key-asks)
    - [Code Style](#code-style)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Dependencies](#dependencies)
    - [Installing Dependencies](#installing-dependencies)
      - [Front End Dependencies](#front-end-dependencies)
      - [Backend Dependencies](#backend-dependencies)
    - [Database Setup](#database-setup)
    - [Running the server](#running-the-server)
  - [API Reference](#api-reference)
    - [Errors](#errors)
    - [API Endpoints](#api-endpoints)
      - [`GET /categories`](#get-categories)
      - [`GET /questions`](#get-questions)
      - [`DELETE /questions/<int:question_id>`](#delete-questionsintquestion_id)
      - [`POST /questions`](#post-questions)
        - [Adding New Question](#adding-new-question)
        - [Searching for a question](#searching-for-a-question)
      - [`GET /categories/<int:category_id>/questions`](#get-categoriesintcategory_idquestions)
      - [`POST /quizzes`](#post-quizzes)
  - [Deployment](#deployment)
  - [Authors](#authors)
  - [Acknowledgements](#acknowledgements)
***
# Full Stack API Trivia App
## Project Title : Trivia App
### Project Description
- This is a web app, which tries to check the General Knowledge of the participants across six major categories, given below:
    1. Science
    2. Art
    3. Geography
    4. History
    5. Entertainment
    6. Sports

### Project Requirements
- To help in developing the API for the underlying web app, so that it gets connected to a database, and can be used by the front end for various purposes such as:
  - Showing all the questions
  - Segregating questions by categories
  - Adding new questions
  - Deleting questions
  - Showing Questions by Categories
  - Searching for Questions
### Key Asks
- At the end of the API development , the web application should be able to:
  1. Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer.
  2. Delete questions.
  3. Add questions and require that they include question and answer text.
  4. Play the quiz game, randomizing either all questions or within a specific category.

### Code Style
Though this is a simple project, I have used a lot of code style conventions, espcially the PEP 8 guidelines and [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).
## Getting Started
### Prerequisites
- Intermediate level understanding of Python
- Understanding of PostgreSQL database
- Understanding of RESTful APIs
- Understanding of HTML, CSS, and JavaScript
- Understanding of Flask
- Understanding of SQLAlchemy

### Dependencies
The major dependencies of this project are:
- Python version [3.10.2](https://www.python.org/downloads/release/python-3102/) 
- [FLask 2.x.x](https://flask.palletsprojects.com/en/2.0.x/) - a lightweight backend microservices framework. Flask is required to handle requests and responses.
- [PostgreSQL](https://www.postgresql.org/) version 13.5 as the database.
- [SQLAlchemy](https://www.sqlalchemy.org/) version 1.4.31, which is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
- Python virtual environment for managing package installations, a great primer for these can be found in this [short realpython's course](https://realpython.com/courses/working-python-virtual-environments/).
- [FLask-CORS](https://flask-cors.readthedocs.io/en/latest/) - a Flask extension that allows cross-origin resource sharing, thus , making cross-origin AJAX possible.

### Installing Dependencies
#### Front End Dependencies
- Since this project's main focus is on APIs, the frontend has already been constructed and we can use the frontend dependencies by going to the `frontend` directory and running the command
```bash
npm install
```
#### Backend Dependencies
- To install the backend dependencies, we need to go to the `backend` directory and run the command
```bash
pip install -r requirements.txt
```
### Database Setup
We can install the database by first going to the terminal `psql` shell and creating a database called `trivia`. Then we can run the following comand from the `backend` directory:
```bash
psql trivia < trivia.sql
```

### Running the server
- To run the server, we need to go to the `backend` directory and run the command
```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
export FLASK_DEBUG=true
flask run 
```
The app runs on `localhost:5000` and the `FLASK_DEBUG` environment variable is set to `true`.
## API Reference

### Errors
- The API returns the following error messages:
  - `400` - Bad Request
  - `404` - Not Found
  - `405` - Method Not Allowed
  - `422` - Unapproachable

- Errors are returned in the json format, a sample of which is given below:
```json
{
    "success": false,
    "error": 404,
    "message": "Not Found"
}
```
### API Endpoints
#### `GET /categories`
This endpoint returns a list of all the categories in the dictionary format, where category id is the key and category type is the value.

Example request format:
```bash
GET /categories
```
Example json response format:
```json
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "success": true
}
```
#### `GET /questions`
This endpoint returns questions stored in the database in the paginated format, where a page size is of 10 questions. this has been done so as to avoid the large number of questions that are stored in the database and to make the API more efficient and frontend more responsive.


Example request format:
```bash
GET /questions
```
Example json response format:
```json
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "questions": [
    {
      "category": 4, 
      "category_type": "History", 
      "difficulty": 2, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }, 
    {
      "category": 4, 
      "category_type": "History", 
      "difficulty": 1, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "category": 5, 
      "category_type": "Entertainment", 
      "difficulty": 4, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "category": 5, 
      "category_type": "Entertainment", 
      "difficulty": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "category": 5, 
      "category_type": "Entertainment", 
      "difficulty": 3, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "category": 6, 
      "category_type": "Sports", 
      "difficulty": 3, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "category": 6, 
      "category_type": "Sports", 
      "difficulty": 4, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "category": 4, 
      "category_type": "History", 
      "difficulty": 2, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "category": 3, 
      "category_type": "Geography", 
      "difficulty": 2, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "category": 3, 
      "category_type": "Geography", 
      "difficulty": 3, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ], 
  "success": true, 
  "total_questions": 21
}

```
#### `DELETE /questions/<int:question_id>`
This endpoint deletes a question from the database, which was specified by its id in the url. It returns the success message in the json format and then repaginates the questions.

Example request format:
```bash
DELETE /questions/<int:question_id>
```
Example json response format:
```json
{
  "deleted": 23, 
  "questions": [
    {
      "answer": "Maya Angelou", 
      "category": 4, 
      "difficulty": 2, 
      "id": 5, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }, 
    {
      "answer": "Muhammad Ali", 
      "category": 4, 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "answer": "Apollo 13", 
      "category": 5, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "Tom Cruise", 
      "category": 5, 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": 5, 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "answer": "Brazil", 
      "category": 6, 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": 6, 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": 4, 
      "difficulty": 2, 
      "id": 12, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": 3, 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": 3, 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ], 
  "success": true, 
  "total_questions": 20
}

```
#### `POST /questions`
This endpoint does two things
1. Posts a new question if there is no `searchTerm` in the request body .
2. Searchs for a question if there is  `searchTerm` in the request body.

##### Adding New Question
This endpoint adds a question to the database. It returns the success message in the json format and then repaginates the questions.

Example request format:
```bash
POST /questions
```
Example json resquest body in json format:
```json
{
    "category": 1,
    "question": "What is the Newton's third law",
    "answer": "To every action, there is an equal and opposite reaction",
    "difficulty": 3
}
```

Example json response format:
```json
{
    "created": 26,
    "questions": [
        {
            "answer": "Maya Angelou",
            "category": 4,
            "difficulty": 2,
            "id": 5,
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        },
        {
            "answer": "Muhammad Ali",
            "category": 4,
            "difficulty": 1,
            "id": 9,
            "question": "What boxer's original name is Cassius Clay?"
        },
        {
            "answer": "Apollo 13",
            "category": 5,
            "difficulty": 4,
            "id": 2,
            "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        },
        {
            "answer": "Tom Cruise",
            "category": 5,
            "difficulty": 4,
            "id": 4,
            "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        },
        {
            "answer": "Edward Scissorhands",
            "category": 5,
            "difficulty": 3,
            "id": 6,
            "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        },
        {
            "answer": "Brazil",
            "category": 6,
            "difficulty": 3,
            "id": 10,
            "question": "Which is the only team to play in every soccer World Cup tournament?"
        },
        {
            "answer": "Uruguay",
            "category": 6,
            "difficulty": 4,
            "id": 11,
            "question": "Which country won the first ever soccer World Cup in 1930?"
        },
        {
            "answer": "George Washington Carver",
            "category": 4,
            "difficulty": 2,
            "id": 12,
            "question": "Who invented Peanut Butter?"
        },
        {
            "answer": "Lake Victoria",
            "category": 3,
            "difficulty": 2,
            "id": 13,
            "question": "What is the largest lake in Africa?"
        },
        {
            "answer": "The Palace of Versailles",
            "category": 3,
            "difficulty": 3,
            "id": 14,
            "question": "In which royal palace would you find the Hall of Mirrors?"
        }
    ],
    "success": true,
    "total_questions": 21
}
```

##### Searching for a question
Example json resquest body in json format:
```json
{
    "searchTerm": "India"
}
```

Example json response format:
```json
{
    "questions": [
        {
            "answer": "Agra",
            "category": 3,
            "difficulty": 2,
            "id": 15,
            "question": "The Taj Mahal is located in which Indian city?"
        }
    ],
    "success": true,
    "total_questions": 1
}
```

#### `GET /categories/<int:category_id>/questions`
This endpoint returns a list of questions based on the category id.It returns an array of questions under that particular category id and totla number of questions in that category.
Example request format:
```bash
GET /categories/1/questions
```

Example json response format:
```json
{
    "current_category": 1,
    "questions": [
        {
            "answer": "The Liver",
            "category": 1,
            "difficulty": 4,
            "id": 20,
            "question": "What is the heaviest organ in the human body?"
        },
        {
            "answer": "Alexander Fleming",
            "category": 1,
            "difficulty": 3,
            "id": 21,
            "question": "Who discovered penicillin?"
        },
        {
            "answer": "Blood",
            "category": 1,
            "difficulty": 4,
            "id": 22,
            "question": "Hematology is a branch of medicine involving the study of what?"
        },
        {
            "answer": "To every action, there is an equal and opposite reaction",
            "category": 1,
            "difficulty": 3,
            "id": 26,
            "question": "What is the Newton's third law"
        }
    ],
    "success": true,
    "total_questions": 4
}
```

#### `POST /quizzes`
This endpoint allows user to play a quix game, either by a category or by all.
## Deployment
The application can be either hosted on the remote server and/or cloud or can be hosted locally. If no domain is configured then the app runs in the local environment.
- The base URRs are:
  - for backend `http://127.0.0.1:5000/`
  - for frontend `http://127.0.0.1:3000/`

## Authors
**Nikhil Pandey** is the main author of this project. he has contributed to the project by writing the backend code in the following two code files
 1. `backend/flasr/__init__.py`
 2. `backend/test_flaskr.py`
Apart from that he has written the documentation which is given in the `README.md` file, which you are reading now.
## Acknowledgements
This project is a part of the Udacity Full Stack Web Developer Nanodegree program. So obviously it has used a lots of resources from Udacity, espcailly the lecture notes and exercise codes. Apart from the these two, the Q&A forum for this [trivia project](https://knowledge.udacity.com/?nanodegree=nd0044&page=1&project=630&rubric=2634&sort=SCORE) is also a source of information as well as codes for this project.
