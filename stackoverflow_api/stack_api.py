import flask
from flask import jsonify, request
from flask_restful import Resource, reqparse

app = flask.Flask(__name__)
app.config["DEBUG"] = True



# Create data for StackOverflow-lite using a list of dictionaries.
questions = [
    {'question_id': 1,
     'title': 'How to configure a typeError in python?',
     'category': 'Python',
     'file': 'errors.html',
     'details': 'I am trying to run a certain file but it is returning that a typeError',
     'user_id':1
     },

    {'question_id': 2,
     'title': 'How to create a responsive website from scratch',
     'category': 'Websites',
     'file': 'website.css',
     'details': 'I have been trying to create this website but it is not responsive on mobile gadgets',
     'user_id':1
     },
     
   {'question_id': 3,
     'title': 'How to test my api endpoints in heroku',
     'category': 'Tesing',
     'file': 'test.tests',
     'details': '1992',
     'user_id':1
     }
]

answers = [
    {
        'answer_id': 1,
        'question_id': 2,
        'name':"coder456",
        'email': "coder@gmail.com",
        'reply': "You can json instead of Python",
        'user_id':1
    },

    {
        'answer_id': 2,
        'question_id': 1,
        'name':"dGang00R",
        'email': "dgang@gmail.com",
        'reply': "Try using html5 and css3",
        'user_id': 2
    },

    {
        'answer_id': 3,
        'question_id': 1,
        'name':"gamer00R",
        'email': "GM@gmail.com",
        'reply': "How about aborting the program?",
        'user_id': 3
    }


]

users = [
    {
        'user_id': 1,
        'user_name': "coder456",
        'user_email':"coder@gmail.com",
        'user_password': "1234"
       
    },

    {
        'user_id': 2,
        'user_name': "dGang",
        'user_email':"gang@gmail.com",
        'user_password': "5555"
    },

    {
        'user_id': 3,
        'user_name': "gamer00R",
        'user_email':"GM@gmail.com",
        'user_password': "5545"
    }


]

# A route to return index page of this platform.
@app.route('/', methods=['GET'])
def home():
    return "<h1>StackOverflow-lite</h1>\
    <p>This platform is to help all interested users to ask questions and provide feedback.</p>"

# A route to return all of the existing users on this platform.
@app.route('/api/v1/users/all', methods=['GET'])
def api_get_all_users():
    return jsonify(users)

# A route to return a specific user on this platform.
@app.route('/api/v1/users/userId', methods=['GET'])
def api_get_user_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'user_id' in request.args:
        id = int(request.args['user_id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    user_results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for user in users:
        if user['user_id'] == id:
            user_results.append(user)

    # Use the jsonify function to convert our list 
    # to the JSON format.
    return jsonify(user_results)

# A route to register a new user on the platform.
@app.route('/api/v1/auth/signup', methods=['POST'])
def api_add_user():
    try:
        parser = reqparse.RequestParser()
        parser.add_argument("user_id")
        parser.add_argument("user_name")
        parser.add_argument("user_email")
        parser.add_argument("user_password")
        
        args = parser.parse_args()
        for user in users:
            if(args["user_name"] == user["user_name"]):
                return "User with username {} already exists".format(args["user_name"]), 400

        user = {
            "user_id":args["user_id"], 
            "user_name": args["user_name"], 
            "user_email" :args["user_email"], 
            "user_password":args["user_password"]
            
        }
        users.append(user)
        return jsonify(user)
    except:
        return "something went wrong"

# A route to login a user.
@app.route('/api/v1/auth/login', methods=['GET'])
def api_user_login():
   
    if 'user_email' in request.args:
        email = str(request.args['user_email'])
    else:
        return "Error: No email field provided. Please enter your email."

    user_profiles = []

    
    for user in users:
        if user['user_email'] == email:
            user_profiles.append(user)

      
    return jsonify(user_profiles)
        

# A route to return all questions on this platform.
@app.route('/api/v1/questions/all', methods=['GET'])
def api_get_all_questions():
    return jsonify(questions)

# A route to return a specific question.
@app.route('/api/v1/questions/questionId', methods=['GET'])
def api_get_question_id():
    
    if 'question_id' in request.args:
        id = int(request.args['question_id'])
    else:
        return "Error: No id field provided. Please specify an id."

    question_results = []

    for question in questions:
        if question['question_id'] == id:
            question_results.append(question)
            
    return jsonify(question_results) 

            
#A route to post a new question on the platform
@app.route('/api/v1/questions/question/add', methods=['POST'])
def api_add_question():
    try:
        parser = reqparse.RequestParser()
        parser.add_argument("question_id")
        parser.add_argument("title")
        parser.add_argument("category")
        parser.add_argument("file")
        parser.add_argument("details")
        parser.add_argument("user_id")
        args = parser.parse_args()
        for question in questions:
            if(args["title"] == question["title"]):
                return "question with title {} already posted".format(args["title"]), 400

        question = {
            "question_id":args["question_id"], 
            "title": args["title"], 
            "category" :args["category"], 
            "file":args["file"], 
            "details" :args["details"],
            "user_id" :args["user_id"]
        }
        questions.append(question)
        return jsonify("Successfully posted your question!", question)
    except:
        return "something went wrong"

#route to add an answer to a specific question
@app.route('/api/v1/questions/questionId/answers/post', methods=['POST'])
def api_add_answer():
    try:
        parser = reqparse.RequestParser()
        parser.add_argument("answer_id")
        parser.add_argument("question_id")
        parser.add_argument("name")
        parser.add_argument("email")
        parser.add_argument("reply")
        parser.add_argument("user_id")
                
        args = parser.parse_args()
        for answer in answers:
            if(args["reply"] == answer["reply"]):
                return "This kind of answer {} already posted".format(args["reply"]), 400

        answer = {
            "answer_id":args["answer_id"],
            "question_id":args["question_id"], 
            "name": args["name"], 
            "email" :args["email"], 
            "reply":args["reply"], 
            "user_id":args["user_id"]
                    
        }
        answers.append(answer)
        return jsonify("You have successfully posted your answer!", answer)
    except:
        return "something went wrong"


#route to get answers to a specific question
@app.route('/api/v1/answers/questionId', methods=['GET'])
def api_question_answer_id():
   
    if 'question_id' in request.args:
        id = int(request.args['question_id'])
    else:
        return "Error: No id field provided. Please specify an id."

    results = []

    for answer in answers:
        if answer['question_id'] == id:
            results.append(answer)

    return jsonify(results)

if __name__ == '__main__':
    app.run()
