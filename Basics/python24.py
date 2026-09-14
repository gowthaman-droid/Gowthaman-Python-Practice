s = input("Enter string: ")

found = False

for ch in s:
    if s.count(ch) == 1:
        print("First non-repeating character is:", ch)
        found = True
        break

if not found:
    print("None")