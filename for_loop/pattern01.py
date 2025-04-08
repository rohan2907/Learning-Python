for i in range(1,6):
    for j in range(1,6):
        print("*", end='  ')
    print('')    

for i in range(1,6):
    for j in range(1,6):
        if i >= j:
           print("*", end='  ')
    print('')    

for i in range(1,6):
    for j in range(1,6):
        if i <= j :
           print("*", end='  ')
    print('')     

for i in range(1,6):
    print(" "*(i-1), end=' ')
    print("*"*(6-i))
          

      
          
         