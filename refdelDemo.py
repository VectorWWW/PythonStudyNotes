from sys import getrefcount

# a = [1, 2, 3]
# b = a
# print(getrefcount(b))
# del a
# print(getrefcount(b))

# a = [1,2,3]
# del a[0]
# print(a)

a = [1, 2, 3]
b = a
print(getrefcount(b))
a = 1
print(getrefcount(b))