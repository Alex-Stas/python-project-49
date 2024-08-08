#!/usr/bin/env python3

import random
import brain_games.game_engine


def main():
    # brain_games.cli.welcome_user()
    QUANTITY_OF_ROUNDS = 3
    PRIME_GAME_MESSAGE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    RND_BETWEEN_NUM1, RND_BETWEEN_NUM2 = 1, 100
    user_name = brain_games.game_engine.welcome_user()
    print(PRIME_GAME_MESSAGE)
    for _ in range(QUANTITY_OF_ROUNDS):
        number = generate_random_number(RND_BETWEEN_NUM1, RND_BETWEEN_NUM2)
        right_answer = is_prime_return_correct_answer(number)
        result_of_round = brain_games.game_engine.ask_for_answer_check_correct_react_and_return_result(user_name, number, right_answer)
        if not result_of_round:
            return
        else:
            continue
    print(f'Congratulations, {user_name}!')
    return
    
        
    


# def welcome_user():
#     print('Welcome to the Brain Games!')
#     user_name = prompt.string(prompt='May I have your name? ', empty=False)
#     print(f'Hello, {user_name}!')
#     return user_name


def generate_random_number(start, end):
    random_number = random.randint(start, end)
    return random_number


def is_prime_return_correct_answer(number):
    i = 2 
    while i <= pow(number, 0.5):
        if number % i == 0 : return 'no'
        i += 1 
    return 'yes'


if __name__ == '__main__':
    main()
