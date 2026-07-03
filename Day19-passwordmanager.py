import random
import string 
print("This is password generator app")
letters=int(input("Enter the number of letters you want in your password: "))
numbers=int(input("Enter the number of numbers you want in your password: "))
symbols=int(input("Enter the number of symbols you want in your password: "))
#print(string.ascii_letters)
#print(string.digits)
#print(string.punctuation)
password=[]
for i in range(letters):
    password.append(random.choice(string.ascii_letters))
for i in range(numbers):
    password.append(random.choice(string.digits))
for i in range(symbols):
    password.append(random.choice(string.punctuation))
print("Your password is: ", password)


random.shuffle(password)
print("Your password is: ", ''.join(password))
