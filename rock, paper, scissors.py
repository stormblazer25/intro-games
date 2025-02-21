import random
options = ['Rock', 'Paper', 'Scissors']
while True:
    user_choice = input('Choose Rock, Paper or Scissors: ')
    computer_choice = random.choice(options)
    print('Your choice: ', user_choice)
    print('Computer chose: ', computer_choice)
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice.lower() == 'rock' and computer_choice == 'Scissors':
        print('You win!')
    elif user_choice.lower() == 'paper' and computer_choice == 'Rock':
        print('You win!')
    elif user_choice.lower() == 'scissors' and computer_choice == 'Paper':
        print('You win!')
    else:
        print('Computer wins!')





