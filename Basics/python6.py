year=int(input("Enter the year to find it is leap year or not: "))
def leap(year):
    leap=False
    if year%400==0 or ( year%100!=0 and  year%4==0):
        return True       
    else:
        return False
r=leap(year)    
if r==True:
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")



