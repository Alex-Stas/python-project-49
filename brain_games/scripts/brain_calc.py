#!/usr/bin/env python3

import random
import brain_games.game_engine


def main():
    # brain_games.cli.welcome_user()
    QUANTITY_OF_ROUNDS = 3
    CALC_GAME_MESSAGE = 'What is the result of the expression?'
    RND_BETWEEN_NUM1, RND_BETWEEN_NUM2 = 1, 100
    user_name = brain_games.game_engine.welcome_user()
    print(CALC_GAME_MESSAGE)
    for _ in range(QUANTITY_OF_ROUNDS):
        num1 = generate_random_number(RND_BETWEEN_NUM1, RND_BETWEEN_NUM2)
        num2 = generate_random_number(RND_BETWEEN_NUM1, RND_BETWEEN_NUM2)
        operation = random.choice(['+', '-', '*'])
        full_expression = f'{num1} {operation} {num2}'
        right_answer = perform_operation_return_correct_answer(full_expression)
        result_of_round = brain_games.game_engine.ask_for_answer_check_correct_react_and_return_result(user_name, full_expression, right_answer)
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


def perform_operation_return_correct_answer(full_expression):
    return str(eval(full_expression))


if __name__ == '__main__':
    main()
