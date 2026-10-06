def calculator():
    while True:
        print("\n==============================")
        print("     INTERACTIVE CALCULATOR")
        print("==============================")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Km to Miles")
        print("6. Celsius to Fahrenheit")
        print("7. USD to INR")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        # Addition
        if choice == "1":
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print("Addition =", a + b)
            except ValueError:
                print("Please enter valid numbers.")

        # Subtraction
        elif choice == "2":
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print("Subtraction =", a - b)
            except ValueError:
                print("Please enter valid numbers.")

        # Multiplication
        elif choice == "3":
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print("Multiplication =", a * b)
            except ValueError:
                print("Please enter valid numbers.")

        # Division
        elif choice == "4":
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                if b == 0:
                    print("Cannot divide by zero.")
                else:
                    print("Division =", a / b)

            except ValueError:
                print("Please enter valid numbers.")

        # Km to Miles
        elif choice == "5":
            try:
                km = float(input("Enter kilometers: "))
                miles = km * 0.621371
                print("Miles =", round(miles, 2))
            except ValueError:
                print("Please enter a valid number.")

        # Celsius to Fahrenheit
        elif choice == "6":
            try:
                celsius = float(input("Enter Celsius: "))
                fahrenheit = (celsius * 9 / 5) + 32
                print("Fahrenheit =", round(fahrenheit, 2))
            except ValueError:
                print("Please enter a valid number.")

        # USD to INR
        elif choice == "7":
            try:
                usd = float(input("Enter USD amount: "))
                inr = usd * 83
                print("INR =", round(inr, 2))
            except ValueError:
                print("Please enter a valid amount.")

        # Exit
        elif choice == "8":
            print("Thank you for using Interactive Calculator!")
            break

        else:
            print("Invalid choice. Please select 1 to 8.")


calculator()