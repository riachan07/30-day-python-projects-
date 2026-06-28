print("This is a Quiz Game!")

questions = [
    {
        "question": "Capital of India?",
        "answer": "delhi"  
    },
    {
        "question": "Capital of Russia?",
        "answer": "moscow"
    },
    {
        "question":"Capital of China?",
        "answer": "beijing"  
    }
]

score = 0

for q in questions:
    print(q["question"])

    user_answer = input("Your answer: ").lower()

    if user_answer == q["answer"]:
        print("Correct!")
        score += 1

    else:
        print("Wrong!")

print(f"Your score is {score}/{len(questions)}")

if score==len(questions):
    print("PERFECT SCOREEE!!")
elif score >=2:
    print("good going!")
else:
    print("keep practicing!")
