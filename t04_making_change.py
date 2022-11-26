######################################################################
# Author: Jan Pearce and Patrick Shepherd   TODO: Change this to your names
# Username: pearcej & shepherdp             TODO: Change this to your usernames
#
# Assignment: T04: Unit Testing
#
# Purpose: Demonstrates the use of division and modulus operations.
#
# This program INCORRECTLY calculates the largest number of
# quarters, dimes, nickels and pennies needed to make that change in coins.
# It is designed to show a subtle error and the value of unit tests.
#
######################################################################
# Acknowledgements:
#   Original Author: Dr. Jan Pearce
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import sys

TESTNUM = 1

def mytest( did_pass ):
    """
    Print the result of a unit test.

    This function works correctly--it is verbatim from the textbook, Chapter 6.

    You should reuse this function anytime you are creating a custom test suite

    :param passed_torf: Boolean representing if the unit test passed or failed
    :return: None
    """

    global TESTNUM

    if did_pass:
        msg = 'Test %d Passed' % TESTNUM
    else:
        msg = 'Test %d Failed' % TESTNUM
    print(msg)

    TESTNUM += 1

def pennies_testsuite():
    """
    The test suite function utilizes the testit() function,
    and is designed to test the is_i_steal_pennies() function.

    :return: None
    """
    print("\nRunning pennies_testsuite()).")

    # Remember that i_steal_pennies() returns a list in the form [num_quarters, num_dimes, num_nickels, num_pennies]
    mytest(i_steal_pennies(0.88) == [3, 1, 0, 3])  # because three quarters, 1 dime, and 3 pennies equals 88 cents
    mytest(i_steal_pennies(0.89) == [3, 1, 0, 4])  # because three quarters, 1 dime, and 4 pennies equals 89 cents

    # TODO ADD MORE UNIT TESTS HERE!


    print("Run of pennies_testsuite() complete.")


def i_steal_pennies(to_change):
    """
    This function looks like it should take a floating point number to_change
    and return a list of how much change to give as [num_quarters, num_dimes, num_nickels, num_pennies]

    However, it compounds small truncation errors of the floating point arithmetic.
    Such errors are subtle and can be quite hard to debug, so unit tests are useful!
    A better algorithm would be to use integers instead of floats,
    but the point of this assignment is NOT to fix the error.
    It IS to help you learn to use and to value unit tests.

    :param to_change: a float representing an amount of money
    :return: A list of the number of quarters, dimes, nickels,
             and pennies representing the amount of money above
    """
    # TODO DO NOT CHANGE THIS FUNCTION!

    # Initialize values
    num_quarters = 0
    num_dimes = 0
    num_nickels = 0
    num_pennies = 0

    # Compute numbers of each coin type
    if to_change >= 0.25:
        num_quarters = int(to_change / 0.25)
        to_change = float(to_change % 0.25)

    if to_change >= 0.1:
        num_dimes = int(to_change / 0.1)
        to_change = float(to_change % 0.1)

    if to_change >= 0.05:
        num_nickels = int(to_change / 0.05)
        to_change = float(to_change % 0.05)

    if to_change >= 0.01:
        num_pennies = int(to_change / 0.01)

    return [num_quarters, num_dimes, num_nickels, num_pennies] # this order will be retained


def print_change(coinlist):
    """
    This program expects an input coin list of [num_quarters, num_dimes, num_nickels, num_pennies]
    It will print the values out for the user.

    :param coinlist: A list of the number of quarters, dimes, nickels,
                     and pennies representing the amount of money above
    :return: None
    """

    print("Can you tell if I am an honest machine? ")
    print("Give out the following change: ")
    valuelist = ["Quarter(s): ", "Dime(s): ", "Nickel(s): ", "Penny(s): "]
    for item in range(4):
        print(valuelist[item] + str(coinlist[item]))


def user_input_of_coins():
    """
    This function is created just for interactive fun.
    This would be for the normal mode of operation (not testing)

    :return: None
    """

    the_total = float(input("Input total amount of dollars and cents (e.g., 2.45): "))
    print("You have asked how to make " + str(the_total)+ " in change.")
    list_of_change = i_steal_pennies(the_total)
    print_change(list_of_change)


def main():
    """
    This main function is intended to test the correctness of the i_steal_pennies() function

    :return:
    """

    pennies_testsuite()


if __name__ == "__main__":
    # If you run this code directly (i.e., hit the green run button on this file), it runs the test suite
    # If you call this code from another file (e.g., t04_making_change_interactive.py), it will NOT run the test suite
    main()
