n = int(input("Enter a number: "))

a = 0
b = 1

for i in range(0,n):
    c = b + a
    a = b
    b = c
print(a)    