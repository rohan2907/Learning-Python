## Finding the word starting with given letter

l1 = ['apple','cat','dog','burger','pasta','noodle']

letter = str(input('Enter a letter: '))

for x in l1:
    if x.startswith(letter):
        print(x)
