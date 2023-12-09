import itertools
import sys
from itertools import product

global pw
pw = sys.argv[1]
#questions to determine more information about the password before
#guessing, in case the user knows more information about the password
#that would cut time off the guessing process.
pwlength = int(input("How long is the password?"))
print("For the following questions, type Y if yes or if unsure, and N if no.")
lower = input("Does the password have lowercase letters?")
upper = input("Does the password have uppercase letters?")
numbers = input("Does the password have numbers?")
symbols = input("Does the password have symbols?")
pwCharList = ""

if (lower=="Y"):
    pwCharList+="abcdefghijklmnopqrstuvwxyz"
if (upper=="Y"):
    pwCharList+="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if (numbers=="Y"):
    pwCharList+="1234567890"
if (symbols=="Y"):
    pwCharList+="`~!@#$%^&*()-_=+[{]}|';:/?.>,<"


#uses Cartesian Product function for all lengths of password up to the
#number input by the user to determine every possible combination.

for j in range (1, pwlength+1):

    c = product(pwCharList,repeat=j)
    for i in list(c):
        #runs through, formats, and prints the list of passwords.
        password = ""
        lister = list(i)
        for j in list(lister):
            password +=j
        if (password == pw):
            print("Password Found! It is " + password)
            quit()
            
print("Password Not Found. Sorry!")

    

