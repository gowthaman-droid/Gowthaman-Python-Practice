a=list(map(int,input("Enter the values: ").split()))
t=int(input("Enter the target: "))
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==t:
            print(a[i],"+",a[j],"=",t)


