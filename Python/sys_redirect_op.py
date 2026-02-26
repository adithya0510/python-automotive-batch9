#Using the sys module, write a program that redirects output of a program to a text file.

import sys   #module
n = int(input("Enter a number: "))   # input statement can be shown in terminal
file = open("redirect_op.txt", "w")
sys.stdout = file              # redirect after input is entered

print("Output is redirected to the text file")    # prints after file is opened
if n % 2 == 0:
    print(f"{n} is an Even number")
else:
    print(f"{n} is an Odd number")
file.close()