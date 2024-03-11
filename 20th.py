n=int(input("Enter no of element:"))
li=[]
for i in range(0,n):
    val=int(input("Enter element:"))
    li.append(val)
print(li)
so=li.sort()
print(so)

print("min=",so[0])
print("max=",so[n-1])