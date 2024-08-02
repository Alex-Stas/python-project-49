#!/usr/bin/env python3

import prompt
import random
# import brain_games.cli


def main():
    # brain_games.cli.welcome_user()
    QUANTITY_OF_ROUNDS = 3
    EVEN_GAME_MESSAGE = 'Answer "yes" if the number is even, otherwise answer "no"'
    RND_BETWEEN_NUM1, RND_BETWEEN_NUM2 = 1, 100
    user_name = welcome_user()
    for _ in range(QUANTITY_OF_ROUNDS):
        number = generate_random_number(RND_BETWEEN_NUM1, RND_BETWEEN_NUM2)
        right_answer = check_even_return_correct_answer(number)
        print(EVEN_GAME_MESSAGE)
        print(f'Question: {number}')
        user_answer = prompt.string(prompt='Your answer: ', empty=True)
        if user_answer != right_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{right_answer}'.")
            print(f"Let's try again, {user_name}!")
            return
        else:
            print('Correct!')
    print(f'Congratulations, {user_name}!')
    return

    # print(user_name)
    # print(generate_random_number(1,100))
    # print(check_even_return_correct_answer(number))


def welcome_user():
    print('Welcome to the Brain Games!')
    user_name = prompt.string(prompt='May I have your name? ', empty=False)
    print(f'Hello, {user_name}!')
    return user_name


def generate_random_number(start, end):
    random_number = random.randint(start, end)
    return random_number


def check_even_return_correct_answer(number):
    return 'yes' if number % 2 == 0 else 'no'


if __name__ == '__main__':
    main()
