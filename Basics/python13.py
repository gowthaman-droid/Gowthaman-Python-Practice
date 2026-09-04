import random
import string
l=int(input("Enter the length of the password: "))
c=string.ascii_letters + string.digits + "!@#$%"
password=""
for i in range(l):
    password += random.choice(c)

print("Your Password: ",password)
print("Don't share")