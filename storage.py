
import json
from expense import Expense

FILE = "expenses.json"

def save_expenses(expenses):
    expense_data = []

    for expense in expenses:
        expense_data.append(expense.to_dict())

    
    with open(FILE, "w") as file:
        json.dump(expense_data, file, indent=4)


def load_expenses():
    try:
    
        with open(FILE, "r") as file:
            expense_data = json.load(file)

        expenses = []

        for data in expense_data:
            expense = Expense.from_dict(data)
            expenses.append(expense)

        return expenses

    except (FileNotFoundError, json.JSONDecodeError):
        return []
