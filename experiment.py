# Functions for calculations
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def get_user_input(message, is_numeric=True):
    while True:
        try:
            user_input = input(message)
            if is_numeric:
                user_input = float(user_input)
            return user_input
        except ValueError:
            print("Please only enter numerical digits.")

def confirm_input(prompt, value):
    while True:
        confirmation = input(f"{prompt} {value}, correct? (Yes/No): ")
        if confirmation.lower() == 'yes':
            return True
        elif confirmation.lower() == 'no':
            return False
        else:
            print("Invalid input.")

def calculator():
    while True:
        response = input("Do you want to use the calculator? (Yes/No): ")
        if response.lower() == 'no':
            print("Maybe later...")
            return

        if response.lower() == 'yes':
            while True:
                num1 = get_user_input("Enter first number: ")
                if confirm_input("Is", num1):
                    break
                print("Redoing input...")

            operations = {
                '1': ("Addition", add),
                '2': ("Subtraction", sub),
                '3': ("Multiplication", mul),
                '4': ("Division", div)
            }

            while True:
                print("1. Addition(+)")
                print("2. Subtraction(-)")
                print("3. Multiplication(*)")
                print("4. Division(/)")
                oper = input("Enter your operation (1/2/3/4): ")

                if oper in operations:
                    operation_name, operation_function = operations[oper]
                    if confirm_input(f"The operation is \"{operation_name}\"", operation_name):
                        break
                    print("Redoing input...")
                else:
                    print("Invalid input.")

            while True:
                num2 = get_user_input("Enter second number: ")
                if oper == '4' and num2 == 0:
                    print("Cannot divide by zero")
                elif confirm_input("Is", num2):
                    break
                else:
                    print("Redoing input...")

            result = operation_function(num1, num2)
            print(f"{num1} {operations[oper][0]} {num2} =", result)

            redo = input("Do another calculation? (Yes/No): ")
            if redo.lower() == 'no':
                print("Exiting Calculator.")
                return
            elif redo.lower() != 'yes':
                print("Invalid input.")

calculator()
