# Project 2: Student Attendance Prediction
# A simple machine-learning project using Logistic Regression.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 1. Load the dataset
data = pd.read_csv("student_attendance.csv")

# 2. View the data
print("First five rows:")
print(data.head())

# 3. Check for missing values
print("\nMissing values:")
print(data.isnull().sum())

# 4. Select the input variables and target
features = [
    "Previous_Average",
    "Study_Hours_Per_Week",
    "Assignment_Score"
]

X = data[features]
y = data["Good_Attendance"]

# 5. Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

# 6. Create and train the model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 7. Make predictions
predictions = model.predict(X_test)

# 8. Evaluate the model
accuracy = accuracy_score(y_test, predictions)
print("\nModel accuracy:", round(accuracy * 100, 2), "%")

print("\nConfusion matrix:")
print(confusion_matrix(y_test, predictions))

print("\nClassification report:")
print(classification_report(y_test, predictions))

# 9. Try a simple prediction for a new student
new_student = pd.DataFrame({
    "Previous_Average": [70],
    "Study_Hours_Per_Week": [10],
    "Assignment_Score": [75]
})

prediction = model.predict(new_student)[0]

if prediction == 1:
    print("\nPrediction for the new student: Good attendance")
else:
    print("\nPrediction for the new student: Lower attendance")
