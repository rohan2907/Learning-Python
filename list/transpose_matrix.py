## Transpose of a matrix

l1 = [[1,2,3,4],[2,3,4,5],[6,7,8,9]]

l2 = []

for i in range(0,4):
    s = []
    for j in range(0,3):
        s.append(l1[j][i])
    l2.append(s)    

print(l2)    
