#Indexing in tuple
person=("Parag",19,"Balaghat")
print(person[0])
print(person[-3])
print(person[1])
print(person[-2])
print(person[2])
print(person[-1])

#Write a function circle_stats(radius) that returns both the area and circumference 
# of a circle as a tuple (use math.pi). Unpack the result into two variables and print both.
import math
def circle_stats(radius):
      area = math.pi * (radius ** 2)

      circumference = 2 * math.pi * radius

      return area, circumference
area,circumference=circle_stats(8)

print("Area=",area)
print("Circumference=",circumference)


#3.
students=[("Riya", 87), ("Aman", 45), ("Parag", 92)]
for name,marks in students:
      print(name,"scored", marks)


# Write a function swap(a, b) that returns the two values swapped, 
# using tuple packing/unpacking. Call it with two numbers and two 
# strings. Then do the same swap in one line without a function 
# (Python allows this natively — try to figure out how)
def swap(a,b):
      return b,a
x,y=swap(10,20)
print("Swapped Numbers:",x,y)

#Strings
a,b=swap("Hello","Parag")
print("Swapped strings:",a,b)

#one-line swap
p=21
a=39
p,a=a,p
print("One line swap:",p,a)