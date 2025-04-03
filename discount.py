amount = float(input("Enter the total amount: "))
if (amount <= 1000):
    final_amount = (amount - amount * 0.1)
elif (amount >= 1000 and amount <= 5000):
    final_amount = (amount - amount * 0.15)
elif (amount >= 5000 and amount <= 10000):
    final_amount = (amount - amount * 0.20)
else:
    final_amount = (amount - amount * 0.25)
print(f'Final amount after discount: {final_amount}')
   