i=int(input("Enter any number:"))
x=i
rev=0
while i>0:
    rem=i%10
    rev=(rev*10)+rem
    i=i//10

if x==rev:
    print("number is palindrom")
else:
    print("number is not palindrom")