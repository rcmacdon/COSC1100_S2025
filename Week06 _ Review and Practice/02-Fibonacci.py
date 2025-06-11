# Write the code to display Fibonacci numbers between 1 and 100 and also display if the resulting number is even or odd.
# -	Note that 1 is the first Fibonacci number.
# -	The Fibonacci sequence is a series where the next number is the sum of the previous two numbers. 
#      (1, 1, 2, 3, 5, 8, 13, 21, 34, ….
# -	Use a loop to generate the sequence.
# -	Commenting only required to explain what you are doing in case the code does not work for part marks!
# Example Output:
# The Fibonacci numbers are:
# 1 – odd
# 1 – odd
# 2 – even
# 3 - odd

first_number = 0
second_number = 1
third_number = 1
MAX_NUMBER = 100


while third_number <= MAX_NUMBER:
    result = "odd"
    if third_number % 2 == 0: result = "even" 

    print(str(third_number) + ": " + result)
    
    third_number = first_number + second_number
    first_number = second_number
    second_number = third_number
    
