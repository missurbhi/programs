#add items of numeric list:
sum=0
n=int(input("Enter no of element:"))
li=[]
for i in range(0,n):
    val=int(input("Enter element:"))
    li.append(val)
print(li)
for i in range(0,n):
    sum=sum+li[i]
print("sum=",sum)