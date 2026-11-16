
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=venom&height=230&color=0:102A56,100:2563EB&text=Python%20File%20Handling&fontSize=42&fontColor=FFFFFF&animation=fadeIn&desc=Institute%20Expense%20Tracker%20%7C%20Attendance%20Cleaner&descSize=16&descAlignY=70" width="100%" alt="Python File Handling Banner">
</p>

<h1 align="center">Python Files & Errors Assessment</h1>

<p align="center">
  <b>Smart Institute Management Tools using Python</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Status-Completed-success" alt="Status">
  <img src="https://img.shields.io/badge/Concepts-File%20Handling-orange" alt="File Handling">
  <img src="https://img.shields.io/badge/Concepts-Sets-purple" alt="Sets">
  <img src="https://img.shields.io/badge/Concepts-Comprehensions-blueviolet" alt="Comprehensions">
  <img src="https://img.shields.io/badge/Project-Beginner%20Friendly-brightgreen" alt="Beginner Friendly">
</p>

<p align="center">
  <a href="https://github.com/meesam-ali-sherazi/python-files-errors-assessment">
    <img src="https://img.shields.io/badge/Explore%20Repository-181717?style=for-the-badge&logo=github&logoColor=white" alt="Explore Repository">
  </a>
  <a href="https://replit.com/github/meesam-ali-sherazi/python-files-errors-assessment">
    <img src="https://img.shields.io/badge/Run%20Online-F26207?style=for-the-badge&logo=replit&logoColor=white" alt="Run Online">
  </a>
</p>

---

## 📌 1. Project Overview

This project contains two Python-based management applications designed for a training institute.

The purpose is to demonstrate practical use of Python file handling, exception handling, sets, list comprehensions, functions, loops, and conditions.

### Applications

| Application | Python File | Purpose |
|---|---|---|
| Institute Expense Tracker | `expense_tracker.py` | Record and manage daily institute expenses |
| Student Attendance Cleaner | `attendance_cleaner.py` | Clean attendance records and remove duplicate names |

### Project Architecture

```text
       PYTHON INSTITUTE MANAGEMENT SYSTEM
                       |
            +----------+----------+
            |                     |
     EXPENSE TRACKER       ATTENDANCE CLEANER
            |                     |
      expenses.csv          attendance.txt
            |                     |
     Category Totals        Name Cleaning
            |                     |
       Save Records          Remove Duplicates
                                  |
                           Sort Alphabetically
                                  |
                         attendance_clean.csv
```

---

## 📁 2. Repository Structure

```text
python-files-errors-assessment/
│
├── expense_tracker.py
│
├── attendance_cleaner.py
│
├── attendance.txt
│
└── README.md
```

**Automatically generated files:**

- `expenses.csv` – stores expense records.
- `attendance_clean.csv` – stores cleaned attendance records.

---

## 💰 3. Task 1 — Institute Expense Tracker

**File:** `expense_tracker.py`

### Overview

The Institute Expense Tracker is a simple Python application that helps administration maintain daily operational expenses.

Users can add expenses, view saved records, and calculate total expenses according to categories.

### Features

- Add new expense records.
- Store date, item, category, and amount.
- Save records in `expenses.csv`.
- Load previously saved expenses.
- Display all expense records.
- Calculate category-wise totals.
- Display unique categories using a set.
- Handle invalid numeric input using `ValueError`.

### Program Menu

```text
===== INSTITUTE EXPENSE TRACKER =====

1. Add New Expense
2. Show All Expenses
3. Calculate Total Expenses by Category
4. Exit

Enter your choice:
```

### How It Works

1. The program checks whether `expenses.csv` exists.
2. Previously saved records are loaded.
3. The user selects an option from the menu.
4. New expense details are collected.
5. The amount is validated.
6. The expense is added to the list.
7. All records are saved in the CSV file.

### Error Handling

| Error / Validation | Purpose |
|---|---|
| `FileNotFoundError` | Starts with an empty list if the CSV file does not exist |
| `ValueError` | Handles invalid numeric amounts |
| Amount validation | Rejects zero and negative amounts |

### Concepts Used

- File Handling
- CSV Module
- Dictionaries
- Lists
- Sets
- Functions
- While Loop
- For Loop
- If-Else Conditions
- Try-Except

---

## 🎓 4. Task 2 — Student Attendance Cleaner

**File:** `attendance_cleaner.py`

### Overview

The Student Attendance Cleaner is designed to organize student attendance records.

It cleans unnecessary spaces, standardizes capitalization, removes duplicate names, and sorts students alphabetically.

### Features

- Read student names from `attendance.txt`.
- Remove unnecessary spaces using `strip()`.
- Convert names into title case using `title()`.
- Use list comprehension to clean records.
- Remove duplicate names using sets.
- Sort names alphabetically.
- Save cleaned records in `attendance_clean.csv`.
- Display original and unique student counts.

### Sample Input

`attendance.txt`

```text
Ali
ahmed
  Ali
Usman
sara
AHMED
  usman
Fatima
sara
Hassan
```

### Expected Output

```text
===== ATTENDANCE REPORT =====

Original Records: 10
Unique Students: 6

===== CLEANED ATTENDANCE LIST =====

Ahmed
Ali
Fatima
Hassan
Sara
Usman

Cleaned attendance saved successfully!
```

### Error Handling

| Error | Purpose |
|---|---|
| `FileNotFoundError` | Displays a helpful message if `attendance.txt` is missing |

### Concepts Used

- File Handling
- Text File Reading
- CSV Writing
- List Comprehension
- Sets
- `strip()`
- `title()`
- `sorted()`
- Exception Handling

---

## 🧠 5. Python Concepts Explained

### File Handling

Used to read and write data in external files.

Example:

```python
with open("attendance.txt", "r") as file:
    names = file.readlines()
```

### Exception Handling

Used to prevent programs from crashing when an expected error occurs.

Example:

```python
try:
    amount = float(input("Enter amount: "))

except ValueError:
    print("Invalid amount!")
```

### Sets

Sets store unique values and automatically remove duplicates.

Example:

```python
categories = {"Utilities", "Stationery", "Utilities"}

print(categories)
```

### List Comprehension

A short and readable way to create a new list from existing data.

Example:

```python
cleaned_names = [
    name.strip().title()
    for name in original_names
    if name.strip()
]
```

---

## ▶️ 6. How to Run the Project

### Requirements

- Python 3.8 or newer
- Visual Studio Code (recommended)
- Git (for cloning the repository)

### Step 1 — Clone Repository

Open your terminal:

```bash
git clone https://github.com/meesam-ali-sherazi/python-files-errors-assessment.git
```

### Step 2 — Open Project Folder

```bash
cd python-files-errors-assessment
```

### Step 3 — Run Expense Tracker

```bash
python expense_tracker.py
```

Alternative:

```bash
python3 expense_tracker.py
```

Windows alternative:

```bash
py expense_tracker.py
```

### Step 4 — Run Attendance Cleaner

```bash
python attendance_cleaner.py
```

Alternative:

```bash
python3 attendance_cleaner.py
```

---

## 🧪 7. Testing & Test Cases

Both applications should be checked with normal, invalid, and edge-case inputs.

### Task 1 — Expense Tracker

| # | Test Scenario | Input | Expected Result |
|---|---|---|---|
| 1 | Add expense | Internet Bill, 2500 | Expense saved |
| 2 | Invalid amount | abc | ValueError handled |
| 3 | Zero amount | 0 | Amount rejected |
| 4 | Negative amount | -500 | Amount rejected |
| 5 | Valid amount after error | 1500 | Expense saved |
| 6 | Duplicate categories | Utilities twice | One unique category |
| 7 | Display expenses | Choice 2 | All records displayed |
| 8 | Calculate totals | Choice 3 | Category-wise totals |
| 9 | Reload records | Restart program | Previous data loaded |
| 10 | Missing CSV | Delete expenses.csv | Empty list initialized |

### Task 2 — Attendance Cleaner

| # | Test Scenario | Input | Expected Result |
|---|---|---|---|
| 1 | Duplicate names | Ali, Ali | One Ali |
| 2 | Different capitalization | ali, ALI | One Ali |
| 3 | Extra spaces | `  Ahmed  ` | Ahmed |
| 4 | Alphabetical sorting | Random names | Sorted A–Z |
| 5 | Blank lines | Empty lines | Ignored |
| 6 | Empty file | No names | Zero unique students |
| 7 | Missing file | No attendance.txt | Error message |
| 8 | Sample records | 10 records | 6 unique students |

---

## 💾 8. Sample Expense Data Persistence

One of the main requirements is that expense records must remain saved even after closing the program.

### First Run — Save Expense

```text
Enter your choice: 1

Enter expense date: 14-11-2026
Enter item name: Internet Bill
Enter expense category: Utilities
Enter expense amount: 2500

Expenses saved successfully!
```

The program creates `expenses.csv`:

```csv
date,item,category,amount
14-11-2026,Internet Bill,Utilities,2500.0
```

### Second Run — Load Previous Expense

```text
Previous expenses loaded successfully!

Enter your choice: 2

===== ALL EXPENSES =====

Date: 14-11-2026
Item: Internet Bill
Category: Utilities
Amount: Rs. 2500.00
```

**Result:** Previously saved expense records are successfully loaded from the CSV file.

---

## 📊 9. Project Learning Outcomes

After completing this assessment, the following Python concepts are practiced:

- Reading and writing external files.
- Working with CSV files.
- Handling runtime errors.
- Validating user input.
- Managing data using lists and dictionaries.
- Removing duplicates using sets.
- Cleaning data using list comprehension.
- Sorting and processing records.
- Creating reusable functions.
- Building simple real-world management applications.

---

## 👨‍💻 10. Author

<p align="center">
  <b>Muhammad Meesam Ali Sherazi</b>
  <br>
  Python Programming Student
  <br><br>
  <a href="https://github.com/meesam-ali-sherazi">
    <img src="https://img.shields.io/badge/GitHub-meesam--ali--sherazi-181717?style=for-the-badge&logo=github" alt="GitHub Profile">
  </a>
</p>

---

<p align="center">
  <b>Built with Python 🐍</b>
  <br>
  <sub>Python Files & Errors Assessment | 2026</sub>
</p>
