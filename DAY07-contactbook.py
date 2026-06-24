print("this is  a contact book")
contacts={}
while True:
    print("====== CONTACT BOOK ======")
    choice=input(str("1. Add Contact 2. View Contacts 3  . Search Contact 4. Exit"))
    if choice=="1":
        print ("Add contact selected")
       
        name=input("enter name ")
        phone=input("enter phone number ")
        contacts[name]=phone
        print(f"the list is {contacts}")
    elif choice=="2":
        print("view contacts seletected")
        for contact in contacts:
            print(f"{contact} : {contacts[contact]}")
            
    elif choice=="3":
        print("search contact selected")
        name=input("enter name to be found")
        if name in contacts:
            contacts[name]
            print(f"{name} : {contacts[name]}")
        else:
            print("contact not found")
   
    elif choice =="4":
        print("okie")
        break
        
    else:
        print("invalid choice")
  
 
