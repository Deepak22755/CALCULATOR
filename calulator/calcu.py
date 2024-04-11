from function import *

while True:
    print("what do you want to do")
    print("+ - Add")
    print("- - Subtract")
    print("* - Multiply")
    print("/ - Divide")
    print("Enter E to exit")
    
    option = input("choose an operation: ")
    if option == 'e' or option == 'E':
        break
    
    num1 = float(input("enter first number: "))
    num2 = float(input("enter second number: "))
    
    if option == '+':
        addition(num1,num2)
    elif option == '-':
        subtraction(num1,num2)
    elif option == '*':
        multiply(num1,num2)
    elif option == '/':
        division(num1,num2)
    else:
      print("invalid operation enetered")
    

