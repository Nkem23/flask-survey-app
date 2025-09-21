# Step 1: Connect & Collect Data from MongoDB
from pymongo import MongoClient
import pandas as pd

client = MongoClient("mongodb://localhost:27017/")
db = client["surveyDB"]
collection = db["users"]

# collect the user survey records from MongoDB and store them in a Python list, "data".
data = list(collection.find())

# convert the records in the variable data to CSV, by creating a class
import csv

class User:
    def __init__(self, age, gender, income, expenses):
        self.age = age
        self.gender = gender
        self.income = income
        self.expenses = expenses

    def to_dict(self):
        return {
            "Age": int(self.age),
            "Gender": self.gender,
            "Income": int(self.income),
            **{k:int(v) for k,v in self.expenses.items()}
        }

# write CSV
with open("survey_data.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["Age","Gender","Income","utilities","entertainment","school_fees","shopping","healthcare"])
    writer.writeheader()
    for record in data:
        user = User(record["age"], record["gender"], record["income"], record["expenses"])
        writer.writerow(user.to_dict())

# Step 3: Load CSV into Pandas for data manipulation
df = pd.read_csv("survey_data.csv")

df.head()
df.info()

# Step 4: Visualization  of the data 
import matplotlib.pyplot as plt

# Visualization A: Ages with Highest Income
age_avg_income = df.groupby("Age")["Income"].mean().sort_values(ascending=False)
top10_age_avg = age_avg_income.head(10)

plt.figure(figsize=(10,6))
top10_age_avg.plot(kind="bar")
plt.title("Top 10 Ages by Average Income")
plt.xlabel("Age")
plt.ylabel("Average Income")
plt.savefig("top10_age_avg_income.png")

plt.show()


# Visualization B: Ages with Lowest Income
bottom10_age_avg = age_avg_income.tail(10)

plt.figure(figsize=(10,6))
bottom10_age_avg.plot(kind="bar")
plt.title("Bottom 10 Ages by Average Income")
plt.xlabel("Age")
plt.ylabel("Average Income")
plt.savefig("bottom10_age_avg_income.png")

plt.show()


# Visualization C: Gender distribution across spending categories
# make a list of the expenses columns ( utilities, entertainment, shopping, school fees, healthcare)
expense_cols = ["utilities", "entertainment", "school_fees", "shopping", "healthcare"]

spending_by_gender = df.groupby("Gender")[expense_cols].sum()

# Transpose so categories are on x-axis and genders are bars
spending_by_gender_T = spending_by_gender.T

spending_by_gender_T.plot(kind="bar")  
plt.title("Gender Distribution Across Spending Categories (Total spending)")
plt.xlabel("Spending Category")
plt.ylabel("Total Spending")
plt.legend(title="Gender")
plt.savefig("gender_spending_by_category.png")

plt.show()
