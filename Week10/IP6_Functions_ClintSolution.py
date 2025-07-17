# ---------------------------------
# ICE 6: Functions - CLINT's SOLUTION
# March 18, 2025
# Clint MacDonald
# ---------------------------------

#region IMPORTS
#endregion

#region GLOBAL VARIABLES (CONSTANTS)
# YOU MAY NOT CHANGE ANYTHING IN THIS SECTION
# except for the values of the variables for testing purposes
MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 12
ALLOW_SPECIAL_CHARACTERS = True
ALLOWED_SPECIAL_CHARACTERS = "!@#$%^&*"
MUST_HAVE_DIGIT = True
MUST_HAVE_UPPERCASE = True
MUST_HAVE_LOWERCASE = True
ALLOW_SPACES = False
ALPHANUMERIC_CHARACTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
#endregion

#region FUNCTION DEFINITIONS
# Enter your code here.... erase this comment before submitting
def getString(prompt):
    '''Obtains a string from the user'''
    return input(prompt).strip()

def passwordsMatch(password1, password2):
    '''checks if two strings are identical'''
    return password1 == password2

def validatePassword(password):
    '''wrapper function that consolidates all password validation tests'''
    # testing code, commented out before go live
    # print("Testing password length..." + str(test_password_length(password)))
    # print("Testing password allowed characters..." + str(test_password_allowed_characters(password)))
    # print("Testing password must have digit..." + str(test_password_must_have_digit(password)))
    # print("Testing password must have uppercase..." + str(test_password_must_have_uppercase(password)))
    # print("Testing password must have lowercase..." + str(test_password_must_have_lowercase(password)))
    # print("Testing password allow spaces..." + str(test_password_allow_spaces(password)))

    isValid = True
    if not test_password_length(password):              isValid = False
    if not test_password_allowed_characters(password):  isValid = False
    if not test_password_must_have_digit(password):     isValid = False
    if not test_password_must_have_uppercase(password): isValid = False
    if not test_password_must_have_lowercase(password): isValid = False
    if not test_password_allow_spaces(password):        isValid = False

    return isValid

    # or you could do this, but not as readable or maintainable.
    
    # return test_password_length(password) and test_password_allowed_characters(password) and test_password_must_have_digit(password) and test_password_must_have_uppercase(password) and test_password_must_have_lowercase(password) and test_password_allow_spaces(password)
    
def test_password_length(password: str):
    '''tests if the password is within the length range'''
    return len(password) >= MIN_PASSWORD_LENGTH and len(password) <= MAX_PASSWORD_LENGTH

def test_password_allowed_characters(password: str):
    '''tests if the password contains only allowed characters'''
    if ALLOW_SPECIAL_CHARACTERS:
        for c in password:
            if c not in ALLOWED_SPECIAL_CHARACTERS and c not in ALPHANUMERIC_CHARACTERS:
                #print("Invalid character: ", c)
                return False
    else:
        for c in password:
            if c not in ALPHANUMERIC_CHARACTERS:
                #print("Invalid character: ", c)
                return False
    return True

def test_password_must_have_digit(password: str):
    '''tests if the password contains at least one digit'''
    if MUST_HAVE_DIGIT:
        has_digit = False
        for c in password:
            if c.isdigit():
                #print("Digit found: ", c)
                has_digit = True
        return has_digit
    else:
        return True
    
def test_password_must_have_uppercase(password: str):
    '''tests if the password contains at least one uppercase letter'''
    if MUST_HAVE_UPPERCASE:
        has_uppercase = False

        #loop through each letter to test for an upper case letter
        for c in password:
            if c.isupper():
                #print("Uppercase found: ", c)
                has_uppercase = True

        return has_uppercase
    else:
        return True
    
def test_password_must_have_lowercase(password: str):
    '''tests if the password contains at least one lowercase letter'''
    if MUST_HAVE_LOWERCASE:
        has_lowercase = False

        #loop through each letter to test for an lower case letter
        for c in password:
            if c.islower():
                print("Lowercase found: ", c)
                has_lowercase = True
        
        return has_lowercase
    else:
        return True
    
def test_password_allow_spaces(password: str):
    '''tests if the password contains spaces'''
    if not ALLOW_SPACES:
        if " " in password: return False
        else: 
            return True
    else:
        return True
#endregion

#region MAIN APPLICATION

# YOU MAY NOT CHANGE ANYTHING IN THIS REGION
print('-'*40)
print("Welcome to the Password Generator")

doContinue = True
while doContinue:
    print('-'*40)

    # input
    password = getString("Enter your password (Q to Quit): ")
    if password.upper() == "Q":
        doContinue = False
        continue

    # have the user re-type the password to confirm
    password2 = getString("Re-enter your password: ")

    # check if the passwords match
    if passwordsMatch(password, password2):

        # check if the password is valid
        if validatePassword(password):    
            print("Password is valid")
        else: 
            print("Passwords are invalid")
    else:
        print("Passwords do not match")

    input("Press Enter to continue...")

print("Goodbye!")
print('-'*40)
exit(0)
#endregion