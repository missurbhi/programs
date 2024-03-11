#logical operators
# a=int(input("Enter a number:"))
# if a>10 and a<20:
#     print(a," lies between 10 and 20")
# else:
#         print(a,"does not  lies between 10 and 20")

# b=90
# if b>10 or b>20:
#       print("true")
# else:
#       print("false")
a=10
if not (a%3==0 or a%5==0 ):
  print(a,"is not divisible by either 3 or 5")
else:
  print(a,"is divisible by 3 or 5")
