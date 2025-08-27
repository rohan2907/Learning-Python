# create a function that generates a list of month names

import calendar
def month_generator():
    count = 1
    while True:
        yield calendar.month_name[count]
        count += 1
        if count > 12:
            break

m = month_generator()
print(list(m))
# Output: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
