# print out multiples of of each number between 1 and 10 to the power of 5 each

# header
header_string = ""
for header_column in range(1, 6):
    header_string += ("%8i" % header_column)
print (header_string)

print(" -------"*5)

for row in range (1,11):

    row_string = ""
    for column in range(1, 6):
        row_string = row_string + ("%8i" % row**column)

    print(row_string)

    