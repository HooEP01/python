import random
import sys


# generate a number 1 to 10
answer = random.randint(int(sys.argv[1]), int(sys.argz[2]))

# input from user


# check that input is number 1 ~ 10
while True:
    try:
        guess = int(input('guess a number 1~10: '))
        if 0 < guess < 11:
            if guess == answer:
                print('you are a genius!')
                break
        else:
            print('hey bozo, I said 1~10')
    except ValueError:
        print('please enter a number')
        break

# check if number is the right guess. Otherwise


# ask again



# def system_argument(a, b):
#     try:
#         num1 = int(a)
#         num2 = int(b)    
#     except:
#         print('Please insert integer only!')
#         num1 = input('number 1: ')
#         num2 = input('number 2: ')
#         system_argument(num1, num2)

#     if num1 < num2:
#         guess_number(random.randint(num1, num2), num1, num2)
#     else:
#         guess_number(random.randint(num2, num1), num2, num1)

    



# def guess_number(number, a, b):
#     try:
#         guess = int(input(f'Guess the number between {a} - {b}: '))
#         if number == guess:
#             print(f'You guess the right answer {number}!')
#         elif guess < a or guess > b:
#             print(f'Please insert number bigger than {a} and small than {b}')
#         else:
#             guess_number(number)
#     except:
#         print('Please insert number only')
#         guess_number(number)

# system_argument(sys.argv[1], sys.argv[2])
