import os
import sys

os.system("clear")
b = input("2 packages? y/n: ")

if b == "y":
        c = input("sudo apt install: ")
        d = input("sudo apt install: ")

        print()
        print("[!] INSTALLING PACKAGES")
        os.system("sudo apt install " + c + " && sudo apt install " + d)
        print()
        sys.exit()
elif b == "n":
        a = input("sudo apt install: ")
        print()
        print("[!] INSTALLING PACKAGE")
        os.system("sudo apt install " + a)
        print()
        sys.exit()
else:
        sys.exit()