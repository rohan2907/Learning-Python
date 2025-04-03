# year = int(input('Enter Year: '))

# if year % 4 == 0:
#     print('Leap Year')
# elif year % 100 == 0 and year % 400 == 0:
#     print('Leap Year')
# else:
#     print('Non Leap Year')  


year = int(input('Enter year'))

if year % 100 == 0:
    if year % 400 == 0:
        print('Leap Year')
    else:
        print('Not a Leap Year')
elif year % 4 == 0:
    print('Leap Year')
else:
    print('Not a Leap Year')