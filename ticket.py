print('Welcome to the RollerCoster!!')
height = int(input("What is your height in cms? "))
bill = 0
if height >= 120:
    print('Allowed to Ride')
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print('Children ticket is of $5')
    elif age < 18:
        bill = 7
        print('Youth tickets is of $7')
    else:
        bill = 12
        print('Adult ticket is of $12')
    want_photo = input('Do you want photos? Press "y" for Yes and "n" for No  ')
    if want_photo == "y":
        bill += 3
    print(f"Total bill is ${bill}")  
else:
    print('Can Not Ride')    
