def add(a,b):
    return a-b
def is_even(n):
    return n%2 == 0

def find_min(a,b,c):
    return min(a,b,c)

# print(add(3,6))
# print(is_even(22454))
# print(find_min(223,4656,2434))

a = int(input("enter a number a:"))
b = int(input("enter a number b:"))
c = int(input("enter a number c:"))
print(find_min(a, b, c))
print(is_even(b))
print(add(a,b))
