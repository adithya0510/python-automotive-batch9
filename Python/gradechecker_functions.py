def check_status(marks):  # defining a function along with arguement
    return marks >= 60   # return True if marks >= 60, else False

#user input (marks)
english = int(input("Enter english marks: "))  # English marks
print("English status:", check_status(english))   # Function calling along with print statement True = Pass(marks >= 60)  False = Fail(marks < 60)

hindi = int(input("Enter hindi marks: "))     # hindi marks
print("Hindi status:", check_status(hindi))

social = int(input("Enter social marks: "))   # social marks
print("Social status:", check_status(social))
