queue=[]
print("\nWelcome....\nPress 1 to join: \nPress 2 to leave guild: \npress 3 know to position: \npress 4 to see the members: \npress 5 to exit the system.")
while True:
    ch=int(input("Enter your Choice: "))
    if ch==1:
        name=input("Enter Name: ")
        queue.append(name)
        print('Joined successfully')
    elif ch==2:
        name=input('Enter Name:')
        queue.remove(name)
    elif ch==3:
        name=input('Enter Name:')
        for i in range(len(queue)):
            if queue[i]==name:
                print('Position:',i)
            else:
                print(f'{name} left the guild')
    elif ch==4:
        print('Members:',queue)
    elif ch==5:
        print('Exiting...')
        break
    else:
        print('Invalid Choice')