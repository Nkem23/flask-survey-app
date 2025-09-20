from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
import os

app = Flask(__name__)

# Connecting to the MongoDB
mongo_uri = os.getenv("MONGO_URI")  # gets MongoDB URI from environment variable
client = MongoClient(mongo_uri)
db = client["surveyDB"]
collection = db["users"]

# Define the homepage
@app.route('/')
def home():
    return render_template('form.html')

# Define another webpage, when client submits a form
@app.route('/submit', methods=['POST'])
def submit():

    age = request.form['age']
    gender = request.form['gender']
    income = request.form['income']

# define expenses item and collect client's input
    expenses = {
        "utilities": request.form.get('utilities', 0),
        "entertainment": request.form.get('entertainment', 0),
        "school_fees": request.form.get('school_fees', 0),
        "shopping": request.form.get('shopping', 0),
        "healthcare": request.form.get('healthcare', 0),
    }


# save the input to MongoDB
    collection.insert_one({
        "age": age,
        "gender": gender,
        "income": income,
        "expenses": expenses
    })

    return redirect('/')

# run the app

if __name__ == '__main__':
     app.run(host="0.0.0.0", port=5000)

# expose for Elastic Beanstalk
application = app

