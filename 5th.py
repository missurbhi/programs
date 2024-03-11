#leap year or not
year=int(input("Enter year to check leap year:"))
if year%4==0 and year%100!=0 or year%400==0:
    print(year,"is leap year")