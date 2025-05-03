# Find the number of occurance of each item

l1 = ['A','B','D','Y','O','E','Z','Z','A']

result = []

for x in l1:
    if x not in result:
        result.append(x)
        b = l1.count(x)
        result.append(b)

print(result)    