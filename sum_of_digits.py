# Need to find sum of all the digits of a number.

n = int(input("Enter a number: "))
sum = 0

while n > 0:
    r = n % 10
    sum = sum + r
    n = n // 10
print(f'Sum of digits: {sum}')
