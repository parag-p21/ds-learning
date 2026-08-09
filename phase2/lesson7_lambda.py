cube=lambda n: n**3
print("Cube of 4 is",cube(4))

is_even=lambda p: p % 2 == 0
print("Is 6 even",is_even(6))
print("Is 7 even",is_even(7))

full_name = lambda first, last: first + " " + last
print("Full Name:", full_name("Parag", "Patle"))

products = [("Laptop", 55000), ("Phone", 15000),
             ("Tablet", 25000), ("Earbuds", 3000)]
sor=sorted(products,key=lambda s:s[1])
print(sor)

high_price=list(filter(lambda a: a[1]>=10000,products))
print(high_price)
discounted = list(map(lambda a: (a[0], a[1] * 0.90), products))
print(discounted)


temperatures = [22, 35, 18, 40, 28, 15, 38]
above_30=list(filter(lambda a:a>30,temperatures))
print(above_30)

Con_fahrenheit = list(map(lambda t: (t * 9/5) + 32, temperatures))

print(Con_fahrenheit)
print("Above 30°C:",above_30)
print("In Fahrenheit:", Con_fahrenheit)


orders = [
    {"id": 1, "product": "Laptop", "amount": 55000, "status": "delivered"},
    {"id": 2, "product": "Phone", "amount": 15000, "status": "pending"},
    {"id": 3, "product": "Tablet", "amount": 25000, "status": "delivered"},
    {"id": 4, "product": "Earbuds", "amount": 3000, "status": "cancelled"},
    {"id": 5, "product": "Monitor", "amount": 18000, "status": "delivered"},
]

delivered_orders = list(filter(lambda o: o["status"] == "delivered", orders))
product_names = list(map(lambda o: o["product"], delivered_orders))
amounts = list(map(lambda o: o["amount"], delivered_orders))
total_revenue = sum(amounts)
print("Delivered Orders:", delivered_orders)
print("Product Names:", product_names)
print("Total Revenue:", total_revenue)