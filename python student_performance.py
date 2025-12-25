Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import pandas as pd
>>> data = {
...     "StudyHours": [1, 2, 3, 4, 5, 6, 7, 8],
...     "Attendance": [60, 65, 70, 75, 80, 85, 90, 95],
...     "Marks": [40, 45, 55, 60, 65, 75, 85, 95]
...     }
>>> df = pd.DataFrame(data)
>>> print(df)
   StudyHours  Attendance  Marks
0           1          60     40
1           2          65     45
2           3          70     55
3           4          75     60
4           5          80     65
5           6          85     75
6           7          90     85
7           8          95     95
>>> X = df[["StudyHours", "Attendance"]]
>>> y = df["Marks"]
>>> from sklearn.model_selection import train_test_split
>>> from sklearn.linear_model import LinearRegression
>>> X_train, X_test, y_train, y_test = train_test_split(
...     X, y, test_size=0.25, random_state=42
...     )
>>> model = LinearRegression()
>>> model.fit(X_train, y_train)
LinearRegression()
>>> from sklearn.metrics import r2_score
>>> y_pred = model.predict(X_test)
>>> print("R2 Score:", r2_score(y_test, y_pred))
R2 Score: 0.9888888888888887
>>> new_student = pd.DataFrame([[6, 88]], columns=["StudyHours", "Attendance"])
>>> predicted_marks = model.predict(new_student)
>>> print("Predicted Marks:", predicted_marks[0])
Predicted Marks: 81.47115384615388
