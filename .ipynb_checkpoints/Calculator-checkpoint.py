def add(a, b):
    return a+b
def subtract(a, b):
    return a-b
def multiply(a, b):
    return a*b
def divide(a, b):
    if b==0:
        return "Error! Cannot divide by zero."
    return a/b

while True:
    print("\n CALCULATOR")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")
    if choice == "5":
        print("Thank You")
        break

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == "1":
        print(add(num1,num2))
    elif choice == "2":
        print(subtract(num1,num2))
    elif choice == "3":
        print(multiply(num1,num2))
    elif choice == "4":
        print(divide(num1,num2))
    else:
        print("Invalid Choice")
        break