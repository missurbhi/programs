#palindrom number between 500 and 1000
rev=0
for i in range(500,1000):
    x=i
    rem=x%10
    rev=rev*10+rem
    x=x//10
    if i==rev:
     print(i)