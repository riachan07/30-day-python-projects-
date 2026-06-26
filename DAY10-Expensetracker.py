print("This is an expense tracker!")
expense={}
while True:
    
    choice=input("1.Add expense 2.View expense 3.Total expense 4.Exit ")
    if choice=="1":
        print("Add expense")
        item=input("add the item ")
        amount = int(input("add the amount of item "))
        expense[item]=amount
        print("Expense Added Successfully!")

    elif choice=="2":
        
        print("------ Expenses ------")

        for item in expense:
         print(f"{item}:₹{expense[item]}")
         
        print("----------------------")

    elif choice=="3":
        print("total expenses")
        result=sum(expense.values())
        print(f"Total Expense: ₹{result}")
    elif choice=="4":
     print("okay bye")
     break
    else:
     print("Invalid choice! Please try again.")
     
     
