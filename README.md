# JaskaranOS
JaskaranOS - A command-based operating system, built on Python

# Description
JaskaranOS (a.k.a JOS) is a command-based operating system that was made on Python by Jaskaran. Work started on it on 27/09/2022, and the first version was released on 01/10/2022. It is an open-source operating system that does most basic stuff that you would find on a UNIX shell, and if you want, you can run CMD commands on it.

# Adding your own commands
## Locally
To add in your own commands, you first need to download the latest version of JaskaranOS source code [here](https://github.com/TheAnister/JaskaranOS/releases/). Inside the `source code.zip` file, you will find a file named `main.py`. Extract that file to any location you want, and then open it up using a text editor. Scroll all the way down, and then just before the last ```else```, write your own command using this format:
```
  elif a == "test":
    print("This is just a test.")
```
If your program uses input taken from when the user types something in, please use this format;
```
  elif a[5] == "test ":  ## a[5] means first 5 characters including space
     print("Hello," + a[5:]) ## a[5:] means all characters after the 5th character including the space
```     

## Publishing your own commands
To publish your own command using [this form](https://forms.gle/E51v22UuDgpYzEkU9). <--- This form will not be checked starting 24/02/2023 as Jaskaran is retiring from JOS. Contributors will need another form.

## Compiling your program
If you would like to compile your program into a functioning .exe file, ensure that you have all the correct modules installed, then simply type `exe` into JaskaranOS and an automatic `python-to-exe` program will run.

# More Python
For more python projects, be sure to visit us on our site: [JaskaranPython](https://jaskaranpython.glitch.me)

Here is our backup-site: [PyJaskaran](https://TheAnister.github.io)

# Statistics
This program is no easy feat. It took two weeks before the first update was ready to be released, with four hours a day being dedicated to finishing this program. Now that it has been completed, the main contributor (Jaskaran) dedicated all his efforts into making this the best Python OS yet.

# R.I.P ?
Jaskaran is retiring from Jaskaran Operating System, starting 24/02/2023. His last contribution was the JaskaranOS: Flex version (JOS5). This github will now rely soley on other contributors.
