from expense import Expense
class ExpenseManager:

    def __init__(self, expenses=None):
        self.expenses = expenses if expenses is not None else []
    

    def _next_id(self):
        if len(self.expenses) == 0:
            return 1
        else:
            return max(expense.expense_id for expense in self.expenses) +1 
        

    def add_expense(self, amount, category, date, note):
        expense_id = self._next_id()

        new_expense = Expense(expense_id, amount, category, date, note)

        self.expenses.append(new_expense)

        return new_expense

    
    def delete_expense(self, expense_id):
        for expense in self.expenses:
            if expense.expense_id == expense_id:
                self.expenses.remove(expense)
                return True

        return False

    
    def get_all(self):
        return self.expenses

    
    def total(self):
        total_amount = 0

        for expense in self.expenses:
            total_amount += expense.amount

        return total_amount

    
    def summary_by_category(self):
        summary = {}

        for expense in self.expenses:
            if expense.category in summary:
                summary[expense.category] += expense.amount
            else:
                summary[expense.category] = expense.amount

        return summary

