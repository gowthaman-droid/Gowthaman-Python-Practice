import winsound
password=""
while password!="12345":
    password=input("Enter  your password: ")
    if password!="12345":
        print("password is incorrect!!")
        for i in range(3):
            winsound.Beep(1000,500)

print("Login successfully")