## Adding 2 Matrix

l1 = [[1,2,3,4],[2,3,4,5],[6,7,8,9]]
l2 = [[2,3,4,5],[3,4,5,6],[4,5,7,8]]

l3 = []

for i in range(0,3):
    s = []
    for j in range(0,4):
        r = l1[i][j] + l2[i][j]
        s.append(r)
    l3.append(s)    

print(l3)
 