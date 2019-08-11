import random

#print instructions
print("We're going to play a guessing game")
print("I'm going to pick a secret number and you have to guess it")
print("Before each guess I will tell you the range in which you should guess")

#initialize variables
number_of_guesses = 0
lower_bound = 1
upper_bound = 100
secret_number = random.randint(lower_bound,upper_bound)
guess = lower_bound - 1

#create a while loop, while guess is not equal to secret number
while guess != secret_number:

    #computer gives the range of the guess
    print("Guess a number between" , lower_bound , "and" , upper_bound)

    #user can guess computer tells them whether it's correct
    guess = int(input("Guess: "))

    #says when guess is too high or too low
    if guess > secret_number:
        print("Guess lower")
        upper_bound = guess - 1
    elif guess < secret_number:
        print("Guess higher")
        lower_bound = guess + 1

    #user guesses until they get it right

    #computer tracks number of guesses
    number_of_guesses = number_of_guesses + 1

#computer tells secret number and number of guesses
print("You got it in" , number_of_guesses , "guesses. The secret number is" , secret_number)
