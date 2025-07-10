# ------------------------------------------
# Title:   ICE 5 - Arrays
# Author:  
# Date:
# Purpose: To demonstrate knowledge of working with arrays
# ------------------------------------------

#region Declarations
studentList = []
ALLOW_DUPLICATES = False
menuText = """
------------------------------------
Main Menu
1. Add Student to the Queue
2. View Enter Queue
3. Call Next Student in Queue
4. Remove Student From Queue
5. Quit"""
#endregion

#region Main Application
print('-'*40)
print("Welcome to the Student Queue Application!")
print('-'*40)

doContinue = True
while doContinue:
    print(menuText)
    print('-'*40)
    print("Students in the queue: %d" % len(studentList))
    print('-'*40)
    choice = input("Enter your choice (1-5): ")

    print('-'*40)
    if choice == "1":
        studentName = input("Enter the student's name: ")
        if studentName in studentList and not ALLOW_DUPLICATES:
            print("Student %s already exists in the list." % studentName)
        elif len(studentName) == 0:
            print("Student name cannot be empty.")
        else:
            studentList.append(studentName)
            print("Student %s added to the list." % studentName)
    elif choice == "2":
        print("Students in the queue:")
        for student in studentList:
            print(student)
    elif choice == "3":
        if len(studentList) > 0:
            nextStudent = studentList.pop(0)
            print("Next student in line is %s" % nextStudent)

            if input("Is the student present (y/n)? ").lower() == "n":
                print("Student %s is absent, added to the end of the list!" % nextStudent)
                studentList.append(nextStudent)
            
        else:
            print("No students in the queue.")
    elif choice == "4":
        studentName = input("Enter the student's name: ")
        if studentName in studentList:
            studentList.remove(studentName)
            print("Student %s removed from the list." % studentName)
        else:
            print("Student %s not found in the list." % studentName)
    elif choice == "5":
        doContinue = False
        print("Thank you for using the Student Queue Application!")
    else:
        print("Invalid choice. Please try again.")  

    print('-'*40)
    print('press enter to continue...')
    input()
    print('-'*40)

#endregion