# Videodata Analysis – Task 1 (Data Wrangling)

## 📌 Project Overview
This project focuses on **data understanding, data quality assessment, data cleaning, and feature engineering** using a CSV dataset (`Videodata.csv`).  
The goal of Task-1 is to transform raw data into a **clean, analysis-ready dataset** with proper documentation.

This task was completed as part of an internship assignment to demonstrate foundational data wrangling skills.

---

## 📂 Dataset Description
- **Dataset name:** Videodata.csv  
- **Type:** Tabular CSV data  
- **Content:** Demographic and work-related attributes such as age, working hours, capital gain/loss, etc.

A detailed explanation of each column is provided in **`data_dictionary.md`**.

---

## 🧠 Task Objectives
The following objectives were achieved:

1. Understand the dataset structure and columns  
2. Identify data quality issues (missing values, duplicates, formatting issues)  
3. Clean and preprocess the dataset  
4. Perform basic feature engineering  
5. Generate a final cleaned dataset ready for analysis  

---

## 🛠️ Data Cleaning Steps
The following cleaning operations were performed using Python (Pandas):

- Replaced invalid symbols (`?`) with proper missing values
- Removed duplicate rows
- Trimmed extra spaces from text columns
- Checked and handled missing values
- Ensured consistent formatting across columns

All cleaning logic is implemented in **`data_cleaning.py`**.

---

## 🔧 Feature Engineering
New meaningful features were created to enhance the dataset:

- **Age Group:** Categorized individuals into age brackets (Young, Adult, Senior, Old)
- **Work Hours Category:** Classified working hours into Part-time, Full-time, and Overtime
- **Capital Activity:** Identified whether an individual had capital gain, loss, or none

These features improve interpretability and make the data more suitable for analysis.

---

## 📦 Project Files

Videodata.csv                 → Raw dataset
data_dictionary.md            → Column descriptions
data_cleaning.py              → Data cleaning & feature engineering script
final_cleaned_videodata.csv   → Final cleaned dataset
README.md                     → Project documentation

---

## ▶️ How to Run the Code
1. Make sure Python and Pandas are installed  
2. Place all files in the same directory  
3. Run the script:

```bash
python data_cleaning.py

---

4.The cleaned dataset will be saved as:

final_cleaned_videodata.csv
final_cleaned_videodata.csv