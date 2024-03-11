#factorial of number:
num=int(input("Enter number:"))
fact=1
for i in range(num,1,-1):
    fact=fact*i

print(fact)