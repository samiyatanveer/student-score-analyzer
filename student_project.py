import numpy as np 
import pandas as pd
import matplotlib.pyplot  as plt

#saving the csv

np.random.seed(42)
n = 200
df = pd.DataFrame({
    "Name": [f"Student_{i}" for i in range(n)],
    "Subject": np.random.choice(["Math", "Physics", "English", "CS"], n),
    "Marks": np.random.randint(30, 100, n).astype(float),
    "City": np.random.choice(["Lahore", "Karachi", "Islamabad", "Peshawar"], n),
    "Attendance": np.random.randint(50, 100, n).astype(float)
})
df.loc[np.random.choice(n, 20, replace=False), "Marks"] = np.nan
df.loc[np.random.choice(n, 10, replace=False), "Attendance"] = np.nan
df.to_csv("students.csv", index=False)

# actual code


df=pd.read_csv("students.csv")
print(df.info())
print(df.describe())

print("counting the null values")
print(df.isna().sum())
df["Marks"]=df["Marks"].fillna(df["Marks"].mean())

df=df.dropna(subset="Attendance")

df["Marks"]=df["Marks"].astype(float)

df=df.drop_duplicates()

passed=df[df["Marks"]>50]
print(passed)

print(df[["Marks","Name"]])

def grade(m):
    if m>80:
        return "A"
    elif m>70:
        return "B"
    elif m>60:
        return "C"
    else:
        return "D"   
df["Grade"]=df["Marks"].apply(grade)
 

average = df.groupby("Subject")["Marks"].mean()
print(average)
city= df.groupby("City")["Name"].count()
print(city)
top=df.nlargest(5,"Marks")
print(top)
gradecount=df["Grade"].value_counts()
print(gradecount)
dfsort=df.sort_values(by="Marks",ascending =False)
print(dfsort.head())




marks=df["Marks"].values
print("std",np.std(marks))
print("minimum  ",np.min(marks))
print("maeannm  ",np.mean(marks))
print("maximumm   ", np.max(marks))

result=np.where(marks>=50, "pss","fail")
p25= np.percentile(marks,25)
p75=np.percentile(marks,75)

print("percentile 25", p25)
print("percentile 75",p75)

clipped=np.clip(marks,20,80)

if len(marks) == 200:
    matrix= marks.reshape(18,20)

    print("matrix row means")
    print(matrix.mean(axis=1))

fake_attendance= np.random.randint(50,101,size=50)
print(fake_attendance)

high=marks[marks>50]
print(high)

fees= pd.DataFrame({
    "Name":df["Name"].sample(min(20,len(df))),
    "feepaid":np.random.randint(1000,5000,min(20,len(df)))
})
merged=pd.merge(df,fees,on="Name", how="left")
print(merged.head())

pivot= pd.pivot_table(
    df,
    values="Marks",
    index="City",
    columns="Subject",
    aggfunc="mean",
)
print("pivot table\n", pivot)

correlation=df["Marks"].corr(df["Attendance"])
print(correlation)

plt.figure(figsize=(6,4))
plt.hist(df["Marks"],bins =60) 
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("frequency")
plt.show()

average.plot(kind= "bar")
plt.title("Average Marks By Subject")
plt.xlabel("Subject")
plt.ylabel("Average Marks")
plt.show()


print(f"Total Students: {len(df)}")
print(f"Average Marks: {df['Marks'].mean():.2f}")
print(f"Highest Marks: {df['Marks'].max():.2f}")
print(f"Lowest Marks: {df['Marks'].min():.2f}")

print(f"Marks-Attendance Correlation: {correlation:.2f}")

