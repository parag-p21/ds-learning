def even_numbers(limit):
    for num in range(0,limit+1,2):
     yield num

for value in even_numbers(20):
    print(value)
    
def fibonacci(n):
    a = 0
    b = 1
    for _ in range(n):  
        yield a
        a, b = b, a + b

for number in fibonacci(10):
    print(number)

total=sum(num ** 2 for num in range (1,100,2))
print(total)

