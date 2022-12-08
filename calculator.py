# Author: <Esther Wang>
# Assignment #2 - Calculator
# Date due: 2020-10-09
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.

def print_menu():
    """print welcome message and available calculator"""
    print("\n1) Perform addition")
    print("2) Perform subtraction")
    print("3) Perform multiplication")
    print("4) Perform division")

def do_addition():
    """inform user addition is chosen,sum 2 numbers, output result"""
    print("\nYou have chosen the addition operation.")
    number_1 = float(input("Enter first number: "))
    number_2 = float(input("Enter second number: "))
    result = number_1 + number_2
    print("The sum is ",result,".",sep="")

def do_subtraction():
    """inform user subtraction is chosen,find difference of 2 numbers, output result"""
    print("\nYou have chosen the subtraction operation.")
    number_1 = float(input("Enter first number: "))
    number_2 = float(input("Enter second number: "))
    result = number_1 - number_2
    print("The difference is ",result,".", sep="")

def do_multiplication():
    """inform user multiplication is selected, find product, output result"""
    print("\nYou have chosen the multiplication operation.")
    number_1 = float(input("Enter first number: "))
    number_2 = float(input("Enter second number: "))
    result = number_1 * number_2
    print("The product is ",result,".", sep="")

def do_division():
    """inform user division was chosen, fid result, output result"""
    print("\nYou have chosen the division operation.")
    number_1 = float(input("Enter first number: "))
    number_2 = float(input("Enter second number: "))
    result = number_1 / number_2
    print("The result of the division of the two numbers is ",result,".", sep="")

def do_calculation():
    """prompt user for calculation choice and calls function to perform calculation"""
    user_input = input("Please enter an option (1-4) or 'q' to quit: ")

    if user_input == "q":
        user_input = user_input

    if user_input == "1":
        do_addition()
    elif user_input == "2":
        do_subtraction()
    elif user_input == "3":
        do_multiplication()
    elif user_input == "4":
        do_division()
    elif user_input != "q":
        print("\nThat was not a valid choice. Try again.")

    return user_input

def run_calculator():
    """runs calculator as a repeated sequence of displaying calculator menu and performing user's choice of operation"""
    print("Welcome to the CS 1114 Calculator!")

    a = True
    while a:
        print_menu()
        b = do_calculation()
        if b == "q":
            print("\nGoodbye.")
            a = False


def main():
    """Runs a program for performing basic arithmetic
    operations between two numbers
    """
    run_calculator()

    
####### DO NOT REMOVE IF STATEMENT BELOW ########

if __name__ == '__main__':
    # Remove comments for next 4 lines to run doctests
    print("Running doctests...")
    import doctest
    doctest.testmod(verbose=True)

    print("\nRunning program...\n")

    main()
