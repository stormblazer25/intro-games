print('Welcome to my hardest quiz for you!')
answer = input("Are you ready to enter the world's hardest quiz? (yes/no): ")
score = 0
total_questions = 5

if answer.lower() == 'yes':
    answer = input('Question 1: What is your favourite programming language? ')
    if answer.lower() == 'python':
        score += 1
        print('Correct! :)')
    else:
        print('Wrong answer! :(')
        print('The correct answer is obviously python')

    answer = input('Question 2: Which country has the highest life expectancy? ')
    if answer.lower() == 'hong kong':
        score += 1
        print('Correct! :)')
    else:
        print('Wrong answer! :(')
        print('The correct answer is hong kong')

    answer = input('Question 3: Where is the flag hoisted on Independence Day? ')
    if answer.lower() == 'red fort':
        score += 1
        print('Correct! :)')
    else:
        print('Wrong answer! :(')
        print('The correct answer is red fort')

    answer = input('Question 4: How many faces does a Dodecahedron have? ')
    if answer.lower() == '12':
        score += 1
        print('Correct! :)')
    else:
        print('Wrong answer! :(')
        print('The correct answer is 12')

    answer = input('Question 5: Which country has the most islands habitat or inhabited ')
    if answer.lower() == 'sweden':
        score += 1
        print('Correct! :)')
    else:
        print('Wrong answer! :(')
        print('The correct answer is sweden')

print("Thank you for playing the world's hardest quiz")
mark = (score/total_questions) * 100
print('Your mark is', mark, '%')
print('Bye, sometime again too! :)')

