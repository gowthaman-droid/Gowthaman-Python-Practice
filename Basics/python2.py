a = list(map(int, input("Enter the values: ").split()))
freq={}
for i in a:
    freq[i]=freq.get(i,0)+1

for i,count in freq.items():
    print(f"{i} : {count}")
print(a)