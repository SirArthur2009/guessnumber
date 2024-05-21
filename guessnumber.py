import random

def chooseNumber():
  return random.randint(0, 100)
def guessNumber(target_number):
    print("Guess a number between 0 and 100")
    guess = int(input())
    if guess == target_number:
        print("You guessed the number!")
        return True
    elif guess > target_number:
        print("Your guess was too high")
        return 'high'
    elif guess < target_number:
        print("Your guess was too low")
        return 'low'
    else:
        print("You did not guess the number")
        return 'error'


def main():
    target_number = chooseNumber()
    while True:
        try:
            result = guessNumber(target_number)
            if result == True:
                print("Congratulations!")
                break
            elif result == 'high':
                print("Please try a lower number")
            elif result == 'low':
                print("Please try a higher number")
            else:
                print("An error occurred")
        except Exception as e:
            print("An exception occurred:", e)

if __name__ == "__main__":
    main()
