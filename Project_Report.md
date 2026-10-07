# PROJECT REPORT: STUDENT ATTENDANCE PREDICTION

## 1. Introduction
I chose this project because attendance is an important part of student learning. I wanted to learn how machine learning can be used to make a simple prediction from academic data.

The dataset is synthetic and was created for learning purposes. It does not contain real student information.

## 2. Problem Statement
Universities may have large amounts of student information, but it can be difficult to identify students who may have attendance problems early. A simple predictive model can demonstrate how data could be used for this type of task.

## 3. Aim
To develop a simple machine-learning model for predicting whether a student is likely to have good attendance.

## 4. Objectives
- Prepare the student dataset.
- Select relevant input variables.
- Train a Logistic Regression model.
- Test the model using unseen data.
- Evaluate its performance.
- Explain the limitations of the model.

## 5. Tools
Python, Pandas and Scikit-learn.

## 6. Method
The data was divided into input variables and a target variable. The target was `Good_Attendance`. The data was split into 80% training data and 20% testing data. Logistic Regression was then trained using the training data. The model was evaluated using accuracy, a confusion matrix and a classification report.

## 7. Results
When the program is run, it displays the model accuracy and other evaluation measures. These results should be interpreted as results from a synthetic learning dataset rather than evidence about real students.

## 8. Conclusion
The project helped me understand the basic steps involved in building a classification model. I learned how to prepare data, train a model, make predictions and evaluate the results.

## 9. Limitations
The dataset is synthetic and small. The selected variables do not represent all factors that may influence attendance. The model therefore should not be used for real student decisions.

## 10. Future Work
Future work could involve an approved real dataset, more features, comparison of different algorithms and better evaluation using cross-validation.
