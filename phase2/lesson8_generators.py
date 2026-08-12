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

def read_students(filepath):
    with open(filepath, "r") as file:
        next(file)  # skip header
        
        for line in file:
            name, marks, grade = line.strip().split(",")
            
            yield {
                "name": name,
                "marks": int(marks),
                "grade": grade
            }


# 1️⃣ Print all students
print("All Students:")
for student in read_students("students.txt"):
    print(student)


# 2️⃣ Print only Grade A students
print("\nGrade A Students:")
for student in read_students("students.txt"):
    if student["grade"] == "A":
        print(student)


# 3️⃣ Calculate average marks using generator expression
marks_gen = (student["marks"] for student in read_students("students.txt"))

total = sum(marks_gen)
count = sum(1 for _ in read_students("students.txt"))

average = total / count
print("\nAverage Marks:", average)