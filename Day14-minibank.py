print("This is a mini bank!")
print("enter a choice below")
history=[]
balance=1000
while True:
    choice=input("1. Check Balance 2. Deposit 3. Withdraw 4.  Transaction History 5.Exit ")
    if choice=="1":
        print(f"Your account balance is {balance}")
    elif choice=="2":
        dep=int(input("enter the amount you want to deposit "))
        amount= dep+balance
        balance= amount 
        print(f"your total amount now is {amount}")
        history.append(f"deposited is ₹{dep}")
    elif  choice=="3":
        wit=int(input("enter the amount you want to withdraw "))
        if wit > balance:
            print("❌ Insufficient balance")
        else:
            balance -= wit
            print(f"Your remaining balance is {balance}")
            history.append(f"withdrew ₹{wit}")

    elif choice == "4":
        print("====== Transaction History ======")

        if len(history) == 0:
            print("No transactions yet.")

        else:
            for transaction in history:
             print(transaction)
        
    elif  choice=="5":
        print("See you later!")
        break 

    
