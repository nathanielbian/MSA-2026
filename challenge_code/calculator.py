import sys

def is_int(value):
    try:
        int(str(value))
        return True
    except ValueError:
        return False
    
def is_digit(value):
    if is_int(value) and 0 <= value <= 9:
        return True
    
    return False

def format_number(value):
    formatted_value = f"{value:.10g}"

    if is_int(value):
        return int(formatted_value)
    
    return float(formatted_value)

def add(value_1, value_2):
    return format_number(value_1 + value_2)

def subtract(value_1, value_2):
    return format_number(value_1 - value_2)

def multiply(value_1, value_2):
    return format_number(value_1 * value_2)

def divide(value_1, value_2):
    return format_number(value_1 / value_2)

def exponentiate(value_1, value_2):
    return format_number(value_1 ^ value_2)

def factorial(value):
    if not is_int(value) or value < 0:
        return -1
    
    if value == 1 or value == 0:
        return 1

    return value * factorial(value - 1)

def exit():
    sys.exit(0)

def help():
    print("Commands:")
    print("exit - Exit the program")
    print("help - Get help")

def interpret_expression(user_input):
    user_input = user_input.replace(" ", "")
    print(user_input)

def get_user_input():
    valid_commands = {"exit", "help"}

    user_input = input(">> ")

    if user_input in valid_commands:
        globals()[user_input]()
    else:
        interpret_expression(user_input)

def main():
    print(add(5645645, 3453453.54))
    print(factorial(4.5))

    print("Welcome to the Calculator!")
    print("--------------------------")
    print("Use \"help\" for help.")

    while True:
        get_user_input()

main()
