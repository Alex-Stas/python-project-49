#!/usr/bin/env python3

import random
import brain_games.game_engine
from brain_games.const import QUANTITY_OF_ROUNDS, CALC_GAME_MESSAGE, \
    RND_BETWEEN_NUM1, RND_BETWEEN_NUM2, MATH_OPERATIONS_LIST


def main():
    user_name = brain_games.game_engine.welcome_user()
    print(CALC_GAME_MESSAGE)
    for _ in range(QUANTITY_OF_ROUNDS):
        num1 = generate_random_number(RND_BETWEEN_NUM1, RND_BETWEEN_NUM2)
        num2 = generate_random_number(RND_BETWEEN_NUM1, RND_BETWEEN_NUM2)
        operation = random.choice(MATH_OPERATIONS_LIST)
        full_expression = f'{num1} {operation} {num2}'
        right_answer = perform_operation_return_correct_answer(full_expression)
        result_of_round = brain_games.game_engine.\
            ask_for_answer_check_correct_react_and_return_result(
                user_name, full_expression, right_answer)
        if not result_of_round:
            return
        else:
            continue
    print(f'Congratulations, {user_name}!')
    return


def generate_random_number(start, end):
    random_number = random.randint(start, end)
    return random_number


def perform_operation_return_correct_answer(full_expression):
    return str(eval(full_expression))


if __name__ == '__main__':
    main()
