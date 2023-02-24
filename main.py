print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nJaskaran Operating System\n")
try:
    from time import *
except:
    print("Error. We need the time module in order for the Operating System to load.. please install it ASAP via CMD in the boot options")
print("Boot 2.0 by Jaskaran, for Faster Boot\n")

start = input("BOOT OPTIONS: \n(enter) - Boot the machine\n'options' - View boot options\n'cmd' - Opens CMD line\n> ")
if start == "options" or start == "option":
    print("BOOT options for JOS..")
    print("1 - Reset JOS\n2 - Coming soon\n3 - Coming soon")
    option = input("> ")
    if option == "1":
        print("Are you sure you want to reset JOS? This will delete all files and do a complete factory reset for JOS. (y/n)")
        if input("> ") == "y":
            print("Importing modules..")
            try:
                import shutil
                print("Successfully imported modules.\nAttempting to do a factory reset...")
                try:
                    
                    shutil.rmtree(r'C:\JaskaranOS')
                    print("Success. Please wait whilst we load up your fresh new version of JOS...")
                    sleep(5)
                except Expection as e:
                    print("Error doing factory reset. Error message:")
                    print(e)
                    sleep(5)
            except:
                print("Error importing shutil. Attempting to resolve..")
                try:
                    import os
                    os.system("pip install shutil")
                    print("Resolved issue.. deleting JOS..")
                    try:
                        shutil.rmtree(r'C:\JaskaranOS')
                        print("Success. Please wait whilst we load up your fresh new version of JOS...")
                        sleep(5)
                    except Expection as e:
                        print("Error doing factory reset. Error message:")
                        print(e)
                        sleep(5)
                except:
                    print("Attempt to resolve failed...")
                    sleep(2)
        else:
            print("Aborted. Contuining to operating system..")
            sleep(2)
elif start == "cmd":
    print("\n\nCMD Emulator")
    try:
        import os
    except:
        print("Error importing module 'os'.")
    while True:
        os.system(input("> "))

print("Loading Boot...")
## Defaults
short = False
## Functions
print("Loading... (this process may take up to 10 seconds without boot)")

print("Creating functions..")
def webpageViewer():
    try:
        import os
        import webbrowser
        import sys
        from time import sleep
        from bs4 import BeautifulSoup
        import requests
        import tkinter as tk
        from tkinter import simpledialog
        import getpass
        import asyncio
        
    except:
        print("Error occured. Cannot access webpage-viewer because following modules need to be installed (via 'pip install (modulename)'): os, webbrowser, sys, time, bs4, requests, tkinter, getpass (used to identify username to write files to specific user), asyncio")
        exit()
    print("Successfully imported modules. \n")
    print("Welcome to JOS's WEBVIEWER - A simple tool used to browse or search the internet!")
    print("Would you like to search (search) or open up a website (website)?")
    query = input("> ")
    if query == "search":
        print("Excellent! What would you like to search for?")
        search = str(input("> "))
        print("What search engine? Please choose from: Google, Bing, Yahoo!, YouTube, Wikipedia, Dictionary")
        engine = input("> ")
        if engine == "google" or "Google":
            webbrowser.open("https://www.google.com/search?q=" + search)
        elif engine == "bing" or "Bing":
            webbrowser.open("https://www.bing.com/search?q=" + search)
        elif engine == "yahoo" or "Yahoo" or "Yahoo!" or "yahoo!":
            webbrowser.open("https://www.search.yahoo.com/search?p=" + search)
        elif engine == "youtube" or "Youtube" or "YouTube" or "you tube":
            webbrowser.open("https://www.youtube.com/results?search_query=" + search)
        elif engine == "wikipedia" or "Wikipedia":
            webbrowser.open("https://en.wikipedia.org/wiki/" + search)
        elif engine == "Dictionary" or "dictionary":
            webbrowser.open("https://www.oxfordlearnersdictionaries.com/definition/english/" + search)
    elif query == "website":
        print("Excellent! What website would you like to visit?")
        website = input("> ")
        webbrowser.open(str(website))
def email():
    try:
        import smtplib, ssl
    except:
        os.system("pip install smtplib")
        os.system("pip install ssl")
        import smtplib, sll
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    if os.path.isfile("C://JaskaranOS/email/email.txt") == True:
        with open('C://JaskaranOS/email/email.txt') as f:
            sender_email = f.readlines()
    else:
        sender_email = str(input("Please type in your email...\n> "))
        os.mkdir("C://JaskaranOS/email")
        f = open("C://JaskaranOS/email/email.txt", "x")
        f = open("C://JaskaranOS/email/email.txt", "w")
        f.write(sender_email)
        f.close()
        
    receiver_email = str(input("Please type in the receivers email...\n> "))
    if os.path.isfile("C://JaskaranOS/email/password.txt.aes") == True:
        passwordd = "a9AS8HAOSIUTHG4IS7YFGOASFAUPQ39Y08haiofisjfauoio9YU9do8gHODifhyf98ofihfaofhyy*Y*F&S*YS&Y87GF87fG8g*&tgf*"
        pyAesCrypt.decryptFile("C://JaskaranOS/email/password.txt.aes", "dataout.txt", passwordd)
        with open('dataout.txt') as f:
            password = f.readlines()
        os.remove('dataout.txt')
    else:
        
        password = str(input("Type your password for your email... (Note, if you use 2FA, you need to make an app password here: https://bit.ly/google-app-passwords )\n> "))
        f = open("C://JaskaranOS/email/password.txt", "w")
        f.write(password)
        f.close()
        passwordd = "a9AS8HAOSIUTHG4IS7YFGOASFAUPQ39Y08haiofisjfauoio9YU9do8gHODifhyf98ofihfaofhyy*Y*F&S*YS&Y87GF87fG8g*&tgf*"
        pyAesCrypt.encryptFile("C://JaskaranOS/email/password.txt", "C://JaskaranOS/email/password.txt.aes", passwordd)
        
        
    message = str(input("Please type in the message contents (Use 'Subject: (SUBJECT)' for the subject).\n> "))
    try:
        print("Sending email...")
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo() 
            server.starttls(context=context)
            server.ehlo() 
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        print("Email successfully sent.")
    except Exception as e:
        print("Error whilst sending email.")
        sleep(1)
        print(e)
print("Done!")
print("Importing modules...")
## modules
import os
import sys
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

if os.path.isdir("C://JaskaranOS/configuration/incorrect-password") == True:
    incorrectcmd = 1
else:
    incorrectcmd = 0

try:
    import urllib.request
except:
    os.system("pip install urllib.request")
    import urllib.request
try:
    import requests
except:
    os.system("pip install requests")
    import requests
try:
    import platform
except:
    os.system("pip install platform")
    import platform

try:
    import subprocess
except:
    os.system("pip install subprocess")
    import subprocess

try:
    import pyAesCrypt
except:
    os.system("pip install pyAesCrypt")
    import pyAesCrypt

try:
    import getpass
except:
    os.system("pip install getpass")
    import getpass
    

try:    
    from colorama import Fore, Back, Style
    from termcolor import colored

except:
    print("We could not import module 'colorama', 'termcolor'. Please install it to continue. Auto-installing it in 5 seconds...")
    sleep(5)
    os.system('python -m pip install colorama termcolor')
    exit()
try:
    from datetime import datetime
except:
    os.system("pip install datetime")
    from datetime import datetime
print("Done!")
os.system("cls" or "clear")
print("\n\n\n\n\n\n\n\n\n")
## functions
print("Defining more functions..")
def listToString(s):
    for i in s:
        print(i,end="\n")

def ping(host):
    response = os.system("ping -n 1 "+host)
    if response == 0:
        print(Fore.GREEN + host + " is up!" + Fore.BLACK)
    else:
      print (Fore.RED + host, "is down!" + Fore.BLACK)
      
print("Done!")     
# Loading
print("Checking boot...")
if os.path.exists("C://JaskaranOS/") and os.path.exists("C://JaskaranOS/boot") == True:
    try:
        print("Importing boot modules..")
        import itertools
        import threading
        import time
    except:
        print("Error importing boot modules. Trying to fix...")
        os.system("pip install itertools")
        os.system("pip install threading")
        os.system("pip install time")
        import itertools
        import threading
        import time
        
    print("\n\nBooting...")
    done = False
    #here is the animation
    def animate():
        for c in itertools.cycle(['|', '/', '-', '\\','|', '/', '-', '\\','|', '/', '-', '\\']):
            if done:
                break
            sys.stdout.write('\r ' + c)
            sys.stdout.flush()
            sleep(0.1)
        sys.stdout.write('\rDone!     \n')

    t = threading.Thread(target=animate)
    t.start()

    try:
        passwordd = "vTWMDsvbAnlFmFNIRRML"
        pyAesCrypt.decryptFile("C://JaskaranOS/encrypted-password.txt.aes", "dataout.txt", passwordd)
    except Exception as e:
        print("Error whilst decrypting/accessing encrypted file.")
        print(e)
    with open('dataout.txt') as f:
        urpass = f.read()
    os.remove("dataout.txt")
    sleep(1)
    done = True
else:
    if os.path.exists("C://JaskaranOS/") == True:
        print("Please wait, loading!")
        print("decrypting password...")
        try:
            passwordd = "vTWMDsvbAnlFmFNIRRML"
            pyAesCrypt.decryptFile("C://JaskaranOS/encrypted-password.txt.aes", "dataout.txt", passwordd)
        except Exception as e:
            print("Error whilst decrypting/accessing encrypted file.")
            print(e)
        print("done!\nreading file...")
        try:
            with open("dataout.txt") as f:
                urpass = f.read()
        except:
            print("An error occured! This may be due to a corrupted password. One possibility of this error was leaving set-up whilst you hadn't encrypted/chosen the password!")
        print("done!\ndeleted decrypted file...")
        os.remove("dataout.txt")
        print("done!\nloading password manager...")
        sleep(0.7)

import socket
#if firstuser
try:
    if os.path.exists("C:\JaskaranOS") == True:
        firstuser = "false"
        sleep(1)
        print("Opened popup-window...")
        print(Fore.GREEN + "\n              Welcome back to JOS - Jaskaran's Operating System\n" + Fore.RESET)
    else:
        print("")
        os.mkdir("C:\JaskaranOS")
        firstuser = "true"
except:
    print(Fore.RED + "Cannot access C:\ Drive. Please ensure that you have access to it in order to use commands such as "+ Fore.BLUE + "write" + Fore.RED + "." + Fore.RESET)


existss = "0"
## Password login/creator
sleep(1)
try:    
    if firstuser == "true":
        print("Popup-window..")
        print(Fore.GREEN + "Welcome to JaskaranOS! This is a part-command and part-gui based operating system. For help on commands, please type in: 'help' in the command line!\nPlease do not exit/turn your computer off during setup, or this will corrupt the file. In case your file is corrupted, make sure to do a factory reset in the boot options!" + Fore.RESET)

        sleep(5)
        print("Please input a Password! (Don't worry- the password will be encrypted!)")
        
        password = input("> ")
        
        
        print("Set password to", str(password))
        with open('C://JaskaranOS/password.txt', 'w') as f:
            f.write(str(password))
            
        print("Successfully set password!\n")
        ## encrypt password file
        try:
            import pyAesCrypt
        except:
            print("Hold on a second! A module hasn't been installed correctly! Fixing..")
            os.system("pip install pyAesCrypt")
            import pyAesCrypt
            print("There you go!")
        passwordd = "vTWMDsvbAnlFmFNIRRML"
        print("Please wait whilst we encrypt your password... (dont turn off ur pc!!)")
        pyAesCrypt.encryptFile("C://JaskaranOS/password.txt", "C://JaskaranOS/encrypted-password.txt.aes", passwordd)
        sleep(2)
        os.remove("C://JaskaranOS/password.txt")
        print("Done.\n")
        boot = input("Would you like to have a boot screen(this may take up to 10 seconds to load the os but is a safer option). Yes/no\n> ")
        if boot == "yes":
            os.mkdir("C://JaskaranOS/boot")
            print("Done! You can switch your option by using command 'boot'!\n\n")
    else:
        
        print("\n     Please enter your password!")
        x = 0
        rx = 1
        while x < 3:
            password = input("> ")
            if str(password) == urpass:
                print("Succesfully authorised user.")
                x = 10
                break
            else:
                print("Error: Invalid password. Attempt "+ str(rx) + "/3.")
                x += 1
                rx += 1
        else:
            print("\nUh oh! The password you typed was incorrect 3 times!")
            sleep(2)
            print("Please try again later!")
            exit()
        
        f.close()
        
except Exception as e:
    password = input("\n Error with Password Manager. Possible solutions: allow access to C-DRIVE to save passwords, remove JaskaranOS folder from CDrive (may have corrupted after update). Meanwhile, please type in a temp password below\n> ") ## C:// unaccessible or not working, can't store data
    print(e)
print("Type 'help' for commands!\n\n")

user = getpass.getuser()
while True:
    
    a = str(input(user+"@"+socket.gethostname()+" > "))

# now the processing!

 # Help
    if a == "help":
        print(Back.BLUE + "Welcome to JaskaranOS help! Here are the available commands:\nhelp - Opens this\necho (string) - Echoes (repeats) back\nls (string) - List Files in Directory\ntext (string/directory) - Creates a new text file\nwrite (string) - Write to a text file. First write what you want, then it will ask you for the directory. Use \ n (without spaces) for a new line.")
        print("read (directory) - Reads text file specified by user.")
        print("run (directory) - Runs an application.")
        print("ping (website) - Pings a website to check if it can connect.\nsay (input) - Text To Speech engine. Change voice by saying 'say male' or 'say female'")
        print("username / user - Checks your username. Requires GETPASS module.")
        print("password / pass - Asks for password to continue. Doesn't work on some compilers.")
        print("cmd (input) - Used windows CMD to run advanced commands.")
        print("pip install (input) - Installs python modules using PIP.")
        print("download (url) - Downloads and installs a URL.")
        print("boot - Change your boot options(enable/disable it)")
        print("credits - Opens up the credits pages.")
        print("email - Opens up the JOS Gmail E-Mail client")
        print("translate - Opens up the JOS Translator, based on Google Translate")
        print("sudo - Opens up sudo configuration.")
        print("configure - Opens up the JOS configuration.")
        print("time - Gets current time.")
        print("shut down - Shuts down JOS")
        print("restart - Restarts JOS")
        print("user - Shows Device Username")
        print("device - Shows Device Hostname")
        print("update notes - Shows the latest update notes.")
        print("ram usage - Shows current RAM usage & total ram")
        print("cpu usage - Shows current CPU usage")
        print("speed test - Check your current internet speed.")
        print(Back.RESET)

 # Echo
    elif a[0:5] == "echo " or a[0:5] == "print":
        echo = a[5:]
        print(echo)

 # List files
    elif a[0:3] == "ls ":
        ls = str(a[3:])
        try:
            okay = '\n'.join(map(str, (os.listdir(ls))))
            print("Files in", ls+":\n\n\nl"+okay)
        except FileNotFoundError:
            print("Folder Not Found!")
    
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
        
    elif a[0:7] == "colour " or a[0:6] == "color " or a == "color " or a == "colour ":
        if a[0:7] == "colour ":
            color = a[7:]
        elif a == "color " or a == "colour ":
            print("Please specify a "+Fore.GREEN+"colour."+Fore.RESET)
            color = "(from colorama import colourname)\nERROR OCCURED: CANNOT IMPORT COLOR ERROR FROM COLORAMA"
        else:
            color = a[6:]
        print("Colour is now", color)
        try:
            print(Fore.color + "Testing to check colour..")
        except:
            print("\nError: Color system is currently " + Fore.RED + "offline. " + Fore.RESET + "Please try again later. For more information, type:\n'"+Fore.BLUE+"color-offline"+Fore.RESET+"'")
    
    elif a == "color-offline" or a == "colour-offline":
        print("The colour system is currently"+Fore.RED+" offline"+Fore.RESET+". This is because the "+Fore.GREEN+"colour"+Fore.BLUE+" system "+Fore.RESET+"is currently undergoing heavy development. Please check back in future updates.")
        
        
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
                with open('C://JaskaranOS/password.txt', 'r') as f:
                    lines = f.readlines()
                    print(lines)
            except Exception as e:
                print("Invalid operation. Password file cannot be accessed.")
                sleep(1)
                print(e)
            
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
    
    elif a == "web":
        webpageViewer()
        
    elif a[0:8] == "install " or a[0:9] == "download ":
        if a[0:8] == "install ":
            asd = a[8:]
        elif a == "install " or a == "download ":
            print(Fore.RED+"Invalid. Please specifiy a download link.")
        else:
            asd = a[9:]
        
        if not asd[0:4] == "http":
            print(Fore.RED + "Error. Cannot get webpage "+Fore.BLUE+asd+Fore.RESET+Fore.RED+". Please make sure URL begins with: http"+Fore.RESET)
        else:
            response = requests.get(asd)
            print("File name? Please include extention.")
            fname = input("> ")
            open("C://JaskaranOS/"+fname, "wb").write(response.content)
            print("Successfully downloaded URL "+asd+" to: C://JaskaranOS/"+fname+". Would you like to open the folder?")
            yesorno = input("> ")
            if yesorno == "yes":
                print("Opening Folder... please stand by.")
                os.startfile(os.path.realpath("C://JaskaranOS"))
    
    elif a == "wwazzup" or a == "whats up" or a == "what's up" or a == "yo":
        print("Hi.")
        
    elif a == "lol" or a == "xd" or a == "xD" or a == "XD":
        print("What's so funny?")
        

    elif a == "boot":
        if os.path.exists("C://JaskaranOS/boot"):
            # Boot exists. Disable it!
            # must be empty directory or won't delete
            os.rmdir("C://JaskaranOS/boot")
            print("\nDisabled boot. Please restart for the changes to take effect.\n")
        else:
            # Boot doesn't exist. Enable it!
            os.mkdir("C://JaskaranOS/boot")
            print("\nEnabled boot. Please restart for the changes to take effect.\n")
    
    elif a == "":
        print(Fore.RED+"Please input something to process."+Fore.RESET)
        
    elif a == "credits":
        print("Thank you for taking your time to have a look at the credits.")
        try:
            import webbrowser
        except:
            print("Uh oh! Module  Webbrowser cannot be imported! Please install it")
        sleep(1)
        print("This operating system was created by Jaskaran. We are now opening the official link for JaskaranPython so that you can view more python projects. We are then going to be opening the github page for JaskaranOS, so you can see the contributors.")
        sleep(5)
        webbrowser.open("https://jaskaranpython.glitch.me")
        sleep(2)
        webbrowser.open("https://github.com/TheAnister/JaskaranOS")
        
    elif a == "pyexe" or a == "exe":
        print("Running python 'auto-py-to-exe'...")
        os.system("auto-py-to-exe")
    
    elif a == "l bozo" or a == "l":
        print(Fore.RED + "L bozo." + Fore.RESET)
    
    elif a == "email":
        email()
    
    elif a == "translate":
        try:
            from googletrans import Translator
            from pprint import pprint
        except:
            os.system("pip install googletrans==3.1.0a0")
            os.system("pip install pprint")
            from googletrans import Translator
            from pprint import pprint
            
        translator = Translator()
        tt = input("What would you like to translate into English?\n> ")
        src = input("Please enter the language code (e.g en = english, de = german, etc.)\n> ")
        try:
            translation = translator.translate(str(tt), src=str(src))
            print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
        except Exception as e:
            print("Error whilst translating.")
            sleep(1)
            print(e)
    elif a == "sudo":
        print("JOS sudo 1.1")
        print(Fore.GREEN+"available sudo command:\nsudo apt"+Fore.RESET)
    
    elif a == "sudo apt":
        print("JOS sudo apt 1.1")
        print("apt has super cow powers")
        print(Fore.GREEN+"available sudo apt commands:\nsudo apt install\nsudo apt remove\nsudo apt update\nsudo apt upgrade"+Fore.RESET)
    
    elif a == "sudo apt install":
        print("JOS sudo apt install 1.1")
        print(Fore.RED+"please specify what to install :)"+Fore.RESET)
    elif a == "sudo apt remove":
        print("JOS sudo apt remove 1.1")
        print(Fore.RED+"please specify what to remove :)"+Fore.RESET)
    elif a == "sudo apt update":
        print("JOS sudo apt update 1.1")
        print(Fore.RED+"please specify what package to update :)"+Fore.RESET)
    elif a == "sudo apt upgrade":
        print(Fore.RED+"Attempting to get latest version of JOS..")
        sleep(1)
        print("Error. Attempting manual process..\n")
        input(Fore.RED+"Are you sure you would like to upgrade to the latest JOS? Press enter to proceed."+Fore.RESET)
        import webbrowser
        webbrowser.open("https://github.com/TheAnister/JaskaranOS")
    
    elif a[0:17] == "sudo apt install ":
        print("JOS sudo apt install 1.1")
        print(Fore.RED+"package unavailable :)"+Fore.RESET)
    
    elif a[0:16] == "sudo apt remove ":
        print("JOS sudo apt remove 1.1")
        print(Fore.RED+"package does not exist, is it installed?"+Fore.RESET)
        
    elif a[0:16] == "sudo apt update ":
        print("JOS sudo apt update 1.1")
        print(Fore.RED+"error: specified package not found, or is already updated to latest version."+Fore.RESET)
    
    elif a == "configure":
        print("configuration of JOS")
        print(Fore.GREEN+"configure incorrect-command - when command not found, search query on google.")
        print(Fore.RESET)
    
    elif a == "configure incorrect-command":
        if incorrectcmd == 1: # if enabled
            incorrectcmd = 0
            os.rmdir("C://JaskaranOS/configuration/incorrect-password")
            print("now disabled.")
        else:
            incorrectcmd = 1
            os.mkdir("C://JaskaranOS/configuration/")
            os.mkdir("C://JaskaranOS/configuration/incorrect-password")
            print("now enabled.")
        print("done.")
    
    elif a == "time":
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        print("Current Time:", current_time)
        
    elif a == "restart":
        print("Restarting...")
        sleep(2)
        if input("\nWould you also like to restart your computer?\n> ") == "yes":
            print("Restarting computer... 5 second countdown")
            sleep(5)
            os.system("shutdown /r /t 1")
        print("Shutting down all processes..")
        sleep(0.2)
        print("Success\n")
        os.execl(sys.executable, sys.executable, *sys.argv)
        
    elif a == "stop" or a == "shutdown" or a == "shut down" or a == "exit":
        print("Shutting down..")
        sleep(2)
        if input("\nWould you also like to shut down your computer?\n> ") == "yes":
            print("Shutting down your computer... 5 second countdown")
            sleep(5)
            os.system("shutdown /s /t 1")
        print("Shutting down all processes..")
        sleep(0.2)
        print("Success\n")
        exit()
        
    elif a == "device":
        print("Your device name is currently", socket.gethostname())
    
    elif a == "disk usage":
        try:
            import shutil
            from hurry.filesize import *
        except:
            os.system("pip install shutil")
            import shutil
            os.system("pip install hurry.filesize")
            from hurry.filesize import *

        total, used, free = shutil.disk_usage("/")

        print("Total: "+size(total, system=verbose))
        print("Used: "+size(used, system=verbose))
        print("Free: "+size(free, system=verbose))
        print("\nTotal: "+size(total, system=alternative))
        print("Used: "+size(int(used), system=alternative))
        print("Free: "+size(int(free), system=alternative))
    
    elif a == "world cup":
        import webbrowser
        webbrowser.open("https://www.google.com/search?q=world+cup")
    
    elif a == "ur mom" or a == "your mom" or a == "you dad" or a == "ur dad":
        print("I'd say the same to you, but you don't have one.")
    
    elif a == "cpu" or a == "cpu usage":
        try:      
            import os
            import psutil
        except:
            print("Cannot get module: psutil. Auto-installing.. please wait..")
            os.system("pip install psutil")
            import psutil
        load1, load5, load15 = psutil.getloadavg()
        print(load1, load5, load15)
        cpu_usage = (load15/os.cpu_count()) * 100
        print("The CPU usage is", str(cpu_usage)+" percent")
    
    elif a == "ram" or a == "ram usage":
        try:
            import psutil
        except:
            print("Error getting module: psutil. Auto-installing.. please wait..")
            os.system("pip install psutil")
            import psutil
        try:
            rampercent = psutil.virtual_memory()[2]
            ramused = psutil.virtual_memory()[3]/1000000000
            ramtotal1 = int(ramused)/int(rampercent)
            ramtotal = ramtotal1*100
            winram1 = ramtotal/1000000000
            winram = winram1*1074000000
        except:
            print("error, psutil not working?")
        if ramtotal < ramused:
            print("Error! RAM being used too fast, ramused is larger than ramtotal. Retrying...")
            rampercent = psutil.virtual_memory()[2]
            ramused = psutil.virtual_memory()[3]/1000000000
            ramtotal1 = int(ramused)/int(rampercent)
            print(ramtotal1)
            ramtotal = ramtotal1*100
            print(ramtotal)
            winram1 = ramtotal/1000000000
            print(winram1)
            winram = winram1*1074000000
            print(winram)
        print('RAM memory % used:', rampercent)
        print('RAM Used (GB):', ramused)
        print('RAM Total (GB):', ramtotal)
        print('Windows RAM Total (GB):', round(winram)) ## just in case of an error, round() is better as the memory is likely to be a whole number
        print("\nWhy does windows identify RAM differently? this is because windows measures it in gigibytes not gigabytes, there is a difference")
    
    
    elif a == "speed test" or a == "internet speed test" or a == "internet" or a == "speedtest" or a == "internet speedtest" or a == "ping":
        print("Checking internet speed.....")
        try:
            import speedtest  
        except:
            os.system("pip install speedtest-cli")
            import speedtest
        st = speedtest.Speedtest()
  
        option = int(input('''What speed do you want to test:  
  
        1) Download Speed  
  
        2) Upload Speed  
  
        3) Ping 
        ''' + "\n> "))
  
  
        if option == 1 or option == "1":  
            print("Checking download speed...")
            download = st.download()
            print(str(int(st.download())/1049000) + "MB")

            print("Done.")
  
        elif option == 2 or option == "2": 
            print("Checking upload speed...")
            upload = st.upload()
            print(str(int(st.upload())/1049000) + "MB")

            print("Done.")
  
        elif option == 3 or option == "3":  
            print("Pinging..")
            servernames =[]  
  
            st.get_servers(servernames)  
  
            print(st.results.ping)
            print("Done.")
            if ping == 0 or ping == "0":
                print("Hang on a minute! Your ping is 0! This may be because of an error!")
  
        else:
  
            print("Please enter the correct choice !") 
    
        
    
    
    
    else:
        if a == "update notes":
            ## update notes
            print("- Added in AutoBoot v2 for faster boot.")
            print("- Added 'restart', 'shutdown', 'user', 'device', 'disk usage', 'ram', 'cpu' & 'speedtest' commands for easier access to basic commands that you would find on a normal OS.")
            print("- Updated 'sudo' to 1.1")
            print("- Updated 'Auto-Install-Module' for the program to run faster for the first time")
            print("- Bug fixes for speedtest")
            print("- Changed from GUI to console-based")
            
            
        if incorrectcmd == 1:
            import webbrowser
            webbrowser.open("https://www.google.com/search?q="+str(a)+"&oq=google&aqs=JOS")
        else:
            print(Fore.RED + "Unknown command. Please type in 'unknown command' for more information." + Fore.RESET)
        
    
