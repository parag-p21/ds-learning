#OPerations in Sets
batch_a = {"Alice", "Bob", "Charlie", "David"}
batch_b = {"Charlie", "David", "Eve", "Frank"}

print("Students in both batches",batch_a&batch_b)
print("Students only in batch a",batch_a - batch_b)
print("Students in either batch",batch_a|batch_b)
print("Students exactly in one batch",batch_a^batch_b)


#Unique values 
Num=[1,2,3,2,4,3,5,1,6]
unique_numbers=set(Num)
print(sorted(set(Num)))    # [1, 2, 3, 4, 5, 6] as a list
print(unique_numbers)

#Defining a function

def common_elements(list1,list2):
    
    return list(set(list1) & set(list2))

L1=[1,2,3,4,5]
L2=[3,4,5,6,7]
Intersection=common_elements(L1,L2)
print(Intersection)

#Mini challenge
premium_customers = [101, 205, 303, 101, 404, 205]
active_customers = [205, 303, 505, 606, 101]

premium_set = set(premium_customers)
active_set = set(active_customers)

premium_and_active = premium_set & active_set

premium_not_active = premium_set - active_set

all_unique_customers = premium_set | active_set

print("Premium & Active:", premium_and_active)
print("Premium NOT Active:", premium_not_active)
print("All Unique Customers:", all_unique_customers)