print("This is student grade app")

print("====== STUDENT GRADE MANAGER ======")

student = {}

while True:
    choice = input("1. Add Student 2. View Students 3. Search Student 4. Calculate Average 5. Exit ")

    if choice == "1":
        print("This is add student section")

        file = open("gpa.txt", "a")

        note = input("Enter student name: ")
        number = input("Enter student grade: ")

        student[note] = number

        file.write(note + "," + number + "\n")

        file.close()

    elif choice == "2":
        print("This is view student section")

        file = open("gpa.txt", "r")

        print(file.read())

        file.close()          

        
        for note in student:
            print(f"{note}: {student[note]}")

    elif choice == "3":
        print("This is search student section")

        file = open("gpa.txt", "r")

        search = input("Enter the student name you want to search: ").lower()

        notes = file.readlines()

        found = False        

        for note in notes:
            if search in note.lower():    
                print("Student found!")
                print(note)
                found = True

        if not found:         
            print("Student not found.")

        file.close()          

    elif choice == "4":
        print("This is calculate average section")

        file = open("gpa.txt", "r")

        notes = file.readlines()

        total = 0
        count = 0

        for note in notes:
            total += float(note.split(",")[1])
            count += 1

        if count > 0:         
            average = total / count
            print("Average grade:", average)
        else:
            print("No student records found.")

        file.close()          

    elif choice == "5":
        print("Exiting the app")
        break                 

    else:
        print("Invalid choice.")
