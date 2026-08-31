import time
import winsound
seconds= int(input("Enter the alarm time in sec: "))
time.sleep(seconds)
for i in range(10):
    winsound.Beep(1000,500)
