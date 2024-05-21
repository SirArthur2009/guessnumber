import random

import time

def addToken(amount):
    file = open('C:\\Users\\levig\\Documents\\js-coding-for-teens\\Python_modules\\Tokens.tok', 'r')
    number = file.readline()
    try:
        number = int(number)    
        number += amount
        print('Token succesfully added')
    except:
        print('Token not added, sorry')
    file.close()
    file = open('C:\\Users\\levig\\Documents\\js-coding-for-teens\\Python_modules\\Tokens.tok', 'w')
    file.write(str(number))
    print('Current balance: ' + str(number))
def getTokens():
    file = open('C:\\Users\\levig\\Documents\\js-coding-for-teens\\Python_modules\\Tokens.tok', 'r')
    num = int(file.readline)
    file.close()
    return num
def takeTokens(amount):
    file = open('C:\\Users\\levig\\Documents\\js-coding-for-teens\\Python_modules\\Tokens.tok', 'r')
    num = int(file.readline())
    num2 = num - amount
    if num2 < 0:
        print('Balance to low')
    else:
        num = num2
    file.close()
    file = open('C:\\Users\\levig\\Documents\\js-coding-for-teens\\Python_modules\\Tokens.to', 'w')
    file.write(str(num))

def findNumber():
    print("Welcome to find the Number")
    print("You will be playing against the PC")
    level = levelBought()
    if (level == 'h') == False:
        choice = input('Would you like to buy a level? ')
        if choice in ['y', 'yes']:
            print('level bought: ' + level)
            levelToBuy = input('Which level would you like to buy? m/5 h/7')
            if levelToBuy == 'm' and level == 'e':
                pass
    difficulty = pickDifficulty()

    GameWon = False
    turn = random.randint(0, 1)
    number = random.randint(1, 100)
    computerGuesses = []
    while GameWon == False:
        if turn == 0:
            guess = playerGuess()
        elif turn == 1:
            print("Computer guess...")
            time.sleep(1)
            guess = computerGuess(difficulty, computerGuesses)

            
            print("The computer guesses ", str(guess))

        if guess == number:
            if turn == 0:
                print("Player wins")

            elif turn == 1:
                print("Computer wins")
            GameWon = True
        elif guess > number and turn == 1:
            computerGuesses.append([guess, "h"])
            turn = 0
        elif guess < number and turn == 1:
            computerGuesses.append([guess, "l"])
            turn = 0
        elif guess >number and turn == 0:
            print("Too high")
            turn = 1
        elif guess < number and turn == 0:
            print("Too low")
            turn = 1

def levelBought ():
    file = open('C:\\Users\\levig\\Documents\\js-coding-for-teens\\Python_modules\\LevelBought.lvlA', 'r')
    level = file.readline()
    file.close()
    return level

def pickDifficulty():
    pickDifficulty = False
    levelAvailable = levelBought()
    while pickDifficulty == False:
        print('You can play ' + levelAvailable + ' and all easier difficulties')
        difficulty = input("What difficulty would you like to play today? (easy, medium, hard)\n").lower()
        if difficulty in ["e", "easy", "1"] and levelAvailable in ['e', 'm', 'h']:
            difficulty = "easy"
            pickDifficulty = True
        elif difficulty in ["m", "medium", "2"] and levelAvailable in ['m', 'h']:
            difficulty = "medium"
            pickDifficulty = True
        elif difficulty in ["h", "hard", "3"] and levelAvailable in ['h']:
            difficulty = "hard"
            pickDifficulty = True
        else:
            print("Choice not reconized please try again")
    return difficulty         

def playerGuess():
    guessing = True
    print("Your turn to guess")
    while guessing:
        guess = input("What's your guess? ")
        try:
            int(guess)
            guessing = False
        except:
            print("try again, be sure to enter a number between 1 and 100")
            
    
    return int(guess)

def computerGuess(difficulty, previousGuesses):
    hGuesses = [101]
    lGuesses = [0]
    lGuess = 0
    hGuess = 100
    guess = 0
    if difficulty == "easy":
        guess = random.randint(0, 100)
    elif difficulty == "medium":
        for i in previousGuesses:
            if i[1] == "l":
                lGuesses.append(i[0])
            elif i[1] == "h":
                hGuesses.append(i[0])

        lGuesses.sort()
        hGuesses.sort()

        try:
            guess = random.randint(lGuesses[-1], hGuesses[0])
        except:
            guess = int(random.randint(lGuess, hGuess))

    elif difficulty == "hard":
        for i in previousGuesses:
            if i[1] == "l":
                lGuesses.append(i[0])
            elif i[1] == "h":
                hGuesses.append(i[0])

        lGuesses.sort()
        hGuesses.sort()
        try:
            guess = round((lGuesses[-1]+hGuesses[0])/2)
        except:
            pass
            

    else:
        print("Difficulty setting not reconized")

    return int(guess)

findNumber()
        
