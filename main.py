from manager import ExpenseManager
from storage import load_expenses, save_expenses
from utils import get_valid_amount, get_valid_date, pause

manager = ExpenseManager(load_expenses())

def add_expense_ui():
    print("---Add Expense--")
    amount = get_valid_amount()

    while True:
        category = input("Enter the Category of the Expense: ").strip().title()
        if not category:
            print("Category cannot be empty! ")
        else:
            break
    date_input = get_valid_date()
    note  = input("Enter a note (Optional): ").strip()

    manager.add_expense(amount,category,date_input,note)
    save_expenses(manager.get_all())
    print("Expense Added!")

def view_expense_ui():
    print("---All Expenses ---")
    expenses = manager.get_all()

    if not expenses:
        print("Expense List is Empty!")
        return
    for expense in expenses:
        print(expense)

    print("-"*25)
    print("Total Spent:", manager.total())

def delete_expense_ui():
    print("---Delete Expense ---")

    if not manager.get_all():
        print("Expense List is Empty! ")
        return

    view_expense_ui()

    try:
        delete_id = int(input("Enter the expense id to delete: ").strip())
    except ValueError:
        print("Please enter a valid expense id!")
        return

    if manager.delete_expense(delete_id):
        save_expenses(manager.get_all())
        print("Expense Deleted! ")
    else:
        print("There is no expense with this id.")

def summary_ui():
    print(" ")
    print("==== Summary ===")

    if not manager.get_all():
        print("Expense List is Empty!")
        
        return

    for category, total in manager.summary_by_category().items():
        print(f"{category}: {total}")

    print("-" * 35)
    print("Grand Total:", manager.total())


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
            add_expense_ui()
            pause()
        elif choice == "2":
            view_expense_ui()
            pause()
        elif choice == "3":
            delete_expense_ui()
            pause()
        elif choice == "4":
            summary_ui()
            pause()
        elif choice == "5":
            print("GoodBye!")
            break
        else:
            print("Invalid Input, Try Again!")

main()