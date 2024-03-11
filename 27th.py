li1=[]
li2=[]
n=int(input("Enter n:"))
num=int(input("Enter number to divide the list:"))
for i in range(0,n):
  num=int(input("Enter number:"))
  li1.append(num)
 
print(li1)

for i in range (0,n):
    if li1[i]%num==0:
     li2.append(li1[i])

print(li2)