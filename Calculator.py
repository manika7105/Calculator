print("\n==========Calculator==========")

def calculator():
    num1 = float(input("\nEnter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif choice == '2':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif choice == '3':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif choice == '4':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid input!")

while True:
    print("\nSelect an option:")
    print("1. Calculate")
    print("2. Quit")

    main_choice = input("Enter choice (1/2): ")

    if main_choice == '1':
        calculator()
    elif main_choice == '2':
        print("Exiting calculator...")
        break
    else:
        print("Invalid main menu input.")