

## modules
import os
try:
    from time import *
except:
    print("Installing time module...")
    os.system('python -m pip install time')
    exit()
try:
    from functools import reduce
except:
    print("We could not import module 'functools'. Please install it to continue. Auto-installing in 5 seconds...")
    sleep(5)
    os.system('python -m pip install functools')
    exit()
    
try:
    import urllib.request
    import requests
    import platform
    import subprocess

except:
    print("We could not import the following modules: 'urllib', 'requests', 'platform', 'subprocess'. Please install them to continue. Auto-installing it in 5 seconds...")
    sleep(5)
    sleep(5)
    os.system('python -m pip install urllib requests platform subprocess')
    exit()
try:    
    from colorama import Fore, Back, Style
    from termcolor import colored

except:
    print("We could not import module 'colorama', 'termcolor'. Please install it to continue. Auto-installing it in 5 seconds...")
    sleep(5)
    os.system('python -m pip install colorama termcolor')
    exit()
os.system("cls" or "clear")
print("\n\n\n\n\n\n\n\n\n")
## functions
def listToString(s):
    for i in s:
        print(i,end="\n")

def ping(host):
    response = os.system("ping -n 1 "+host)
    if response == 0:
        print(Fore.GREEN + host + " is up!" + Fore.BLACK)
    else:
      print (Fore.RED + host, "is down!" + Fore.BLACK)
#if firstuser
try:
    if os.path.exists("C:\JaskaranOS") == True:
        firstuser = "false"
        print(Fore.GREEN + "Welcome back to JOS - Jaskaran's Operating System\n" + Fore.RESET)
    else:
        print("")
        os.mkdir("C:\JaskaranOS")
        firstuser = "true"
except:
    print(Fore.RED + "Cannot access C:\ Drive. Please ensure that you have access to it in order to use commands such as "+ Fore.BLUE + "get" + Fore.RED + "." + Fore.RESET)
try:    
    if firstuser == "true":
        print(Fore.CYAN + "Welcome to JaskaranOS! This is a command-based operating system. For help on commands, please type in: 'help' in the command line!\nThis OS has been tested on a Windows Machine. It currently does not have the capablities to be run on it's own, separate computer." + Fore.RESET)
except:
    print("")
# INPUT
while True:
    a = input("> ")

# now the processing!

 # Help
    if a == "help":
        print(Back.BLUE + "Welcome to JaskaranOS help! Here are the available commands:\nhelp - Opens this\necho (string) - Echoes (repeats) back\nls (string) - List Files in Directory\ntext (string/directory) - Creates a new text file\nwrite (string) - Write to a text file. First write what you want, then it will ask you for the directory. Use \ n (without spaces) for a new line.")
        print("read (directory) - Reads text file specified by user.")
        print("get (url) - [BETA] Download files over the internet. Requires WGET module.")
        print("run (directory) - Runs an application.")
        print("ping (website) - Pings a website to check if it can connect.\nsay (input) - Text To Speech engine. Change voice by saying 'say male' or 'say female'")
        print("username / user - Checks your username. Requires GETPASS module.")
        print("password / pass - Asks for password to continue. Doesn't work on some compilers.")
        print("cmd (input) - Used windows CMD to run advanced commands.")
        print("pip install (input) - Installs python modules using PIP." + Back.RESET)

 # Echo
    elif a[0:5] == "echo ":
        echo = a[5:]
        print(echo)

 # List files
    elif a[0:3] == "ls ":
        ls = str(a[3:])
        try:
            okay = '\n'.join(map(str, (os.listdir(ls))))
            print("Files in", ls+":\n\n\nl"+okay)
        except FileNotFoundError:
            print("File Not Found!")
    
 # Create new textfile
    elif a[0:5] == "text ":
        text = str(a[5:])
     
        try:
            f = open(text+".txt", 'w')
            print("Created new file in", text)
        except:
            print("Error occured.")

    # Text Editor
    elif a[0:6] == "write ":
        write = str(a[6:])
    
        print("Where would you like to store this? Please enter a directory (no extension).")
        directory = input("> ")
        try:
            with open(str(directory+".txt"), 'w') as f:
                f.write(write)
            print("Wrote", write, "to", directory)
        except:
            print(Fore.RED + "Error occured." + Fore.RESET + " Tips: " + Fore.RED + "do NOT include the .txt" + Fore.RESET + " and include a valid directory")
    
 # Text Reader
 
    elif a[0:5] == "read ":
        read = str(a[5:])

    
     
        with open(read+".txt") as f:
            lines = f.readlines()
            print(listToString(lines))
 
    # [BETA] Get
    elif a[0:4] == "get ":
        get = str(a[4:])
        try:
            try:
                import wget
            except:
                print("Error! Please install WGET by typing in CMD: 'pip install wget'")
            print("Please enter a file location(with file name and extension). E.g: C:\JaskaranPython\Logo.png")
            hi = input("> ")
            wget.download(url, str(hi)) 

        except:
            print("Error. Development on the get function is still ongoing. Some websites which do not follow a particular protocol cannot be decoded.")
         
    # Run
    elif a[0:4] == "run ":
        run = str(a[4:])
        try:
            os.startfile(run)
        except:
            print("Error. Incorrect file path?")
     
     
    elif a[0:5] == "ping ":
        pinsg = a[5:]
        print("You have chosen to ping, "+str(pinsg))
        ping(pinsg)
        
    elif a == "hi" or a == "hello" or a == "hey there" or a == "what do you do" or a == "what do you do?":
        print(Fore.GREEN + "Hello, there! Please type in 'help' for help on commands!" + Fore.RESET)
        
    elif a[0:7] == "colour " or a[0:6] == "color ":
        if a[0:7] == "colour ":
            color = a[7:]
        else:
            color = a[6:]
        print("Colour is now", color)
        try:
            print(Fore.color + "Testing to check colour..")
        except:
            print("\nError: Color system is currently " + Fore.RED + "offline. " + Fore.RESET + "Please try again later.")
            
    elif a[0:4] == "say ":
        say = str(a[4:])
        try:
            import pyttsx3
        except:
            print(Fore.RED + "Error! Please install the 'pyttsx3' python package! ( pip install pyttsx3 ) ")
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        if a == "say male":
            print("Setting voice to Male...")
            engine.setProperty('voice', voices[1].id)
            print("Done.")
        elif a == "say female":
            print("Setting voice to Female...")
            engine.setProperty('voice', voices[0].id)
            print("Done.")
        else:

            engine.say(say)
            engine.runAndWait()
        
        
    elif a == "password" or a == "pass":
        try:
            import getpass
        except:
            print(Fore.RED + "Error. 'Getpass' Module required." + Fore.RESET)
        try:
            getpass.getpass()
        except:
            print(Fore.RED + "Error! Incorrect password?")
        else:
            print('Password success!')
            
    elif a == "username" or a == "user":
        try:
            import getpass
        except:
            print(Fore.RED + "Error. 'Getpass' Module required." + Fore.RESET)
        
        print("Your username is " + Fore.GREEN + getpass.getuser() + Fore.RESET + ".")
        
    elif a[0:4] == "cmd ":
        cmd = a[4:]
        os.system(cmd)
    
    elif a == "unknown command":
        print(Fore.RED + "You have typed in an unknown command. The system does not know how to handle this request.")
        print(Fore.MAGENTA + "For a list of available commands, please type in: " + Fore.GREEN + "'help'" + Fore.RESET)
        print(Fore.CYAN + "If you are looking to run Windows CMD commands on JOS, please type in: '" + Fore.GREEN + "cmd (input)" + Fore.CYAN + "'" + Fore.RESET) 
    
    elif a[0:12] == "pip install ":
        pip = a[12:]
        os.system("python -m pip install "+pip)
    
    
    
    else:
        print(Fore.RED + "Unknown command. Please type in 'unknown command' for more information." + Fore.RESET)
    