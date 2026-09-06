#1. Write a function safe_divide(a, b) that returns the result of division, 
# but catches ZeroDivisionError and returns "Cannot divide by zero" instead.
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"


print(safe_divide(10, 2))  # 5.0
print(safe_divide(10, 0))  # Cannot divide by zero

#2. Given scores = {"Riya": 87, "Aman": 45, "Parag": 92}, write a one-line dict 
# comprehension that keeps only students scoring above 60.
scores = {"Jiya": 87, "Aman": 45, "Parag": 92}
result = {name: score for name, score in scores.items() if score > 60}
print(result)

#3. What's the difference between return and yield? Give one real use case for yield.



#Write a lambda that takes a number and returns True if it's divisible by both 3 and 7.
check = lambda n: n % 3 == 0 and n % 7 == 0
print(check(21))  # True
print(check(15))  # False

#5. You have data = [12, 15, 12, 18, 20, 12, 25]. Write code to find the mean, median, and mode using 
#functions you built in Phase 3 (or rewrite them quickly).
data = [12, 15, 12, 18, 20, 12, 25]

def mean(data):
    return sum(data) / len(data)

def median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    
    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2

def mode(data):
    return max(set(data), key=data.count)


print("Mean:", mean(data))
print("Median:", median(data))
print("Mode:", mode(data))

# #Write a custom exception class NegativeValueError and a function check_positive(n) that raises it if n < 0.
# class NegativeValueError(Exception):
#     pass

# def check_positive(n):
#     if n < 0:
#         raise NegativeValueError("Value cannot be negative")
#     return n


# print(check_positive(10))   # 10
# print(check_positive(-5))   # NegativeValueError


# #
def dot_product(v1, v2):
    return sum(v1[i] * v2[i] for i in range(len(v1)))

weights=[0.5, 0.5] 
features=[80, 90]
score = dot_product(weights, features)
print(score)