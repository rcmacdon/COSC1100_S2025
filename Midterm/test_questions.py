number1 = "3"
number2 = "5"
number3 = 7
print(number1 + number2)
number3 += 4
print(number1 + str(number3))
print(int(number1) // int(number2))
print("I like %i and %i" % (int(number1),int(number2)))
print(str(number1) + str(number2))

myString = "nums: "
for i in range(2, 8, 2):
    myString += str(i)

print(myString)
