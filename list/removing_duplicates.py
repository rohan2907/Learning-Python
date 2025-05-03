# Checking and removing if there is any duplicate in a list
## Method 1
l1 = [3,5,4,9,8,6,3,5,6,8,3,2,6,7,2,4,7,8,4,3,9]

l2 = []

for x in l1:
    if x not in l2:
        l2.append(x)

print(l2)  

#########################################################
## Method 2

l1 = list(set(l1))
print(l1)