#Shopping bill calculator
n=int(input("Enter the number of items :"))
total = 0

for i in range(n):
    item = input("Enter the name of item : ")
    price = float(input("Enter the price of item : "))
    quantity = int(input(("Enter the quantity of purchased item : ")))

    amount = price*quantity
    total = total + amount 

    print(f"{item} - ₹  {amount :.2f}")

if total >= 5000:
    discount_rate = 20
elif total >= 3000:
    discount_rate = 15
elif total >= 1000:
    discount_rate = 10
else:
    discount_rate = 0

discount = total * discount_rate / 100
amount_after_discount = total - discount

gst = amount_after_discount * .18

final_amount = amount_after_discount + gst

print("==============================SHOPPING BILL================================")
print(f"Total          : ₹{total:.2f}")
print(f"Discount ({discount_rate}%) : ₹{discount:.2f}")
print(f"Amount after Disc. : ₹{amount_after_discount:.2f}")
print(f"GST (18%)          : ₹{gst:.2f}")
print("----------------------------")
print(f"Final Payable      : ₹{final_amount:.2f}")
print("===========================================================================")




# # Library Fine Calculator

# student_name = input("Enter student name: ")
# book_name = input("Enter book name: ")
# late_days = int(input("Enter number of late days: "))

# if late_days <= 0:
#     fine = 0
# elif late_days <= 5:
#     fine = late_days * 2
# elif late_days <= 10:
#     fine = late_days * 5
# else:
#     fine = late_days * 10

# print("============================================")
# print("          LIBRARY FINE")
# print("============================================")

# print(f"Student Name : {student_name}")
# print(f"Book Name    : {book_name}")
# print(f"Late Days    : {late_days}")
# print(f"Total Fine   : ₹{fine}")

# print("============================================")