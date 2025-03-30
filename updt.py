import os
import sys

os.system("clear")
print("[!] UPDATING")
os.system("sudo apt update")
print("")
print("[!] UPGRADING")
os.system("sudo apt upgrade")
print()
sys.exit()