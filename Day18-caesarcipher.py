print("This is caesar cipher app")
word=input("Enter a word: ")
print("You entered:", word)
encrypted_word=""
shift=3
for letter in word:
    old=ord(letter)-ord('a')
    num=ord(letter)
    
    num=num+shift
    new = (old + shift) % 26
    encrypted=chr(new + ord('a'))
    
    
    encrypted_word+=encrypted
    print("Encrypted word:", encrypted_word)
