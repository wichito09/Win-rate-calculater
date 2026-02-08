import calculations


VERSION = '0.0.1'


def greet():

    '''greets the user, like a logo and a message and Version'''

    print('add logo here')

    print(VERSION)

    print("This is a calculator that will calculate your win percentage")


def checknum(num):

    '''checks if number is a str if it is turns it into a float'''

    try:

        num = float(num)

        return False

    except ValueError:

     print('ERROR: please enter a number')

     return True


def impossiblecheck(totalgames,wins):

    '''checks for impossible scenerious like if win execeeds totalgames and if wins or total games are at 0'''

    if wins > totalgames:

        print("stop trying to break the system")

        return True

    elif wins <= 0 or totalgames <= 0:

        print('stop it!')

        return True

    else:

        return False

def numask():

        '''asks for a numbers then checks if numbers are good'''

        print("To start off, input the total amount of game played!")

        while True:

            totalgames = input("-> ")

            while checknum(totalgames):

                totalgames = input("-> ")

            break


        print('now enter the amount of games you won out of the total')

        while True:

            wins = input('-> ')

            while checknum(wins):

                wins = input("-> ")

            break

        numberscomp = [totalgames,wins]

        return numberscomp


def main():
    '''runs the main functioninality of this project'''
    greet()

    numberscomp = numask()

    while impossiblecheck(numberscomp[0],numberscomp[1]):

       numberscomp =  numask()

    print(numberscomp)

       

main()

