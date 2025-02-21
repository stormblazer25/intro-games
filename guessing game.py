import random
answer = random.randrange(1,100)
number_of_guesses = 0
while True:
    guess = int(input('Enter any number between[1,100]: '))
    number_of_guesses = number_of_guesses + 1
    if guess < answer:
        print('Too low try again!')
    elif guess > answer:
        print('Too high try again!')
    else:
        break
print("That's it, you guessed it right!")
print(f'You took {number_of_guesses} guesses')
