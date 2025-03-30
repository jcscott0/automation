import os
import sys

def main():
        q = input("Create folder/subfolder, or add a subfolder to existing parent? ('c' or 'a'): ")

        if q == "c":
                create()
        elif q == "a":
                add()
        else:
                print("Abort.")
                sys.exit()

def create():
        a = input("First folder: ")
        os.system("mkdir " + a)
        b = input("Subfolder: ")
        os.system("mkdir " + a + "/" + b)
        #q = input("Create another subfolder for existing folder?: ")
        sys.exit()

        #if q == "yes":
        #       ab = input("Which parent folder do you want to choose?: ")
        #       c = input("Subfolder: ")
        #       os.system("mkdir " + ab + "/" + c)
        #       sys.exit()
        #else:
        #       sys.exit()

def add():
        p = input("Parent folder to add to: ")
        ps = input("Subfolder: ")
        os.system("mkdir " + p + "/" + ps)
        sys.exit()

main()