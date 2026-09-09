password = input("Enter your password: ") 
length_ok = len(password) >= 8 
has_number = any(ch.isdigit() for ch in password) 
has_upper = any(ch.isupper() for ch in password) 
if length_ok and has_number and has_upper: 
    print("Valid Password !!!!") 
else: 
    print("Invalid Password!!!")     
    if not length_ok: 
        print("Must be at least 8 characters") 
    if not has_number: 
        print("Must contain at least 1 number") 
    if not has_upper: 
        print("Must contain at least 1 uppercase letter") 