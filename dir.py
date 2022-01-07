import os
import time

"""
Install PsTools and put it in the system32 file 
"""
print("Loading...")
os.system("pssuspend  GTA5.exe")
time.sleep(25)
os.system("pssuspend -r  GTA5.exe")
print("DONE.")
