import json
from datetime import date, datetime

FILE = "expenses.json"

def save_expenses():
    with open(FILE, "w") as file:
        json.dump(expenses, file, indent=4)

def load_expenses():
    try:
        with open(FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return[]
    except json.JSONDecodeError:
        return[]

expenses = load_expenses()

def pause(): 
    input("\nPress Enter to return to the menu.....")


def get_valid_amount():
    while True:
       try:
         amount =float(input("Enter the expense amount: ").strip())

         if amount <= 0:
            print("Amount must be greater than zero.")
         else:
            return amount

       except ValueError:
            print("Please enter a valid number.")

def get_valid_date():
    while True:
        date_input = input("Enter date (yyyy-mm--dd) or press Enter for today: ").strip()

        if not date_input:
            return date.today().isoformat()

        try:
            parsed = datetime.strptime(date_input, "%Y-%m-%d")
            return parsed.date().isoformat()
        except ValueError:
            print("Invalid date. Use YYYY-MM-DD (e.g. 2026-10-11).")


def add_expense():
    print("---Add Expense---")
    amount = get_valid_amount()

    while True:
        category =input("Enter the category of the expense: ").strip().title()
        if not category:
            print("Category cannot be empty")
        else:
            break

    date_input = get_valid_amount()

    note = input("Enter a note(Optional): ").strip()
    
    if expenses:
        expense_id = max(item["id"] for item in expenses) +1
    else:
        expense_id = 1

    dict_expense = {
        "id" : expense_id,
        "amount" : amount,
        "category" : category,
        "date" : date_input,
        "note" : note
    }

    expenses.append(dict_expense)
    save_expenses()
    print("Expense Added! ")


def view_expenses():
    print("--- All Expenses ---")
    if not expenses :
         print("Expense List is Empty! ")
         return
   

    total_expense = 0

    for dict_expense in expenses:
        print("Expense ID: ", dict_expense["id"])
        print("Expense Date: ", dict_expense["date"])
        print("Expense Category: ", dict_expense["category"])
        print("Expense Amount: ", dict_expense["amount"])
        print("Expense Note: ", dict_expense["note"])

        print("-" * 25)
        total_expense += dict_expense["amount"]

    print("Total Spent: " , total_expense)    

    print("-" * 25)
    print("")


def delete_expense():
    print("--- Delete Expenses ---")

    if not expenses :
             print("Expense List is Empty! ")
             return

    view_expenses()

    try:
       delete_id = int(input("Enter the expense id to delete: ").strip())
       
    except ValueError:
        print("Please enter the the valid expense id!")
        return

    for dict_expense in expenses:
        if dict_expense["id"] == delete_id:
            expenses.remove(dict_expense)
            save_expenses()
            print("Expense Deleted! ")
            return
    print("No expense with that id.")


def summary():
    print("===== Summary ======")
    if not expenses :
                 print("Expense List is Empty! ")
                 return
    
    category_totals={}

    for dict_expense in expenses:
     category = dict_expense["category"]
     amount = dict_expense["amount"]
     category_totals[category]= category_totals.get(category, 0)+ amount

    for category, total in category_totals.items():
        print(f"{category}:{total}")

    print("-" * 35)
    print("Grand Total:", sum(category_totals.values()))

 
def show_menu():
    print("\n====== Your Expense Recorder =======")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Delete Expense")
    print("4. Summary")
    print("5. Exit")
    print("-" * 25)
    

def main(): 
    while True:
        show_menu()
        choice = input("Choose an Option(1-5): ").strip()

        if choice == "1":
            add_expense()
            pause()
        elif choice == "2":
            view_expenses()
            pause()
        elif choice == "3":
            delete_expense()
            pause()
        elif choice == "4":
            summary()
            pause()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

main()
