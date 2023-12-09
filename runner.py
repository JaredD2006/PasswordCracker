import sys
import os


for i in range (1, len(sys.argv)):
    if (i==1):
        password = sys.argv[1]
    if (i==2):
        program = sys.argv[2]

if (program == "bf"):
    os.system("python3 brute-force.py " + password)
elif (program == "m"):
    os.system("python3 MD5.py " + password)
elif (program == "s"):
    os.system("python3 SHA256.py " + password)
elif (program == "bc"):
    os.system("python3 Bcrypt.py " + password)