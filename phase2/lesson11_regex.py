import re 

text = "Contact us at support@company.com or sales@business.org, not fake@@email"
def extract_emails(text):
    emails=re.findall(r"[\w.-]+@[\w.-]+\.\w{2,4}", text)   #re.findall needs two things: re.finadall(pattern,string)
    return emails

print(extract_emails(text))


#2.
import re
phones = ["+91-9876543210", "(987)654-3210", "987 654 3210", "9876543210"]

def clean_phone(phone):
    phone = re.sub(r"[^\d]","",phone)
    phone = phone[-10:]
    return phone

cleaned = [clean_phone(phone) for phone in phones]
print(cleaned)

#3.
def validate_password(password):
    if len(password) < 8 :
        return False
    if not re.search(r"[A-Z]" , password):
        return False
    if not re.search(r"[0-9]" , password):
        return False
    if not re.search(r"[@#$%^&*]" , password):
        return False
    else:
        return True
print(validate_password("Parag@123"))
print(validate_password("weakpass"))



#Mini challenge 

data = """
Product: Laptop | Price: Rs.55000 | Stock: 45units
Product: Phone | Price: Rs.15000 | Stock: 12units
Product: Tablet | Price: Rs.25000 | Stock: 0units
Product: Earbuds | Price: Rs.3000 | Stock: 8units
"""

import re

data = """
Product: Laptop | Price: Rs.55000 | Stock: 45units
Product: Phone | Price: Rs.15000 | Stock: 12units
Product: Tablet | Price: Rs.25000 | Stock: 0units
Product: Earbuds | Price: Rs.3000 | Stock: 8units
"""

# Pattern explanation:
# Product:\s+   → matches "Product: " (with any spaces after colon)
# (\w+)         → captures the product name (one or more word characters)
# .*?Price: Rs\.→ matches " | Price: Rs." (.*? means any chars, non-greedy)
# (\d+)         → captures the price digits
# .*?Stock:\s+  → matches " | Stock: "
# (\d+)         → captures the stock digits

pattern = r"Product:\s+(\w+).*?Price:\s+Rs\.(\d+).*?Stock:\s+(\d+)"

# re.findall with groups returns list of tuples
matches = re.findall(pattern, data)
print(matches)
# [('Laptop', '55000', '45'), ('Phone', '15000', '12'), ...]

# Convert each tuple into a dictionary
products = []
for name, price, stock in matches:  # unpack each tuple
    products.append({
        "product": name,
        "price": int(price),     # convert string to int
        "stock": int(stock)      # convert string to int
    })

print("\nAll products:")
for p in products:
    print(p)

# Filter only in-stock products
print("\nIn-stock products:")
in_stock = [p for p in products if p["stock"] > 0]
for p in in_stock:
    print(f"{p['product']}: ₹{p['price']} ({p['stock']} units)")