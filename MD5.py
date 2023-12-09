import hashlib
import sys
import os

password = sys.argv[1]

#opens and reads a file of the English dictionary into a variable.
file = "/Materials/dictionary.txt"
#file = "\\Materials\\dictionary.txt"
path = os.getcwd()+file
wordList = open(path, 'r')
wlist = wordList.readlines()

#opens and reads a file of the 10000 most common passwords into a variable.
file2 = "/Materials/commonpasswords.txt"
#file2 = "\\Materials\\commonpasswords.txt"
path2 = os.getcwd()+file2
passwordList = open(path2, 'r')
pwlist = passwordList.readlines()

def hash(x):
    #encodes the string into MD5 before digesting it into hex format
    str = hashlib.md5(x.rstrip().encode('utf-8'))
    return str.hexdigest()

def check(x, y):
    #checks if the password input by the user is equal to the hashed version of a dictionary word/common password
    if (x==hash(y)):
        print("Password Found! It is " + y)
        quit()
    

#runs through the list and encrypts each value to see if it is the same as the one input by the user
for i in range(0, len(wlist)):
    check(password, wlist[i])
for j in range(0, len(pwlist)):
    check(password, pwlist[j])
print("Password Not Found. Sorry!")


