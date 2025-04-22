# Input the credit card number of 16 digit and print the last 4 digits only of the card number
# rest digit should be marked and 'X'.

card_no = input("Enter the card no. ")
formated = ' '.join(card_no[i:i+4]
                    for i in range(0, len(card_no), 4))
print(formated)
last_4_digit = card_no[-4:]
four = 'X' * 4 + ' '
disp_no = four*3 + last_4_digit
print(disp_no)
