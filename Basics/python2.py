#frequency of elements in a list
def frequency(lst):
    freq={}
    for i in lst:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq
 
    