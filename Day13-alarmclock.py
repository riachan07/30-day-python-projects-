from datetime import datetime
import time
import winsound
print("⏰ Alarm Clock")

alarm = input("Enter alarm time (HH:MM): ")

while True:

    now = datetime.now()

    current = now.strftime("%H:%M:%S")

    print(current)

    if current == alarm:
        print("⏰ WAKE UP!!")
        for alarm in range (5):
            print(winsound.Beep(1000, 500))
         
        break

    time.sleep(1)
