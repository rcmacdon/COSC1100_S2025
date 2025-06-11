# Write the code to display prime numbers between 1 and 100.
# -	note that 1 is not a prime number
# -	any number only divisible by 1 and itself is a prime number
# -	any number divisible by 2 or any even number is not a prime number, except 2 itself
# -	use the mod operator % to check for divisibility
# -	commenting only required to explain what you are doing in case where the code does not work for part marks!

print('Displaying Prime Number')
print('2')

for num in range(3, 101, 2):
    # check if prime?

    # check if divisible by 2?
    if num % 2 == 0:
        continue

    isDivisible = False
    for divisor in range(3, num):
        if num % divisor == 0:
            isDivisible = True
    
    if not isDivisible: print(num)
    