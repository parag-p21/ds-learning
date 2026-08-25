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


def filter_by_category(category_name):
    """Returns list of expenses matching a category, using filter+lambda"""
    filtered = list(filter(lambda e: e[2] == category_name, expenses))
    return filtered

def filter_by_date_range(start_date, end_date):
    """Returns expenses within a date range (string comparison works for YYYY-MM-DD format)"""
    filtered = list(filter(lambda e: start_date <= e[3] <= end_date, expenses))
    return filtered

def sort_by_amount(descending=False):
    """Returns expenses sorted by amount"""
    return sorted(expenses, key=lambda e: e[1], reverse=descending)

def get_unique_categories():
    """Returns set of all categories used so far"""
    return {e[2] for e in expenses}    # set comprehension

# Test all four functions
print("\n--- Food expenses only ---")
for e in filter_by_category("Food"):
    print(e)

print("\n--- Expenses between 2026-08-22 and 2026-08-23 ---")
for e in filter_by_date_range("2026-08-22", "2026-08-23"):
    print(e)

print("\n--- Sorted by amount (highest first) ---")
for e in sort_by_amount(descending=True):
    print(e)

print("\n--- Unique categories used ---")
print(get_unique_categories())



import csv

def save_expenses(filepath="expenses.csv"):
    """Saves all expenses to a CSV file"""
    with open(filepath, "w") as f:
        f.write("name,amount,category,date\n")    # header row
        for name, amount, category, date in expenses:
            f.write(f"{name},{amount},{category},{date}\n")
    print(f"Saved {len(expenses)} expenses to {filepath}")


def load_expenses(filepath="expenses.csv"):
    """Generator that yields one expense at a time from file"""
    try:
        with open(filepath, "r") as f:
            next(f)    # skip header row
            for line in f:
                name, amount, category, date = line.strip().split(",")
                yield (name, float(amount), category, date)
    except FileNotFoundError:
        print(f"No saved data found at {filepath}. Starting fresh.")
        return


def load_expenses_into_list(filepath="expenses.csv"):
    """Loads expenses from file into the global expenses list"""
    global expenses
    expenses = list(load_expenses(filepath))
    print(f"Loaded {len(expenses)} expenses from {filepath}")


# Test it
save_expenses()

# Clear the in-memory list to prove loading actually works
expenses = []
print("Expenses cleared from memory:", expenses)

load_expenses_into_list()
view_all_expenses()


#Stage 5 
def show_menu():
    print("\n" + "="*35)
    print("       EXPENSE TRACKER")
    print("="*35)
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Filter by Category")
    print("4. View Totals by Category")
    print("5. Sort by Amount")
    print("6. Save & Exit")
    print("="*35)


def main():
    load_expenses_into_list()    # load saved data on startup
    
    while True:
        show_menu()
        choice = input("Choose option (1-6): ").strip()
        
        try:
            if choice == "1":
                name = input("Expense name: ").strip()
                amount = float(input("Amount: ").strip())
                category = input("Category: ").strip()
                date = input("Date (YYYY-MM-DD): ").strip()
                add_expense(name, amount, category, date)
            
            elif choice == "2":
                view_all_expenses()
            
            elif choice == "3":
                cat = input("Enter category to filter: ").strip()
                results = filter_by_category(cat)
                if results:
                    for e in results:
                        print(e)
                else:
                    print(f"No expenses found in category: {cat}")
            
            elif choice == "4":
                totals_by_category()
            
            elif choice == "5":
                for e in sort_by_amount(descending=True):
                    print(e)
            
            elif choice == "6":
                save_expenses()
                print("Goodbye!")
                break
            
            else:
                print("Invalid option. Choose 1-6.")
        
        except ValueError as e:
            print(f"Invalid input: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()