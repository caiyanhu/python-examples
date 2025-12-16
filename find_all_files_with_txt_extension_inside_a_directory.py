import glob
import os

os.chdir(".")

for file in glob.glob("*.txt"):
    print(file)

for file in os.listdir("."):
    if file.endswith(".txt"):
        print(file)

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".txt"):
            print(file)
