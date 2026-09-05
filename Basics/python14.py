def abs_diff():
    a=int(input("Enter 'A' value: "))
    b=int(input("Enter 'B' value: "))
    sum=a+b
    c= a*a + b*b
    abs=c-sum
    result=abs
    return result
print(abs_diff())

def abs_diff(a,b):
    total_sum=a+b
    sum_of_square=a**2 + b**2
    return abs(total_sum - sum_of_square)
a=int(input(""))
b=int(input(""))
print(abs_diff(a,b))
