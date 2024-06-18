def add(x, y): #1
    return x + y

def subtract(x, y):  #2
    return x - y

def multiply(x, y): #3
    return x * y

def divide(x, y): #4
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def percentage(x, percent): #5
    return (x * percent) / 100

def gcd(a, b): #6
    while b:
        a, b = b, a % b
    return a

def lcm(a, b): #7
    return (a * b) // gcd(a, b)

def main():
    print("Welcome to the Enhanced Calculator!")
    while True:
        print("\nOptions:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Percentage")
        print("6. GCD")
        print("7, LCM")
        print("8. Exit")
        choice = input("Enter your choice (1/2/3/4/5/6/7/8): ")

        if choice == '8':
            print("Exiting the calculator. Goodbye!")
            break

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"Result: {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {divide(num1, num2)}")
        elif choice == '5':
            percent = float(input("Enter percentage: "))
            print(f"{percent}% of {num1} is {percentage(num1, percent)}")
        elif choice == '6':
            print(f"GCD of {num1} and {num2} is {gcd(int(num1), int(num2))}")
        elif choice == '7':
            print(f"LCD of {num1} and {num2} is {lcm(int(num1), int(num2))}")
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
    print("Thank You")
