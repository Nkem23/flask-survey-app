## Project Overview
This Flask web application collects user data, including personal details and expense categories, stores the data in MongoDB,
processes it using a Python class named `User`, and exports the results to CSV for analysis in Jupyter Notebook. 
Visualizations of the collected data are also provided. The app is hosted on AWS.

## Features
- Collects user data through a web form built with **Flask**.
- Stores survey responses in **MongoDB Atlas**.
- Processes data with a Python class `User`.
- Exports processed data to a **CSV file**.
- Supports **data analysis and visualization** in Jupyter Notebook.
- Hosted on **AWS EC2** for live access.


## Technologies Used

- **Python 3.11+**

- **Flask** – Web framework

- **MongoDB** – Database for storing survey responses

- **pymongo** – Python library for MongoDB integration

- **pandas** – Data processing and CSV export

- **matplotlib & seaborn** – Data visualization
  
- **Jupyter Notebook** – Data analysis environment

- **AWS** – Hosting the web application

## Installation & Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/Nkem23/flask-survey-app.git

2. Navigate to the project directory:

       cd flask-survey-app

3. Create a virtual environment

       python -m venv venv
       venv\Scripts\activate      # Windows

4. Install required packages:

       pip install -r requirements.txt

5. MongoDB Setup.

       Make sure MongoDB is running and accessible.
       Default connection URI: mongodb://localhost:27017/
       Database name: survey_db
       Collection name: users

If using MongoDB Atlas (cloud):

      client = MongoClient("mongodb+srv://<username>:<password>@cluster0.mongodb.net/survey_db?retryWrites=true&w=majority")
6. Run the Flask app:

       python app.py

## Data Processing

The User class in models.py performs the following:

    Receives survey data from MongoDB.

    Cleans and validates data.

    Converts expense categories to numeric format.

    Calculates summaries like total expenses and category-wise spending.

    Exports processed data to data/users_data.csv.

  ## AWS Hosting

The Flask app is hosted on AWS EC2.  [http://127.0.0.1:5000/]

Steps:
           
  1. Package your application:
  2. Deploy to AWS EC2.
  3. Access your live app using the assigned AWS URL.

 
 ## File Structure

├── app.py                                 # Main Flask app

├── Flask Healthcare Application .py       # User class for data processing

├── requirements.txt                       # Python dependencies

├── templates                              # HTML templates

├── static/                                 # CSS, JS, images

├── survey_data.csv                           # Exported CSV files

├── Flask Healthcare Application .pptx    # Visulaization and insights of data

└── README.md                              # Project Overview

## Submission Checklist

 a. Flask  web application for survey data collection

 b. MongoDB integration for storing user data

 c. Python User class for data processing

 d. CSV export of processed data

 e. Jupyter Notebook for data analysis

 f. Visualizations generated and exported as images

 g. Application hosted on AWS

 h README file with instructions and project overview

This checklist ensures that every part of the assignment scope is fully addressed.


## Notes

1. Ensure MongoDB is running before submitting data.

2. CSV export is required to perform analysis in Jupyter Notebook.

3. Charts should be saved and exported as image files for submission.
