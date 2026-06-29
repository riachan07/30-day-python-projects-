import random

print("this is a game of hangman")

lib = ["apple", "banana", "ipad", "bottle"]

word = random.choice(lib)

blank = ""

letter = []
lives=6

for i in range(len(word)):
    blank += "_ "

print(blank)

while True:
    guess = input("guess a letter: ")
    letter.append(guess)
    if guess not in word:
        lives -= 1
        print(f"❌ Wrong guess! Lives left: {lives}")
    
    display=""
    for char in word:
        if char in letter:
            display+=char + " "
        else:
            display+="_ "
            
    print (display)
    if lives == 0:
     print(f"💀 Game Over! The word was {word}")
     break
    if "_" not in display:
     print("🎉 You Win!")
     break
