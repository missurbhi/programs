i=int(input("Enter any number:"))
sum=0
x=i
power=len(str(i))
while i>0:
    rem=i%10
    sum=sum+rem**power
    i=i//10
if x==sum:
    print("number is armstrong")
else:
    print("number is not armstrong")