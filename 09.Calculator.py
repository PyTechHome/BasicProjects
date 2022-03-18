#This is a simple calculator coded in python
import os
os.system('cls' if os.name=='nt' else 'clear')
userFirstnumber=int(input("Enter the first number: "))
userSecondnumber=int(input("Enter the second number: "))
result=0
userOperation=input("Enter what you want to do:\nA for Addition, \nS for Subtraction, \nM for Multiplication, \nD for Division: ")
if userOperation.upper()=='A':
    result=userFirstnumber+userSecondnumber
    print(f"The sum of numbers is {result}")
elif userOperation.upper()=='S':
    result=userFirstnumber-userSecondnumber
    print(f"The subtraction of numbers is {result}")
elif userOperation.upper()=='M':
    result=userFirstnumber*userSecondnumber
    print(f"The multiplication of numbers is {result}")
elif userOperation.upper()=='D':
    result=userFirstnumber/userSecondnumber
    print(f"The division of numbers is {result}")
else:
    print("Operation invalid")

