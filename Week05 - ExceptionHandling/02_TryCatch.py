# -----------------------------
# Week 5 - Exception Handling
# Clint MacDonald
# June 2, 2025
# Learning hot to use basic try catch
# -----------------------------

# Try Catch Finally structure
# print('-'*60)
# try:
#     userInt = int(input("Enter a number: "))
#     print("Conversion successful!")
# except Exception as e:
#     print("Conversion Failed!")
#     print(e)
# finally:
#     print("This happens no matter what!")

# print('-'*60)


# try-catch with multiple exceptions

# try:
#     userInt = int(input("Enter a number: "))
#     print("Conversion Successful!")
#     print (10 / userInt)
# except ValueError as v:  # specific exception for conversion errors
#     print("Conversion Failed")
#     print("You did not enter a number!")
#     print(v)
# except ZeroDivisionError as z:
#     print("You cannot divide by zero!")
#     print(z)
# except Exception as e:  # catch all
#     print("A general error occurred!")
#     print(e)
# finally:
#     print("This will always print!")


# --------------------------------
# Nested Try Catch
# try:
#     userInt = int(input("Enter a number: "))
#     print("Conversion Successful")
    
#     try:
#         print(10 / userInt)
#         print("Division Successful")
#     except ZeroDivisionError as z:  # specific exception
#         print("Division Failed")
#         print("You cannot divide by zero")
#         print(z)
#     except Exception as e:  # catch all
#         print("General Error")
#         print(e)

#     print(10 / userInt)
#     print("Everything went great!")    

# except ValueError as v:
#     print("Conversion Failed")
#     print("You did not enter a number")
#     print(v)
# except Exception as e2:
#     print("catching the second error!")
# finally:
#     print("This will always run")



# Throwing exceptions
x = 17
y = 15

try:
    if (x > y):
        raise Exception("x cannot be greater than y")
    else:
        raise Exception("It actually worked and should not raise an exception!")
     
     # do stuff
except Exception as e:
    print("An error occurred!")
    print(e)
finally:
    print("This will always happen")
          
        