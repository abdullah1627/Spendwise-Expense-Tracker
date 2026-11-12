class Expense:
    def __init__(self,expense_id, amount, category, date,note):
        self.expense_id = expense_id
        self.amount = amount
        self.category = category
        self.date = date
        self.note = note
        pass

    def to_dict(self):
        return {
            "id" : self.expense_id,
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "note" : self.note
        }
        pass
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["amount"],
            data["category"],
            data["date"],
            data["note"]
        )

    def __str__(self):
        return f"[{self.expense_id}] {self.date} | {self.category} | {self.amount} | {self.note}"
        pass

if __name__ == "__main__":
    e = Expense(1, 500.0, "Food", "2026-10-11", "Lunch")
    print(e)
    data = e.to_dict()
    print(data)
    print(Expense.from_dict(data)) 