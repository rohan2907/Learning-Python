# Write a code for reversing the number.

n = int(input("Enter a number: "))

rev = 0

while n > 0:
    r = n % 10
    rev = (rev * 10) + r
    n = n // 10
print(f'Reverse of a number is: {rev}')    