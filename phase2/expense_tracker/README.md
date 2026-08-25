# CLI Expense Tracker

A command-line personal expense tracker built in Python. Add, view, filter, sort, and
persist your expenses across sessions — all from a simple terminal menu.

Built as the Phase 2 capstone project of my Data Science learning roadmap, this project
was designed to apply every core Python concept from Phase 2 in one working program.

## Features

- Add new expenses with input validation (rejects negative amounts, empty fields)
- View all expenses in a clean, aligned format
- View spending totals grouped by category
- Filter expenses by category
- Sort expenses by amount (ascending/descending)
- Automatic save on exit, automatic load on startup — data persists between sessions

## How to Run

```bash
# Clone the repo
git clone https://github.com/parag-p21/ds-learning.git
cd ds-learning/phase2/expense_tracker

# Set up virtual environment
python -m venv venv
venv\Scripts\activate      # Windows

# Install dependencies (none currently required beyond standard library)
pip install -r requirements.txt

# Run the program
python expense_tracker.py
```

## Sample Usage

```
===================================
       EXPENSE TRACKER
===================================
1. Add Expense
2. View All Expenses
3. Filter by Category
4. View Totals by Category
5. Sort by Amount
6. Save & Exit
===================================
Choose option (1-6): 4

--- Totals by Category ---
Food         ₹   1026.00
Travel       ₹     90.00
Entertainment ₹    400.00
TOTAL        ₹   1516.00
```

## Python Concepts Used

| Concept | Where It's Used |
|---|---|
| Lists | Storing all expense records |
| Tuples | Each expense stored as `(name, amount, category, date)` |
| Dictionaries | Category-wise totals (frequency counting pattern) |
| Sets | Tracking unique categories |
| String manipulation | Formatting display output, parsing CSV lines |
| Lambda / map / filter | Filtering by category/date, sorting by amount |
| Generators | Memory-efficient loading of expenses from file (`yield`) |
| Exception handling | Input validation, graceful handling of missing files |
| File handling | Saving/loading data as CSV |
| Virtual environments | Isolated project dependencies |

## Known Limitations / Future Improvements

- No date format validation — currently accepts any string as a date
- No ability to edit or delete existing expenses (only add)
- No data visualization (planned for Phase 4 once NumPy/Pandas/Matplotlib are covered)
- Could be extended with a budget-limit warning feature

## Project Structure

```
expense_tracker/
├── expense_tracker.py    # main program
├── expenses.csv           # data file (auto-created on first save)
├── requirements.txt        # dependencies
├── .gitignore                # excludes venv/ from version control
└── README.md                  # this file
```

---
*Built by Parag Patle as part of a structured Data Science learning roadmap.*
*GitHub: [parag-p21](https://github.com/parag-p21)*
