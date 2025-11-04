import pandas as pd
import numpy as np
import csv

# ------------------------------------------
# TASK 1(a) - STUDENT GRADES DATA PROCESSING
# ------------------------------------------

print("\n--- TASK 1(a): Student Grades Dataset ---")

# Load dataset
grades_df = pd.read_csv("student_grades.csv")
print("\nFirst 5 rows:")
print(grades_df.head())

# Data Exploration
print("\nMissing values per column:")
print(grades_df.isnull().sum())

print("\nSummary statistics:")
print(grades_df[['Age','Math_Score','English_Score','Science_Score']].describe())

print("\nUnique Age values:", grades_df['Age'].unique())

# Handling Missing Values (Fill with Mean)
for col in ['Math_Score', 'English_Score', 'Science_Score']:
    grades_df[col].fillna(grades_df[col].mean(), inplace=True)

print("\nAfter filling missing values:")
print(grades_df)

# Data Preparation
grades_df['Total_Score'] = grades_df['Math_Score'] + grades_df['English_Score'] + grades_df['Science_Score']

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
grades_df['Name_Encoded'] = le.fit_transform(grades_df['Name'])

print("\nFinal Prepared Student Dataset:")
print(grades_df)


# ------------------------------------------
# TASK 1(b) - AIRLINE BOOKING DATA PROCESSING
# ------------------------------------------

print("\n--- TASK 1(b): Airline Booking Records ---")

# Load using pandas
df_pandas = pd.read_csv("airline_bookings.csv")
print("\nLoaded using pandas.read_csv():")
print(df_pandas.head())


# Load using csv.reader()
print("\nLoaded using csv.reader():")
with open("airline_bookings.csv", 'r') as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        print(row)
        if i == 5: break


# Load using numpy.loadtxt() (skip header)
print("\nLoaded using numpy.loadtxt():")
try:
    arr1 = np.loadtxt("airline_bookings.csv", delimiter=",", dtype=str, skiprows=1)
    print(arr1[:5])
except:
    print("numpy.loadtxt() skipped due to non-numeric data.")


# Load using numpy.genfromtxt()
print("\nLoaded using numpy.genfromtxt():")
arr2 = np.genfromtxt("airline_bookings.csv", delimiter=",", dtype=str)
print(arr2[:5])


# Connect Dataset Details Exploration
print("\nDetails of specific Flight_ID = 'FL102':")
print(df_pandas[df_pandas['Flight_ID'] == 'FL102'])

print("\nUnique Flight Classes:")
print(df_pandas['Class'].unique())

print("\nUnique Destinations:")
print(df_pandas['Destination'].unique())

print("\nSummary statistics for Amount:")
print(df_pandas['Amount'].describe())


# Conditional Filtering
print("\nFlight_IDs where Amount > 15000:")
print(df_pandas[df_pandas['Amount'] > 15000]['Flight_ID'])

print("\nBooking_IDs where Amount between 20000 and 40000:")
print(df_pandas[(df_pandas['Amount'] >= 20000) & (df_pandas['Amount'] <= 40000)]['Booking_ID'])


# Data Preparation
df_pandas['Booking_Date'] = pd.to_datetime(df_pandas['Booking_Date'])
df_pandas['Travelled_Date'] = pd.to_datetime(df_pandas['Travelled_Date'])
df_pandas['Booking_Lead_Time'] = (df_pandas['Travelled_Date'] - df_pandas['Booking_Date']).dt.days

print("\nCleaned & Enriched Dataset:")
print(df_pandas)
