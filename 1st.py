x=int(input("Enter x:"))
y=int(input("Enter y:"))
ch=int(input("Enter 1 for + , 2 for -,3 for multiply,4 for division ,5 for mode :"))

if ch==1:
 print("Addition:",x+y)
elif ch==2:
 print("Substraction:",x-y)
elif ch==3:
 print("Multiplication:",x*y)
elif ch==4:
 print("Division:",x/y)
elif ch==5:
 print("Modulus:",x%y)
else:
 print("Enter valid choice")