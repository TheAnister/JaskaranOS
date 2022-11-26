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
    import requests
    import platform
    import subprocess
    import pyAesCrypt
    import getpass

except:
    print("We could not import the following modules: 'getpass', 'urllib', 'requests', 'platform', 'subprocess' and/or 'pyAesCrypt'. Please install them to continue. Auto-installing it in 5 seconds...")
    sleep(5)
    os.system('python -m pip install pyAesCrypt getpassw urllib requests platform subprocess')
    exit()
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
    print("Error installing datetime. Fixing issues... (Fix 1/2)")
    try:
        os.system('python -m pip install datetime')
    except:
        ## hacker.!!!.
        print("Error installing module (module already there / corrupt?). Fixing issues... (Fix 2/2)")
        sleep(5)
        print(Fore.RED + "Error occured! This was not meant to happen! You have corrupted the system! Automatically exiting..." + Fore.RESET)
        try:
            exit()
        except:
            print(Fore.RED + "ERROR OCCURED! CANNOT EXIT!")
            while True:
                print("Error Cannot exit! Timing process out, please wait!")
            while True:
                print("Error Cannot exit! Timing process out, please wait!")
            while True:
                print("Error Cannot exit! Timing process out, please wait!")
            while True:
                print("Error Cannot exit! Timing process out, please wait!")
            while True:
                print("Error Cannot exit! Timing process out, please wait!")
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
if os.path.exists("C://JaskaranOS/boot") == True:
    import itertools
    import threading
    import time
    import sys
    print("Booting...")
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
    sleep(3)
    done = True
else:
    print("Please wait, loading!")
    print("decrypting password...")
    try:
        passwordd = "vTWMDsvbAnlFmFNIRRML"
        pyAesCrypt.decryptFile("C://JaskaranOS/encrypted-password.txt.aes", "dataout.txt", passwordd)
    except Exception as e:
        print("Error whilst decrypting/accessing encrypted file.")
        print(e)
    print("done!\nreading file...")
    with open("dataout.txt") as f:
        urpass = f.read()
    print("done!\ndeleted decrypted file...")
    os.remove("dataout.txt")
    print("done!\nloading password manager...")
    sleep(0.5)

import socket

sleep(0.5)
#if firstuser
try:
    if os.path.exists("C:\JaskaranOS") == True:
        firstuser = "false"
        print(Fore.GREEN + "\n              Welcome back to JOS - Jaskaran's Operating System\n" + Fore.RESET)
    else:
        print("")
        os.mkdir("C:\JaskaranOS")
        firstuser = "true"
except:
    print(Fore.RED + "Cannot access C:\ Drive. Please ensure that you have access to it in order to use commands such as "+ Fore.BLUE + "write" + Fore.RED + "." + Fore.RESET)


existss = "0"
## Password login/creator
sleep(3)
try:    
    if firstuser == "true":
        print(Fore.CYAN + "\n                Welcome to JaskaranOS! This is a command-based operating system. For help on commands, please type in: 'help' in the command line!\nThis OS has been tested on a Windows Machine. It will soon be able to be run on it's own computer" + Fore.RESET)
        print("\n     Please set a password below!")
        password = input("> ")
        with open('C://JaskaranOS/password.txt', 'w') as f:
            f.write(str(password))
            
        print("Successfully set password!\n")
        ## encrypt password file
        import pyAesCrypt
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
    
    a = input(user+"@"+socket.gethostname()+" > ")

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
        with open('C://JaskaranOS/password.txt', 'r') as f:
            try:
                lines = f.readlines()
                print(lines)
            except:
                print("Invalid operation. Password file corrupt.")
            
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
        print("Please input something to process.")
        
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
        print("JOS sudo 1.0")
        print("available sudo command:\nsudo apt")
    
    elif a == "sudo apt":
        print("JOS sudo apt 1.0")
        print("apt has super cow powers")
        print("available sudo apt commands:\nsudo apt install\nsudo apt remove\nsudo apt update\nsudo apt upgrade")
    
    elif a == "sudo apt install":
        print("JOS sudo apt install 1.0")
        print("please specify what to install :)")
    elif a == "sudo apt remove":
        print("JOS sudo apt remove 1.0")
        print("please specify what to remove :)")
    elif a == "sudo apt update":
        print("JOS sudo apt update 1.0")
        print("please specify what to update :)")
    elif a == "sudo apt upgrade":
        input("Are you sure you would like to upgrade to the latest JOS? Press enter to proceed.")
        import webbrowser
        webbrowser.open("https://github.com/TheAnister/JaskaranOS")
    
    elif a[0:17] == "sudo apt install ":
        print("JOS sudo apt install 1.0")
        print("package unavailable :)")
    
    elif a[0:16] == "sudo apt remove ":
        print("JOS sudo apt remove 1.0")
        print("package does not exist, is it installed?")
        
    elif a[0:16] == "sudo apt update ":
        print("JOS sudo apt update 1.0")
        print("error: specified package not found, or already updated.")
    
    elif a == "configure":
        print("configuration of JOS")
        print("configure incorrect-command - when command not found, search query on google.")
    
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
        
        
    else:
        if incorrectcmd == 1:
            import webbrowser
            webbrowser.open("https://www.google.com/search?q="+str(a)+"&oq=google&aqs=JOS")
        else:
            print(Fore.RED + "Unknown command. Please type in 'unknown command' for more information." + Fore.RESET)
        
    
