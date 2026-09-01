import winsound
seat=100
booking=True
while booking:
    c=input("Do you want to book seats?(yes/no): ")
    winsound.Beep(1000,500)
    if c.lower()=="yes":
        a=int(input("Enter the number of seats you want to book: "))
        if a<=seat:
            seat=seat-a
            print("Booking successfull...")
            winsound.Beep(1000,500)
            print("Remaining Seats: ",seat)
            winsound.Beep(1000,500)
        else:
            print("Sorry! Seats Remaining: ",seat)
            for i in range(2):
                winsound.Beep(1000,500)    
    else:
        booking=False

print("Thank you for visting!!!")
winsound.Beep(1000,500)
         