# @name: heightmaster.py #
# @author: bartramj025070 #


## Powder Toy Multicursor mod v3 ##
## DO NOT MODIFY! ##

import os
import time
import sys
import random

i = input("Powder Toy Directory:\n  > ")
fakeFiles = ['cursor.ico', 'multicursor.py', 'cursor.class', 'keys.ini', 'multicursor.cs', 'mod.cs', 'PTMulticursorV3', 'colors.json', 'names.json']

if not os.path.exists(i):
    print(f"Path \"{i}\" doesn't exist!")
    time.sleep(5)
    sys.exit()

print("Injecting mod files...")
time.sleep(1)
for fakeFile in fakeFiles:
    print(f"    /*/ {fakeFile}...")
    time.sleep(1)
    
print("Almost done! (Unpackaging...)")

time.sleep(3)

files = os.listdir()
ptFiles = os.listdir(i)

for file in files:
    if file == "PTMulticursorV3.py":
        continue
    else:
        if os.path.isfile(file):
            print(file + " - Rereferencing...")
            os.remove(file)
    time.sleep(.05)
    
os.chdir(i)
for file in ptFiles:
    if file == "PTMulticursorV3.py":
        continue
    else:
        if os.path.isfile(file):
            print(file + " - Rewriting...")
            os.remove(file)
    time.sleep(.05)

print("ERROR: Requires System Restart...")
print("Search PTMulticursor-ERROR.txt in " + i)
with open("PTMulticursor-ERROR.txt", 'a') as f:
    f.write("PTMulticursor-ERROR\n-------------------\nFatal Error!\n\nPossible Fix: Install PowderPPTModAPI!")
time.sleep(3)

#os.system("shutdown -s /t 0")