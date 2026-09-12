n=int(input("Enter n: "))
a=list(map(int,input("Enter elements: ").split()))
l=0
st=0
for num in a:
    if num-1 not in a:
        current=num
        length=1
        while current+1 in a:
            current+=1
            lenght+=1

        if length>l:
            l=length
            st=num

print("Longest con- seq--: ",l)
print("Sequence: ",end="")
for i in range(st,st+l):
    print(i,end="")