# CONSOLE CALCULATOR #


# This function make initial greeting #
def firstStart():
    print('Sup mate!\n'
          'Welcome to my calculator\n')


# This function add two user numbers #
def add(firstNum, secondNum):
    return firstNum + secondNum


# This function subtract two user numbers #
def subtract(firstNum, secondNum):
    return firstNum - secondNum


# This function multiply two user numbers #
def multiply(firstNum, secondNum):
    return firstNum * secondNum


# This function divide two user numbers #
def divide(firstNum, secondNum):
    return firstNum / secondNum


# This function convert user input to int #
def remakeStrToInt(number):
    rNumber = int(number)
    return rNumber


# This function executes the logic of my program #
def mainApp():
    while True:

        # Here we take two user numbers #
        firstNum = input('Enter first number: ')
        secondNum = input('Enter second number: ')

        # Here we allow the user to choose the operation #
        option = input('\nAvailable operations:\n'
                       '\'+\' - add numbers.\n'
                       '\'-\' - subtract numbers.\n'
                       '\'*\' - multiply numbers.\n'
                       '\'/\' - divide numbers.\n'
                       '\'!\' - leave calculator.\n'
                       '\nSelect operation: ')

        # Here start logic of our program #

        # Here we check user numbers #
        if firstNum == '' or secondNum == '':
            print('You didn\'t enter an numbers, try again.')
            mainApp()
        elif firstNum != '' and secondNum != '':

            # Here we call function 'remakeToString' to convert numbers to int #
            rFirstNumber = remakeStrToInt(firstNum)
            rSecondNum = remakeStrToInt(secondNum)

            # Here we check user option #
            if option == '':
                print('You didn\'t enter an option, try again.')
                mainApp()
            elif option == '+':
                print(f'{rFirstNumber} + {rSecondNum} =', add(rFirstNumber, rSecondNum))
            elif option == '-':
                print(f'{rFirstNumber} - {rSecondNum} =', subtract(rFirstNumber, rSecondNum))
            elif option == '*':
                print(f'{rFirstNumber} * {rSecondNum} =', multiply(rFirstNumber, rSecondNum))
            elif option == '/' and rSecondNum == 0:
                print('You wanna subtract to zero, here it\'s impossible, try again.')
                mainApp()
            elif option == '/':
                print(f'{rFirstNumber} / {rSecondNum} =', divide(rFirstNumber, rSecondNum))
            else:
                print('You didn\'t enter an option, try again.')
                mainApp()


# Here we call our functions #
firstStart()
mainApp()
