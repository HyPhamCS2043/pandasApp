#Author: Hy Pham

import pandas as pd;

StudentGPA = pd.DataFrame(
    {
        "Student First Name": [
            "Austin",
            "Bernado",
            "Cecilia",
        ],
        "Student Last Name": [
            "Avery",
            "Santos",
            "Jones"
        ],
        "Degree 1": [""
        "Computer Science",
        "Business",
        "Psychology",],
        "Degree 2": [
            "Mathematics",
            pd.NA, #pd.NA is used to represent missing values in pandas, it is a special value that indicates the absence of data.
            "Computer Science"
        ],
        "Expected Date of Graduation": [
            # pd.Timestamp is used to represent dates in pandas, it allows for easy manipulation and comparison of dates.
            pd.Timestamp("2026-05-05"), 
            pd.Timestamp("202-12-20"),
            pd.Timestamp("2027-05-05"),
        ],
        "Current GPA": [
            3.8,
            4.1,
            3.9,
        ],
        "Credit Hours Completed": [
            120,
            90,
            110,
        ],
    })

print("Table Of UNB Students\n")
print(StudentGPA)
print("\n")
print("The first 2 rows of the table\n")
print(StudentGPA.head(2))
print("The last 2 rows of the table\n")
print(StudentGPA.tail(2))
print("\n")
print("Descriptive statistics of the table\n")
print(StudentGPA.describe())
print("\n")
print("Information about the table\n")
print(StudentGPA.info())
print("\n")
print("The column names of the table\n")

tableColumns = StudentGPA.columns
print(tableColumns) #prints the column names of the dataframe
print("\n")

