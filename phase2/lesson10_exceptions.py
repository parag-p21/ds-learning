class DivisionByZeroError(Exception):
    pass
def division(a,b):
    if not isinstance(a, (int, float)) or not isinstance(b,(int,float)):
        raise ValueError("Both a and b must be a number")
    if b==0:
        raise DivisionByZeroError("Cannot divide by zero")
    return a / b
try:
    print(division(10,2))
except (ValueError ,DivisionByZeroError) as e :
    print(e)

try:
    print(division(10,0))
except DivisionByZeroError as e :
    print(e)


try:
    print(division(10,"2"))
except ValueError  as e :
    print(e)




#2.
class EcommerceError(Exception):
    pass
class OutOfStockError(EcommerceError):
    pass
class InvalidQuantityError(EcommerceError):
    pass

def add_to_cart(product ,quantity ,stock):
    if stock == 0:
        raise OutOfStockError("Product is out of stock.")
    if quantity < 0:
        raise InvalidQuantityError("Entered quantity is invalid or negative")
        
    else:
        return f"Added {quantity} x {product} to cart"


# 1. Normal case
try:
    print(add_to_cart("Laptop", 2, 10))
except EcommerceError as e:
    print(e)


# 2. Out of stock
try:
    print(add_to_cart("Phone", 1, 0))
except OutOfStockError as e:
    print(e)


# 3. Invalid quantity
try:
    print(add_to_cart("Mouse", -2, 10))
except InvalidQuantityError as e:
    print(e)


def safe_read_file(filepath):
    try:
        with open(filepath, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"File not found: {filepath}. Please check the path.")
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise    # re-raises same exception

# Test 1 — file exists (use diary.txt you created earlier)
print(safe_read_file("diary.txt"))

# Test 2 — file doesn't exist
print(safe_read_file("ghost.txt"))



#Mini Challenge
class InvalidAgeError(Exception):
    pass

class InvalidIncomeError(Exception):
    pass

class DataValidator:
    def validate_age(self, age):
        if not isinstance(age, int) or not (18 <= age <= 65):
            raise InvalidAgeError(f"Invalid age: {age}. Must be int between 18-65")
    
    def validate_income(self, income):
        if not isinstance(income, (int, float)) or income < 0:
            raise InvalidIncomeError(f"Invalid income: {income}. Must be positive")
    def validate_record(self, record):
        self.validate_age(record["age"])
        self.validate_income(record["income"])
        return "Valid record"

validator = DataValidator()

records = [
    {"name": "Parag", "age": 19, "income": 50000},
    {"name": "Riya", "age": 15, "income": 60000},
    {"name": "Aman", "age": 25, "income": -5000},
]

for record in records:
    try:
        result = validator.validate_record(record)
        print(f"{record['name']}: {result}")
    except InvalidAgeError as e:
        print(f"{record['name']}: Age error — {e}")
    except InvalidIncomeError as e:
        print(f"{record['name']}: Income error — {e}")