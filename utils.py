from datetime import date, datetime


def pause():
    input("\nPress Enter to return to the menu.....")


def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter the expense amount: ").strip())
            if amount <= 0:
                print("Amount must be greater than zero.")
            else:
                return amount
        except ValueError:
            print("Please enter a valid number.")


def get_valid_date():
    while True:
        date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()

        if not date_input:
            return date.today().isoformat()

        try:
            parsed = datetime.strptime(date_input, "%Y-%m-%d")
            return parsed.date().isoformat()
        except ValueError:
            print("Invalid date. Use YYYY-MM-DD (e.g. 2026-10-11).")