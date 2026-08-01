product={
    "Name":"Books",
    "Price":799,
    "Category":"Education",
    "in_stock":True
}

print(product.get("Name"))
print(product.get("Price"))
print(product.get("Category"))
print(product.get("in_stock"))
#Not in Dict
print(product.get("Discount"),"Discount not available")

#Problem 1

students = {
    "Aman": {"Math": 80, "Science": 85},
    "Riya": {"Math": 75, "Science": 90},
    "Raj": {"Math": 88, "Science": 82}
}

for name, marks in students.items():
    print(f"{name}: Math={marks['Math']}, Science={marks['Science']}")



#problem 2

def invert_dict(d):
    inverted = {}
    for key, value in d.items():
        if value in inverted:
            inverted[value].append(key)
        else:
            inverted[value] = [key]
    return inverted
#provlem 3
def word_frequency(text):
    words = text.split()    # splits string into list of words
    frequency = {}
    
    for word in words:
        if word in frequency:
            frequency[word] += 1   # increment count
        else:
            frequency[word] = 1    # first time → set to 1
    
    return frequency

text = "the cat sat on the mat the cat"
print(word_frequency(text))





