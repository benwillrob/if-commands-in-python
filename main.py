import pyfiglet
import os
import time

from pyfiglet import Figlet

ascii_banner = pyfiglet.figlet_format("Welcome  to  my  game!")
print(ascii_banner)

input("\n \n \n Press ENTER Key To Procede.")

os.system('cls')

name = input("What is your name?\n")

os.system("cls")

input("Hello "+name)
os.system("cls")

age = input("How old are you? \n")

os.system("cls")


if int(age) < 18:
    location = input(name+", I hear that you are " +age+ ". Where do you live!!!!1!!11!! \n")
    os.system("cls")

    input("Ok " +name+ ", lets have seggs in " +location)
    os.system("cls")
    ascii_banner = pyfiglet.figlet_format(name)
    print(ascii_banner)
    ascii_banner = pyfiglet.figlet_format("got molested")
    print(ascii_banner)
    input()
    exit()

else:
    input("ok nvrmnd")
    exit()



