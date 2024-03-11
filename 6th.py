#prime number or not
num=int(input("Enter number:"))
for i in range (2,num,1):
 if num%i==0:
  print(num,"is not a prime number")
 else:
  print(num,"is a prime number")
  break