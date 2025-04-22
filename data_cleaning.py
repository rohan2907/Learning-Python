# Remove any special character present , string should have only alphabets and spaces

scan = 'These+notes^are#not//sufficient.'
clean = ''

for x in scan:
    if x.isalpha() or x.isspace():
        clean = clean + x
    else:
        clean = clean + ' '
print(clean)            