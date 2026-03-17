import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame({
    "Student":["A","B","C","D","E","F","G","H"],
    "Study_Hours":[2,3,4,1,2,3,5,2],
    "Math_score":[65,72,88,60,70,80,95,68]
})
print("student performance DataSet:")
print(df)
print("\nHeighest Math Score:")
print(df["Math_score"].max())
print("\nHeighest Student Hours vs Math score:")
print(pd.crosstab(df["Study_Hours"],df["Math_score"]))
plt.bar(df["Student"],df["Math_score"])
plt.xlabel("Math Score")
plt.ylabel("Student Hours vs Math Score")
plt.title("Student Performance Analysis")
plt.show()