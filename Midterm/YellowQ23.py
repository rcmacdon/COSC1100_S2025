
LOOP_TIMES = 10
MAX_NUMBER = 9
print('-'*58)

try:
    user_input = int(input(('Enter an integer (1-%i)') % MAX_NUMBER))

    if 1 <= user_input >= MAX_NUMBER:
    #if user_input >= 1 and user_input <= MAX_NUMBER:

        for i in range(1, LOOP_TIMES+1):
            print('%i x %i = %i' % (user_input, i, user_input * i))

    else:
        print('input must be in the right range')
except ValueError as v:
    print('You did not enter a number!')

print('-'*58)