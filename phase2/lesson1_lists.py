#Slicing methods
numbers=[99,98,97,96,95,94]
print(numbers[-6])
print(numbers[-1])
print(numbers[2:4:1])


#Inserting and indexing 
fruits = ["apple", "banana", "mango"]
fruits.append("grapes")
fruits.insert(1,"orange")
fruits.remove("banana")
print(fruits)

#Sort,reverse
num=[18,45,7,18,21]
num.sort()
print(num)

num.reverse()
print(num)

num.count(18)
print(num.count(18))

#Functions with list
def list_stats(numbers):
 print("Largest number is:", max(numbers))
 print("Smallest number is:", min(numbers))
 print("Sum of numbers in list is :", sum(numbers))

nums1=[98,200,782,973]
list_stats(nums1)

#Mini challenge

def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:    # fill in the blank — has item been seen?
            result.append(item)
    return result
numbers=[1,3,2,3,1,4]
results=remove_duplicates(numbers)
print("Original List:",numbers)
print("List after removing duplicates:",results)
