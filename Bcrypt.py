import sys
import os
import bcrypt

#opens and reads a file of the English dictionary into a variable.
file = "\\Materials\\dictionary.txt"
path = os.getcwd()+file
wordList = open(path, 'r')
wlist = wordList.readlines()

#opens and reads a file of the 10000 most common passwords into a variable.
file2 = "/Materials/commonpasswords.txt"
#file2 = "\\Materials\\commonpasswords.txt"
path2 = os.getcwd()+file2
passwordList = open(path2, 'r')
pwlist = passwordList.readlines()

pw = sys.argv[1]

def hash(x):
    #encodes the password into bytes and encrypts it with a random salt.
    password = x.encode('utf-8')
    return bcrypt.hashpw(password, bcrypt.gensalt())

def check(x, y):
    #checks if the password input by the user is equal to the hashed version of a dictionary word/common password
    password = x.rstrip().encode('utf-8')
    salt = y.rstrip().encode('utf-8')
    if bcrypt.checkpw(password, salt):
        print("Your Password Is... " + x)
        quit()
        


#runs through the list and encrypts each value to see if it is the same as the one input by the user
for i in range(0, len(wlist)):
    check(wlist[i], pw)
for j in range(0, len(pwlist)):
    check(pwlist[j], pw)
print("Password Not Found. Sorry!")
