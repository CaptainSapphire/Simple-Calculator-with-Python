## imports 
import os # clean outputs
import sys # exiting the program
import time # delay outputs (just looks nice)
import math # calculations


## Calculator Project
print("Welcome to the calculator!") 
print("Type pi for the value of pi (3.14159...), e for the value of e (2.71828...)")# implement later

def pifunction():
    return math.pi;

def efunction():
    return math.e;

choice = ""
while choice != "0":
    choice = input("What operations would you like? \n1: +,-,/,*, ** \n2: trig functions \n3: log, exponential functions \n0: exit ")

    ## simple operations
    if choice == "1":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if (num1 == "pi"):
            num1 = pifunction()
        elif (num1 == "e"):
            num1 = efunction()

        if (num2 == "pi"):
            num2 = pifunction()
        elif (num2 == "e"):
            num2 = efunction()

        operation = input("Enter the operation (+, -, *, /, **): ")
        time.sleep(1)
        
        if operation == "+":
            result = num1 + num2
            operation = "plus"
        elif operation == "-":
            result = num1 - num2
            operation = "minus"
        elif operation == "*":
            result = num1 * num2
            operation = "multiplied by"
        elif operation == "**":  
            result = num1 ** num2
            operation = "to the power of"
        elif operation == "/":
            operation = "divided by"
            if num2 != 0:
                result = num1 / num2
            else:
                print("Divide by zero error. :/")
                sys.exit()
        
        else:
            print("Invalid operation!!")
            sys.exit()
        time.sleep(2)
        print(f"The output of {num1} {operation} {num2} is: {result}")
        time.sleep(5)

    os.system('cls')

    ## Trig Functions
    if choice == "2":
        num = float(input("Enter the number (in degrees): ")) # add option for radians later
        if (num == "pi"):
            num = pifunction()
        elif (num == "e"):
            num = efunction()

        operation = input("Enter the operation (sin, cos, tan): ")
        time.sleep(1)
        
        if operation == "sin":
            result = math.sin(math.radians(num))
        elif operation == "cos":
            result = math.cos(math.radians(num))
        elif operation == "tan":
            result = math.tan(math.radians(num))
        else:
            print("Invalid operation!!")
            sys.exit()
        time.sleep(2)
        print(f"The output of {operation}({num}) is: {result}")


    ## log and exponential functions
    if choice == "3":
        num = float(input("Enter the number: "))
        if (num == "pi"):
            num = pifunction()
        elif (num == "e"):
            num = efunction()
        operation = input("Enter the operation (log, exp): ")
        time.sleep(1)
        
        if operation == "log":
            if num > 0:
                result = math.log(num)
            else:
                print("Math domain error. Logarithm undefined for negative numbers.")
                sys.exit()
        elif operation == "exp":
            result = math.exp(num)
        else:
            print("Invalid operation!!")
            sys.exit()
        time.sleep(2)
        print(f"The output of {operation}({num}) is: {result}")

os.system('cls')
