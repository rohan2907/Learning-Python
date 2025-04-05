# Count the number of digits 

n = int(input("Enter any number of your choice: "))
i = 0
while n > 0:
    i = i + 1
    n = n // 10
    
print(f'Number of Digits: {i}')    
