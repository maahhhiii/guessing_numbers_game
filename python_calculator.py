def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Error: Cannot divide by zero.")
    return a / b

def get_number(prompt):
    """Validates and returns a numeric input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculator():
    current_value = None
    
    while True:
        print("\n--- Simple Calculator Menu ---")
        if current_value is not None:
            print(f"Current Value: {current_value}")
            print("1. Continue calculation with current value")
            print("2. Clear / Start new calculation")
            print("3. Exit")
        else:
            print("1. New Calculation")
            print("2. Exit")
            
        choice = input("Select an option: ").strip()
        
        if choice == '3' or (current_value is None and choice == '2'):
            print("Goodbye!")
            break
        elif choice == '2' and current_value is not None:
            current_value = None
            print("Calculator cleared.")
            continue
        elif choice == '1':
            if current_value is None:
                num1 = get_number("Enter the first number: ")
            else:
                num1 = current_value
                
            operator = input("Enter operator (+, -, *, /): ").strip()
            while operator not in ['+', '-', '*', '/']:
                print("Invalid operator.")
                operator = input("Enter operator (+, -, *, /): ").strip()
                
            num2 = get_number("Enter the second number: ")
            
            try:
                if operator == '+':
                    result = add(num1, num2)
                elif operator == '-':
                    result = subtract(num1, num2)
                elif operator == '*':
                    result = multiply(num1, num2)
                elif operator == '/':
                    result = divide(num1, num2)
                
                print(f"\nResult: {num1} {operator} {num2} = {result}")
                current_value = result  
                
            except ZeroDivisionError as e:
                print(e)

if __name__ == "__main__":
    calculator()
