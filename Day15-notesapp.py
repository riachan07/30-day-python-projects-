
#print("this is learning file handling")
print("this is notes app")
while True:
 choice=input("1. add note 2. view note 3. exit ")
 if choice=="1":
  print("this is add note section")
  file=open("text.txt","a")
  note=input("Enter your note: ")
  file.write(note + "\n")
  
 elif choice=="2":
   print("this is view note section")
   file=open("text.txt","r")
   print(file.read())
   notes = file.readlines()
   for note in notes:
     print(note)
