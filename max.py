# Find the maximum number

n = 5
print(f'Enter {n} Numbers')
i = 0
max = 0

while i < n:
    x = int(input())
    i = i + 1 
    if x > max:
       max = x
       
print(f'max no. is: {max}')

