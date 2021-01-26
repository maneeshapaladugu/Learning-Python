#This is a guess the number game
import random

print('Enter your name')
name = input()

print('Well, ' +name+ 'I am thinking of a number between 1 and 20')
secretNumber = random.randint(1,20)

for guessesTaken in range(1,7): #ranges between 1 to 6
    print('Take a guess')
    guess = int(input())

    if guess > secretNumber:
        print('Your guess is too high')
    elif guess < secretNumber:
        print('Your guess is too low')
    else:
        break

if guess == secretNumber:
    print('Good job ' +name+ '!! You guessed my number in ' +str(guessesTaken)+ ' guesses!')
else:
    print('6 Chances for guess is over. The number i was thinking of was ' +str(secretNumber))
