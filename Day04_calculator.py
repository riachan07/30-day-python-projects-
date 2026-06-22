print("this is a calculator")
x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
choice=input("enter an operator")
def addition(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    return x/y  

if choice=="+":
 result=addition(x,y)
 print(result)
 
if choice=="-":
   result= subtraction(x,y)
   print(result)

if choice=="*":
   result= multiplication(x,y)
   print(result)

if choice=="/":
    result = division(x,y)
    print(result)
