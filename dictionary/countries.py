## Create a dictionary for country names in alphabetically order

# countries = {
#     'A': ['America' , 'Alaska' , 'Argentina'],
#     'B': ['Bhutan' , 'Brazil' , 'Bahrain'],
#     'C': ['China' , 'Costa Rica' , 'Cuba']
# }

countries = {}

for i in range(4):
    name = input('Enter the country name:')
    if name[0].upper() not in countries:
        countries[name[0].upper()] = [name]
    else:
        countries[name[0].upper()].append(name)
print(countries)        
            