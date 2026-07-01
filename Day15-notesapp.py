#print("this is learning file handling")

print("this is notes app")

while True:
    choice = input("1. add note 2. view note 3. search note 4. exit ")

    if choice == "1":
        print("this is add note section")
        file = open("text.txt", "a")
        note = input("Enter your note: ").lower()
        file.write(note + "\n")
        file.close()
        
    elif choice == "2":
        print("this is view note section")
        file = open("text.txt", "r")
        print(file.read())

    elif choice == "3":
        print("this is search note section")
        file = open("text.txt", "r")
        search = input("Enter the note you want to search: ").lower()
        notes = file.readlines()
        for note in notes:
            if search in note:
                print("note found")
                print(note)

        
    elif choice == "4":
        print("exiting the app")
        file.close()
        break
