import sys

c = "Python"

print('Size of c = ', sys.getsizeof(c))
print('Type of c = ', type(c))

del c

if 'c' in locals():
    print("c is exist")
else:
    print("c is not exist")
