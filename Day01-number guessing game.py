import random
print("hello detective")

print("this is a number guessing game")

print("guess a number between 1 to 10")

secret_number= random.randint(1,10)

guess=int(input("guess a number detective: "))
count=0
while guess != secret_number:
    count += 1
    if guess < secret_number:
        print("number to low")
    else:
        print("number to high")
    guess = int(input("guess again detective: "))
if guess == secret_number:
    

  print ("you got the number right, its " + str(secret_number) + "!")
  print("it took you " + str(count) + " guesses.")
