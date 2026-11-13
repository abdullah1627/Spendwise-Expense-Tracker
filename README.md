# SpendWise - Expense Tracker

A console-based expense tracker written in Python, built with object-oriented design. It records daily spending, organizes it by category, and saves everything to a JSON file.

## Features
- Add, view, and delete expenses
- Category summary with totals and a grand total
- Data saved automatically to a JSON file and reloaded on startup
- Input validation for amounts, categories, and dates (YYYY-MM-DD)
- Unique expense ids, even after deletions


## Project structure
```
spendwise/
├── main.py       # menu and user interaction
├── manager.py    # ExpenseManager class (add, delete, total, summary)
├── expense.py    # Expense class (data model)
├── storage.py    # saving and loading the JSON file
├── utils.py      # input validation helpers
└── README.md
```

## How to run
1. Install Python 3.10 or newer
2. Clone this repository:
   ```
   git clone https://github.com/abdullah1627/Spendwise-Expense-Tracker.git
   cd Spendwise-Expense-Tracker
   ```
3. Run:
   ```
   python main.py
   ```

Your data is stored in `expenses.json`, which is created automatically on first use.

## What I learned
- Python functions, dictionaries, and file handling
- Reading and writing JSON
- Input validation with `try/except`
- Object-oriented design: separating the data model, the logic, storage, and the user interface
- Using Git and GitHub

## Roadmap
- [x] Console version with JSON storage
- [x] OOP refactor (Expense and ExpenseManager classes)
- [ ] PostgreSQL database
- [ ] FastAPI backend
- [ ] Angular frontend
- [ ] User login and deployment