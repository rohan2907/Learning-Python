# Print the Menu of a Restaurant which has different items and prices , calculate the number of dashes and show it in the proper alignment.

item1 = 'HotDog'
price1 = '$30'
item2 = 'Pizza'
price2 = '$100'
item3 = 'Pasta'
price3 = '$60'
item4 = 'Coffee'
price4 = '$40'

dash1 = 20 - len(item1) - len(price1)
dash2 = 20 - len(item2) - len(price2)
dash3 = 20 - len(item3) - len(price3)
dash4 = 20 - len(item4) - len(price4)

print(item1 + ('-'*dash1) + price1)
print(item2 + ('-'*dash2) + price2)
print(item3 + ('-'*dash3) + price3)
print(item4 + ('-'*dash4) + price4)
