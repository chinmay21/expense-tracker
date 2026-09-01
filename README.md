# Expense Tracker

A simple command-line **Expense Tracker built with Python** that allows users to record, view, delete, and analyze their expenses. The project uses **JSON for data persistence**, so expenses remain available even after the program is closed.

## Features

* Add a new expense
* View all recorded expenses
* Delete an expense
* Calculate total expenses
* View expenses by category
* Calculate total spending for a specific category
* Store expenses persistently in a JSON file
* Validate user input for common invalid entries

## How It Works

When the application starts, it loads previously saved expenses from `expense.json`.

The user is presented with the following menu:

```text
1. Add Expense
2. View Expenses
3. Delete Expense
4. View Total
5. View Category Summary
6. Exit
```

### 1. Add Expense

The user provides:

* Amount
* Category
* Description
* Date

Each expense is assigned an expense number and stored as a dictionary inside a list.

Example:

```json
{
  "Expense": 1,
  "Amount": 500,
  "Category": "Food",
  "Description": "Lunch",
  "Date": "29:08:2026"
}
```

### 2. View Expenses

Displays all expenses currently stored in the tracker.

### 3. Delete Expense

The user enters the expense number they want to remove.

After deletion, the remaining expense numbers are renumbered and the updated data is saved to the JSON file.

### 4. View Total

Calculates and displays the total amount spent across all recorded expenses.

### 5. View Category Summary

The user enters a category, such as `Food`.

The application displays all expenses belonging to that category and calculates the total amount spent within that category.

### 6. Exit

Closes the application.

## Data Persistence

The project uses Python's built-in `json` module to store expense data in:

```text
expense.json
```

When an expense is added or deleted, the JSON file is updated automatically.

When the application starts again, the existing expenses are loaded from the file.

## Technologies Used

* **Python**
* **JSON**
* `os` module
* File handling
* Lists
* Dictionaries
* Functions
* Loops
* Conditional statements
* Exception handling
* Input validation

## Project Structure

```text
Expense-Tracker/
│
├── expense_tracker.py
├── expense.json
└── README.md
```

> `expense.json` is created automatically when the application saves expense data.

## How to Clone and Run

### Prerequisites

Make sure you have the following installed:

* Python 3
* Git

### 1. Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/chinmay21/expense-tracker.git
```

### 2. Navigate to the Project

```bash
cd expense-tracker
```

### 3. Run the Application

```bash
python expense_tracker.py
```

If your system uses `python3` instead of `python`, run:

```bash
python3 expense_tracker.py
```

## What I Learned

This project helped me practice several important Python concepts, including:

* Working with lists and dictionaries
* Creating and using functions
* Handling user input
* Input validation
* Exception handling with `try` and `except`
* Reading and writing files
* Working with JSON data
* Persisting data between program executions
* Organizing application logic into separate functions

## Future Improvements

Possible improvements for future versions include:

* Support for decimal amounts
* Case-insensitive category searching
* Editing existing expenses
* Searching expenses
* Filtering expenses by date
* Better command-line formatting
* More reliable expense ID management
* Separating application logic and user-interface logic
* Migrating from JSON to a database such as PostgreSQL

## License

This project was created as a learning project and is available for educational and personal use.
