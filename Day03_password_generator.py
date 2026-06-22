#password generator
import random
print("this is a password generator")
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
length = int(input("how long do you want your password to be? "))
password = ""
for i in range(length):
    password += random.choice(characters)
print(f"your password is: {password}")
