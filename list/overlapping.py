## overlapping elements of 2 lists

l1 = [10,12,6,8,48,66,9,3,5]

l2 = [8,5,6,7,3,10,4,66]

l3 = []

for x in l1:
    if x in l2:
        l3.append(x)

print(l3)        