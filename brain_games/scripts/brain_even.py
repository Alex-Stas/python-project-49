#!/usr/bin/env python3

import random
import brain_games.game_engine
from brain_games.const import QUANTITY_OF_ROUNDS, EVEN_GAME_MESSAGE, \
    RND_BETWEEN_NUM1, RND_BETWEEN_NUM2


def main():
    user_name = brain_games.game_engine.welcome_user()
    print(EVEN_GAME_MESSAGE)
    for _ in range(QUANTITY_OF_ROUNDS):
        number = generate_random_number(RND_BETWEEN_NUM1, RND_BETWEEN_NUM2)
        right_answer = is_even_return_correct_answer(number)
        result_of_round = brain_games.game_engine.\
            ask_for_answer_check_correct_react_and_return_result(
                user_name, number, right_answer)
        if not result_of_round:
            return
        else:
            continue
    print(f'Congratulations, {user_name}!')
    return


def generate_random_number(start, end):
    random_number = random.randint(start, end)
    return random_number


def is_even_return_correct_answer(number):
    return 'yes' if number % 2 == 0 else 'no'


if __name__ == '__main__':
    main()
