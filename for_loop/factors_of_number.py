## Find the factors of a number and also tell if the number is a prime number or not.

n = int(input("Enter a number: "))
count = 0
for i in range(1,n+1):
    if (n % i) == 0:
        print(i)
        count = count + 1
if count == 2:
    print("It is a prime number")
else:
    print("It is not a prime number")  
        
    
        
        