
for i in range(1,5):
    for j in range(1,i+1):
        print("*",end="")
     
    print("")

for i in range(5,0,-1):
    for j in range(1,i+1):
        print("*",end=" " )
    print("")

for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print("")

for i in range(1,5):
    for space in range(4,i,-1):
       print(" ", end="")
    for j in range(0,(2*i-1)):
        print("*", end="")
    print(" ")