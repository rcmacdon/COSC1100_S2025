# -----------------------------
# COSC1100 - Week 9 
# Clint MacDonald
# July 10, 2025
# Introduction to Functions and Modularity
# -----------------------------


# Functions are a way to group code together and give it a name. This allows you to reuse the code multiple times without having to write it out each time. Functions can also take in input PARAMETERS and RETURN output. This allows you to create more flexible and reusable code.

# ---------------------------------------------------
# Verbage of Functions
# ---------------------------------------------------

# Various Names used for Functions:
# - Function
# - Method
# - Procedure
# - Subroutine
# - Constructor
# - Destructor
# - Getter or Setter
# - Accessor or Mutator
# - Lambda or Anonymous Function (arrow notation)

# in this course we will cover only functions and sub-routines

# ---------------------------------------------------
# Basic Rules of Functions
# ---------------------------------------------------
# 1. Function names should be descriptive and meaningful usually starting with a verb.
# 2. In Python, functions are declared separately from where they are called and using the "def" keyword
# 3. In Python, functions are declared BEFORE they are used.
# 4. Functions are called using the name and parenthesis ().
# 5. Functions can take in PARAMETERS which are values passed into the function.
# 6. Parameters may have default values
# 7. Functions can RETURN a value using the "return" keyword.
# 8. Functions can have multiple return statements but only one will be executed
# ---------------------------------------------------

# ---------------------------------------------------
# KEY IDEAS for designing functions
# ---------------------------------------------------
# 1. Functions should be small and do ONE thing well (PERFECT)
# 2. Functions should be reusable
# 3. Functions should be testable
# 4. Functions should not care WHY they are being used, they just do their job
# 5. Functions should be absolutely INDEPENDENT of other functions


# ----------------------------------------
# Example Function

def sayHello(): 
    '''A function that prints out "Hello World!"'''
    print("Hello World!")
# end of sayHello() function

sayHello()

print('-'*40)

def sayHelloTo(name):
    '''Function that says hello to the input string'''
    print("Hello %s" % name)

sayHelloTo("Clint")
sayHelloTo("Sally")

name = "John"
sayHelloTo("raj")
print(name)

#example 3
print('-'*40)

def sayHelloGreeting(greeting: str, name: str):
    '''A function the outputs a greeting customized for the name.'''
    print("%s %s!" % (greeting, name))


# use the function
sayHelloGreeting("Good Morning", "John")
sayHelloGreeting("Good Afternoon", "Class")
sayHelloGreeting("Why were you not in class today", "Bob")

# example 4
# math

def addTwoNumbers(num1, num2):
    '''A function that adds two numbers together!'''
    return num1 + num2


x = 4
y = 5
sum = addTwoNumbers(x, y)
print ("%i + %i = %i" % (x, y, sum))


# example 5 - Passing Parameters by Value
print ('-'*40)

def calculateNewSalary(salary: float, percentageRaise: float):
    '''A Function to calculate an employees new salary with the given percentage raise'''
    newSalary = salary * (1 + percentageRaise)
    salary = 0
    return newSalary

# call the function
mySalary = 50000.00
myRaise = 0.05

print("My salary is: $%.2f and my raise is %.2f" % (mySalary, myRaise))
newAmount = calculateNewSalary(mySalary, myRaise)
print("My salary is: $%.2f and my raise is %.2f" % (mySalary, myRaise))
print("My new salary is: $%.2f" % newAmount)

print('-'*40)

#example of returning MORE THAN 1 THING
#example 6
# PYTHON ONLY

def addAndSubtract(a: int, b: int):
    '''Function that returns both the sum and the difference between 2 numbers'''
    add = a + b
    subtract = a - b
    return add, subtract

#calling this function
sum, diff = addAndSubtract(10, 5)
print("Sum: %d, Diff: %d" % (sum, diff))












