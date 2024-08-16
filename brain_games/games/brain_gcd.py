#!/usr/bin/env python3

import random
import brain_games.game_engine
from brain_games.const import QUANTITY_OF_ROUNDS, GCD_GAME_MESSAGE, \
    RND_BETWEEN_NUM1, RND_BETWEEN_NUM2


def main():
    user_name = brain_games.game_engine.welcome_user()
    print(GCD_GAME_MESSAGE)
    for _ in range(QUANTITY_OF_ROUNDS):
        num1 = generate_random_number(RND_BETWEEN_NUM1, RND_BETWEEN_NUM2)
        num2 = generate_random_number(RND_BETWEEN_NUM1, RND_BETWEEN_NUM2)
        right_answer = find_gcd_return_correct_answer(num1, num2)
        question = f'{num1} {num2}'
        result_of_round = brain_games.game_engine.\
            ask_for_answer_check_correct_react_and_return_result(
                user_name, question, right_answer)
        if not result_of_round:
            return
        else:
            continue
    print(f'Congratulations, {user_name}!')
    return


def generate_random_number(start, end):
    random_number = random.randint(start, end)
    return random_number


def find_gcd_return_correct_answer(num1, num2):
    if num2 > num1:
        num1, num2 = num2, num1
    while num1 % num2 != 0:
        num1, num2 = num2, num1 % num2
    return str(num2)


if __name__ == '__main__':
    main()
