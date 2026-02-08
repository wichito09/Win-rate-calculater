import calculations
import time
import sys
import requests

VERSION = '0.0.1'


def greet():
    '''greets the user, like a logo and a message and Version'''

    print(r''' /$$      /$$ /$$           /$$                  /$$$$$$   /$$$$$$ 
| $$  /$ | $$|__/          | $$                 /$$$_  $$ /$$__  $$
| $$ /$$$| $$ /$$  /$$$$$$$| $$$$$$$   /$$$$$$ | $$$$\ $$| $$  \ $$
| $$/$$ $$ $$| $$ /$$_____/| $$__  $$ /$$__  $$| $$ $$ $$|  $$$$$$$
| $$$$_  $$$$| $$| $$      | $$  \ $$| $$  \ $$| $$\ $$$$ \____  $$
| $$$/ \  $$$| $$| $$      | $$  | $$| $$  | $$| $$ \ $$$ /$$  \ $$
| $$/   \  $$| $$|  $$$$$$$| $$  | $$|  $$$$$$/|  $$$$$$/|  $$$$$$/
|__/     \__/|__/ \_______/|__/  |__/ \______/  \______/  \______/ ''')
    print(VERSION)
    print("This is a calculator that will calculate your win percentage")
    print('the program will not check for any problems till the end so if you put a letter it will repeat till the end')


def checknum(num):
    '''checks if number is a str if it is turns it into a float'''

    try:
        num = float(num)
        return num
    
    except ValueError:
     print('ERROR: please enter a number')
     return True


def impossiblecheck(totalgames,wins):
    '''checks for impossible scenerious like if win execeeds totalgames and if wins or total games are at 0'''

    if wins > totalgames:
        print("stop trying to break the system")
        return True
    elif totalgames <= 0:
        print('stop it!')
        return True
    else:
        return False

def numask():
    '''asks for a numbers then checks if numbers are good'''

    print("To start off, input the total amount of game played!")
    totalgames = input("-> ")

    print('now enter the amount of games you won out of the total')
    wins = input('-> ')

    numberscomp = [totalgames,wins]
    return numberscomp


def main():
    '''runs the main functioninality of this project'''

    greet()
    numberscomp = numask()
    numberscomp[0] = checknum(numberscomp[0])
    numberscomp[1] = checknum(numberscomp[1])

    while impossiblecheck(numberscomp[0],numberscomp[1]):
        numberscomp = numask()
        numberscomp[0] = checknum(numberscomp[0])
        numberscomp[1] = checknum(numberscomp[1])
    finalnum = round(calculations.calculatewinper(numberscomp[0],numberscomp[1]))
    print(f'your win rate is {finalnum}%!')
    time.sleep(10)
    sys.exit(0)


main()