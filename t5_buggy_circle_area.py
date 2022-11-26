######################################################################
# Author: Dr. Jan Pearce and Patrick Shepherd      TODO: Change this to your names
# Username: pearcej, shepherdp                     TODO: Change this to your usernames
#
# Assignment: T5: Buggy Fruit
# Purpose: A flawed program which uses a function to determine the area of a circle
# There are several problems with this code. Use the debugger to find them.
#
# Background:
# The area of a circle is the number of square units inside that circle.
# a formula for this area is a = PI * r**2 where PI is an irrational number
# approximated by PI=3.141592
######################################################################
# Acknowledgements:
#   Original Author: Dr. Jan Pearce
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import sys                          #needed for unit testing
r=0                                 #FIXME: This variable should not be here.  Please fix.

def testit(did_pass): #This function is correct
    """
    Print the result of a unit test.

    :param did_pass: Boolean value representing a test case
    :return: None
    """

    # This function may cause an error due to an update in Python.
    # If so, comment the following line out, as well as the lines under the
    # 'if' and 'else' statements, and replace them with a simple print
    # such as 'print( 'Passed' )' or 'print( 'Failed' )'.
    linenum = sys._getframe(1).f_lineno # Gets the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def circleArea(i):                  #FIXME please fix: parameter names should be meaningful!!
    '''area docstring for circle''' #FIXME: example of useless docstring- please fix!
    PI = 3.141592
    i = r                           #FIXME:
    area = PI * r**2                # this formula is correct
    return area

def circleArea_test_suite(): # These until tests are correct
    """
    Test suite to test circleArea
    :return: None
    """
    print("\nRunning circleArea_test_suite()).")
    testit(circleArea(0)==0)
    testit(circleArea(1)==3.141592)
    testit(circleArea(2.5)==3.141592*2.5*2.5)

def main():
    # This is where the main program starts

    myarea = circleArea(r)
    print("The area is: " + str(myarea))
    circleArea_test_suite()

main()
