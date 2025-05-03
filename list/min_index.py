## Minimum index sum of 2 list, we have to find out what they should order that is fav to both of them depending on minimum index

fav1 = ['pizza','nuggets','hotdog','noodles','pasta','burger']
fav2 = ['burger','hotdog','noodles','pasta','nuggets','pizza']

index1 = 10
index2 = 10

for i in range(len(fav1)):
    indx = fav2.index(fav1[i])

    if i + indx < index1 + index2:
        index1 = i
        index2 = indx

print(fav1[index1], index1 + index2)        
