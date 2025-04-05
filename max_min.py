# Find the maximum number & minimum number

n = 5
print(f'Enter {n} Numbers')
i = 0
max = float('-inf')
min = float('inf')
while i < n:
    x = int(input())
    i = i + 1 
    if x > max:
        max = x
    elif x < min:
        min = x   
       
print(f'max no. is: {max}')
print(f'min no. is: {min}')

