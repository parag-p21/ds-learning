# expense_tracker.py

expenses = []    # this will hold all expense tuples

def add_expense(name, amount, category, date):
    """Adds a new expense after validating input"""
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if not name or not category:
        raise ValueError("Name and category cannot be empty")
    
    expense = (name, amount, category, date)
    expenses.append(expense)
    print(f"Added: {name} - ₹{amount} ({category})")

# Test it
add_expense("Lunch", 120, "Food", "2026-08-23")
add_expense("Bus ticket", 30, "Travel", "2026-08-23")
print(expenses)

def view_all_expenses():
    """Display all expenses in a clean format"""
    if not expenses:
        print("No expenses recorded yet.")
        return
    
    print("\n--- All Expenses ---")
    for name, amount, category, date in expenses:    # tuple unpacking
        print(f"{date} | {name:<15} ₹{amount:>8.2f} | {category}")

def totals_by_category():
    """Calculate and display total spent per category"""
    totals = {}    # category -> total amount
    
    for name, amount, category, date in expenses:
        if category in totals:
            totals[category] += amount
        else:
            totals[category] = amount
    
    print("\n--- Totals by Category ---")
    for category, total in totals.items():
        print(f"{category:<12} ₹{total:>10.2f}")
    
    grand_total = sum(totals.values())
    print(f"{'TOTAL':<12} ₹{grand_total:>10.2f}")

# Add a few more test expenses first
add_expense("Groceries", 850, "Food", "2026-08-22")
add_expense("Movie", 400, "Entertainment", "2026-08-21")
add_expense("Auto", 60, "Travel", "2026-08-22")

# Test the new functions
view_all_expenses()
totals_by_category()