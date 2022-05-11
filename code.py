#IMporting flask
from flask import Flask,jsonify, request

#Creating a flask object
app = Flask(__name__)

#Creates a list
contacts = [
    {
        'id': 1,
        'Name': 'Raju',
        'Contact': '9987644456', 
        'done': False
    },
    {
        'id': 2,
        'Name': 'Rahul',
        'Contact': '9876543222', 
        'done': False
    },
]

#Creates portal route for app
@app.route("/")

#Initial screen
def hello():
    return "Hello"

#Creates route to add data.
#Data can be added through postman
@app.route("/add-data", methods=["POST"])

#Function to add contacts
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Provide data"
        },400)

    contact = {
        'id': task[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }
    contacts.append(contact)
    return jsonify({
        "status":"success",
        "message": "Contact added"
    })
    
#Creates route to get data
@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : contacts
    }) 

#Runs the code.
if (__name__ == "__main__"):
    app.run()