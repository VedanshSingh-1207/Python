def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select operation :-")
print("1. +")
print("2. -")
print("3. x")
print("4. /")

while True:

    choice = input("\n + | - | x | / : ")

    if choice in ('+', '-', 'x', '/'):
        num1 = float(input("\nEnter First Number : "))
        num2 = float(input("\nEnter Second Number : "))

        if choice == '+':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '-':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == 'x':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '/':
            print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Invalid Input")