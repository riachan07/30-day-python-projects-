import random
print("this is a virtual 6 face die")

while True:
    ask = input("you want to roll dice yes or no ").lower
    if ask == "yes":
        roll = random.randint(1, 6)
        print(f"🎲 You rolled: {roll}")
    elif ask == "no":
        print("okie bye")
        break
    else:
        print("please answer yes or no")
        continue

    
    if ask != "yes":
        print("okie bye")
        break 
