import pickle
from sklearn.tree import DecisionTreeClassifier

# Sample student data:
# [study hours per day, attendance percentage, internal marks]
X = [
    [1, 40, 20],
    [2, 50, 25],
    [3, 60, 35],
    [4, 70, 45],
    [5, 80, 60],
    [6, 85, 70],
    [7, 90, 80],
    [8, 95, 90],
    [2, 30, 15],
    [3, 45, 25],
    [5, 65, 50],
    [1, 80, 20],
]

# 0 = Fail, 1 = Pass
y = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0]

model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

with open("student_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Student Result model trained successfully!")
print("Model saved as student_model.pkl")