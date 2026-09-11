cards=[5,2,4,7,9,7]
freq={}
for i in cards:
    freq[i]=freq.get(i,0)+1

print(freq)