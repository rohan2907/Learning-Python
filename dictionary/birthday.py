## Find the birthday of a person from the given dictionary

birthdays = {
    'sachin': '03/14/2003',
    'carl': '01/17/2001',
    'khan': '12/10/2005',
    'donald': '06/14/2012',
    'john': '01/06/2005'
}

name = input('Enter the name of the person: ')

if name in birthdays:
    print('Mr./Miss {} was born on {}'.format(name, birthdays[name]))
else:
    print('Name not found in the dictionary')

# for k,v in birthdays.items():
#     print(f'{k}:{v}')