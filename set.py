collections = {1,2,3,"Akshay", "rahul", 7564, 3, 3, 3, "Akshay"}
print(collections)
print(type(collections))  #set is a collection of unique elements
#   it does not maintain the order of elements and it is mutable.

dict = {}
print(type(dict))  # it is a dictionary not a set


set = set()
print(type(set))  # it is a set

set1 = {1,2,3,34}
set2 = {3,4,5,6}

print(set1.union(set2)) # it will give us the unique elements from both sets
print(set1.intersection(set2)) # it will give us the common elements from both sets
