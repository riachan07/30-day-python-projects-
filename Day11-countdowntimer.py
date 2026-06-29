import time 
print("This is a countdown")
seconds=int(input("enter countdown time in seconds: "))

print("Starting in...") 
for i in range (seconds,-1,-1):    
    hours=i // 3600
    minutes = i // 60
    remaining_seconds = i % 60
    
    print(f"{hours:02}:{minutes:02}:{remaining_seconds:02}")
    time.sleep(1)
print("⏰ Time's Up!")
