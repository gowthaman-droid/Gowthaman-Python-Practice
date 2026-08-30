import random
a=random.randint(1,100)
tries=0

while True:
    n=int(input("Guess the no:(1-100): "))
    tries+=1
    if n<a:
        print("Higher...")
    elif n>a:
        print("Lower...")

    elif n==a:
        print("correct Answer Wooooooh!!!" )
        break
    elif n==0:
        print("The Answer is ",a)
        break