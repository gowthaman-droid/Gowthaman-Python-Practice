
a=[]
for i in range(5):
    n=int(input("Enter ur score: "))
    a.append(n)
total = sum(a)
n=5
avg=total/n
if avg>=90:
    print("Grade A")
elif avg>=75:
    print("Grade B")
elif avg>=60:
    print("Grade C")
elif avg>=50:
    print("Grade D")
elif avg>=40:
    print("Fail")
print("Total:", total)
print("Average:", avg)