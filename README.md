# Project 2: Student Attendance Prediction

## 1. Introduction
This project uses machine learning to predict whether a student is likely to have good attendance based on simple academic information.

The dataset is **synthetic** and was created for learning purposes. It does not contain real student information.

## 2. Problem Statement
Poor attendance can make it harder for students to keep up with their studies. A simple prediction model could help identify students who may need additional support.

## 3. Aim
To build a simple machine-learning model that predicts whether a student is likely to have good attendance.

## 4. Objectives
- Load and inspect the data.
- Check for missing values.
- Select useful input variables.
- Split the data into training and testing sets.
- Train a Logistic Regression model.
- Measure model accuracy.
- Test the model with a new example.

## 5. Tools Used
- Python
- Pandas
- Scikit-learn

## 6. Input Variables
The model uses:
- Previous average mark
- Study hours per week
- Assignment score

The target variable is `Good_Attendance`.

## 7. Machine Learning Method
I used **Logistic Regression** because this is a simple classification problem. The model predicts one of two outcomes:
- 1 = Good attendance
- 0 = Lower attendance

## 8. Steps Followed
1. Loaded the dataset.
2. Checked the data.
3. Selected the features and target.
4. Split the data into 80% training and 20% testing data.
5. Trained the Logistic Regression model.
6. Made predictions.
7. Calculated accuracy.
8. Printed a confusion matrix and classification report.
9. Tested a new student example.

## 9. Important Note
The dataset is synthetic. Therefore, the model should not be used to make real decisions about students. A real application would require an approved, sufficiently large and representative dataset.

## 10. Conclusion
This project helped me understand the basic machine-learning workflow: preparing data, splitting data, training a model, making predictions and evaluating results.

## 11. Future Improvements
A future version could compare several models, use more relevant student information, tune the model and test it on an approved real-world dataset.
