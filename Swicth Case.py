# Define the operations
def addition(first_number, second_number):
    answer = first_number + second_number
    return answer


def subtraction(first_number, second_number):
    answer = first_number - second_number
    return answer


def multiplication(first_number, second_number):
    answer = first_number * second_number
    return answer


def division(first_number, second_number):
    answer = first_number / second_number
    return answer


# Function to perform switch-case
def switch(case):
    num_1 = float(input("Enter the first number: "))
    num_2 = float(input("Enter the second number: "))
    operations = [addition(num_1, num_2), subtraction(num_1, num_2),
                  multiplication(num_1, num_2), division(num_1, num_2)]
    index = int(case) - 1
    function = operations[index]
    return function


# Function to check whether the user choice is valid
def user_choice_check(expect, entered):
    temp_string = entered.lower()
    if 'exit' in temp_string:
        print("Program Terminated")
        exit()
        return 1
    elif entered in expect:
        return 1
    else:
        print("Invalid entry\nGive correct input: ")
        return 0


# Function to return the user choice to perform operation
def check_input():
    while 1:
        valid_inputs = ['1', '2', '3', '4']
        input_choice = str(input())
        if user_choice_check(valid_inputs, input_choice):
            break
    return input_choice


# Main Program
print("Below are the operations you can perform:- ")
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
print("Or type 'exit' to terminate the program")
print("\nEnter your choice:- ")
user_choice = check_input()
solution = switch(user_choice)
print("\nThe result is", solution)
