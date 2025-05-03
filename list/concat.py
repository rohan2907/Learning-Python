## Concatenate all integer from a list to a single number

l1 = [2,5,2,3,2,5,5,7,8,9]

l2 = ''.join(map(str, l1))

print(l2)

####################################
# Method 2

s1 = ''

for x in l1:
    s1 = s1 + str(x)
print(int(s1))    
    