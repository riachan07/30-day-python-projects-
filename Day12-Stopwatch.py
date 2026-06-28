import time 
print("⏱️ Stopwatch")
while True:
 countdown=input("Press Enter to start...")
 start=time.time()
 stop=input("Press Enter to stop...")
 end = time.time()
 elapsed = end - start
 minutes = int(elapsed // 60)
 seconds = int(elapsed % 60)
 print(f"{minutes:02}:{seconds:02}")
 
 again=input("do you wanna count again?yes or no ")
 if again=="no":
        print("okay bye")
        break 
