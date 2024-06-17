# Building a simple calculator for Portfolio


# Addition
def add(x, y):
    return x + y

# Subtraction
def subtract(x, y):
    return x - y

# Multiplication
def multiply(x, y):
    return x * y

# Division
def divide(x, y):
    return x / y

# Modulo
def modulus(x, y):
    return x % y

print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")

while True:
    # take input from the user
    operation =  input("Enter one operation(1 or add, 2 or subtract, 3 or multiply, 4 or divide, 5 or modulus,): ")

    # check if choice is one of the four options
    if operation in ('1', '2', '3', '4', '5', "add", "subtract", "multiply", "divide", "modulus"):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if (operation == '1' or operation == "add"):
            print(num1, "+" , num2, "=", add(num1, num2))
    
        elif (operation == '2' or operation == "subtract"):
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif (operation == '3' or operation == "multiply"):
            print(num1, "*", num2, "=", multiply(num1, num2)) 

        elif (operation == '4' or operation == "divide"):
            print(num1, "/", num2, "=", divide(num1, num2))

        elif (operation == '5' or operation == "modulus"):
            print(num1, "%", num2, "=", divide(num1, num2))


        # Check if the User wants another calculation
        next_calculation = input("Let's do next calculation? (yes/no): ")    
    
        # break the while loop if answer is no
        if next_calculation == "no":
            break
    else:
        print("Invalid Input")