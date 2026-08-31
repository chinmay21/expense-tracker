import os
import json
from datetime import datetime

def add_expense(expenses):
    incorrect_amount = True
    incorrect_category = True
    incorrect_description = True
    incorrect_date = True
    expense_id = 0
    while incorrect_amount:
        try:
            amount = int(input("Enter an amount: "))
            if amount <= 0:
                print("Amount can't be null or negative")
            else:
                incorrect_amount = False
        except ValueError:
            print("Only numeric values are accepted!")
    while incorrect_category:
        category = input("Enter a category: ")
        if not category.isalpha():
            print("Please enter a valid string value!")
        else:
            incorrect_category = False
    while incorrect_description:
        description = input("Enter a description: ")
        if description.isdigit():
            print("Please enter a valid string value!")
        else:
            incorrect_description = False
    while incorrect_date:
        date_string = input("Enter a date (YYYY-MM-DD): ")
        try:
            date = datetime.strptime(date_string, "%Y-%m-%d")
            date = date.strftime("%Y-%m-%d")
            incorrect_date = False
        except ValueError:
            print(f"Invalid date: {date_string}")
    print("Expense recorded successfully")

    expense_id += len(expenses) + 1

    expense = { "Expense": expense_id,
                "Amount": amount,
                "Category": category,
                "Description": description,
                "Date": date}
    expenses.append(expense)
    create_json_file(expenses)  
    

def view_expense(expenses):
    for expense in expenses:
        for key, value in expense.items():
            print(f"{key}: {value}")

def delete_expense(expenses):
    invalid_expense = True
    while invalid_expense:
        try:
            id = int(input("Enter an expense number to delete: "))
            if id <= 0:
                print("Expense number can't be zero or negative!")
            else:
                invalid_expense = False
        except ValueError:
            print("Please enter a valid expense number to delete!")
            return
        if len(expenses) == 0:
            print("There are no expenses to delete, Spend some money first!")
        elif len(expenses) < id:
            print("Please enter a valid expense number that exists!")
        else:
            expenses.pop(id - 1)
            for expense in expenses:
                if expense["Expense"] > id:                                       
                    expense["Expense"] -= 1
            create_json_file(expenses) 
            print("Expense deleted successfully!")            
            

def view_total(expenses):
    total_expense = 0
    if len(expenses) == 0:
        print("There are no expenses to total, Dude spend some money first!")
    else:
        for expense in expenses:
            total_expense += expense["Amount"]
        print(f"Your total expense is ${total_expense}")

def view_category_summary(expenses):
    invalid_category = True
    category_total = 0
    while invalid_category:
        if len(expenses) == 0:
            print("There are not categories to summarize!")
            invalid_category = False
        else:
            category = input("Please enter a category to view category summary: ")
            if(category.isdigit()):
                print("Please enter a valid category to summarize!")
            else:
                invalid_category = False

                if [expense for expense in expenses if expense["Category"] == category]:
                    print(f"===== Expenses for {category} category =====")
                    for expense in expenses:
                        if expense["Category"] == category:
                            for key, value in expense.items():
                                    print(f"{key}: {value}")
                            print("*************")
                            category_total += expense["Amount"]
                    print(f"Total spent on {category}: ${category_total}")
                else:
                    print("No category found")

def create_json_file(expenses):
    json_path = "expense.json"
    with open(json_path, "w") as file:
        json.dump(expenses, file, indent=2)
    print("JSON file created successfully")

def load_expenses():
    json_path = "expense.json"
    if os.path.exists(json_path):
        with open(json_path, "r") as json_file:
            expenses = json.load(json_file)
        return expenses
    else:
        expenses = []  
        return expenses   


def main():
    is_running = True
    expenses = load_expenses()
    while is_running:

        user_input = input("Please enter a number to select the task to perform (1.Add Expense)"
                            "(2.View Expenses) (3.Delete Expense) (4.View Total)"
                            "(5.View Category Summary) (6.Exit): ")

        if user_input == "1":
            add_expense(expenses)
        elif user_input == "2":
            view_expense(expenses)
        elif user_input == "3":
            delete_expense(expenses)        
        elif user_input == "4":
            view_total(expenses)       
        elif user_input == "5":
            view_category_summary(expenses)
        elif user_input == "6":
            is_running = False
        else:
            print("Please select a valid value from the given options!")
            is_running = False

if __name__ == "__main__":
    main()