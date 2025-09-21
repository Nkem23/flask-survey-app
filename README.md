## Project Overview
This Flask web application collects user data, including personal details and expense categories, stores the data in MongoDB,
processes it using a Python class named `User`, and exports the results to CSV for analysis in Jupyter Notebook. 
Visualizations of the collected data are also provided. The app is hosted on AWS.

## Features
- Collects user data through a web form built with **Flask**.
- Stores survey responses in **MongoDB**.
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

The Flask app is hosted on AWS Elastic Beanstalk or EC2.  [http://127.0.0.1:5000/]

Steps:
           
  1. Package your application:
  2. Deploy to AWS Elastic Beanstalk via AWS CLI or Console.
  3. Access your live app using the assigned AWS URL.

 
 ## File Structure
flask-survey-app/
│
├── app.py                                 # Main Flask app
├── Flask Healthcare Application .py       # User class for data processing
├── requirements.txt                       # Python dependencies
├── templates/                             # HTML templates
├── static/                                # CSS, JS, images
├── survey_data/                           # Exported CSV files
├── Flask Healthcare Application .pptx/    # Visulaization and insights of data
└── README.md                              # Project Overview

## Submission Checklist

✅ All assignment deliverables are included:

 Flask  web application for survey data collection

 MongoDB integration for storing user data

 Python User class for data processing

 CSV export of processed data

 Jupyter Notebook for data analysis

 Visualizations generated and exported as images

 Application hosted on AWS

 README file with instructions and project overview

 GitHub repository ready for submission

This checklist ensures that every part of the assignment scope is fully addressed.


Notes

Ensure MongoDB is running before submitting data.

CSV export is required to perform analysis in Jupyter Notebook.

Charts should be saved and exported as image files for submission.
