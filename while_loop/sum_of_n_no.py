# Summation of 5 numbers based on user input

n = 5
sum = 0
i = 0
print(f'Enter {n} Numbers')
while i < n:
    i = i + 1
    x = int(input())
    sum = sum + x
print(f'Sum of numbers: {sum}')