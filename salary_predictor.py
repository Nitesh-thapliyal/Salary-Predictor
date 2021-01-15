import joblib
model = joblib.load('Salary.pk')

exp = input("Enter Experience fot Salary to predict: ")
predict = model.predict([[int(exp)]])

print(f"your salary is:{predict}")