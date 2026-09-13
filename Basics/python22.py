name="gowtham"
password="472572"

tr=0
max=3
while tr<max:
    n=input("Enter Your name: ")
    p=input("Enter your password: ")
    if name==n and password==p:
        print("Login Successful !")
        break
    else:
        tr+=1
        print("Worng password!!")
        print("Tries left: ",max - tr)

if tr==max:
    print("Account Blocked !!!")