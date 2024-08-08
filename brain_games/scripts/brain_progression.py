#!/usr/bin/env python3

import random
import brain_games.game_engine


def main():
    # brain_games.cli.welcome_user()
    QUANTITY_OF_ROUNDS = 3
    PROGRESSION_GAME_MESSAGE = 'What number is missing in the progression?'
    RND_BETWEEN_NUM1, RND_BETWEEN_NUM2 = 1, 100
    RND_MAX_STEP_PROGRESSION = 10
    RND_MIN_SIZE_PROGRESSION, RND_MAX_SIZE_PROGRESSION = 5 , 10
    user_name = brain_games.game_engine.welcome_user()
    print(PROGRESSION_GAME_MESSAGE)
    for _ in range(QUANTITY_OF_ROUNDS):
        start_of_progression = generate_random_number(RND_BETWEEN_NUM1, RND_BETWEEN_NUM2)
        step_of_progression = generate_random_number(RND_BETWEEN_NUM1, RND_MAX_STEP_PROGRESSION)
        size_of_progression = generate_random_number(RND_MIN_SIZE_PROGRESSION, RND_MAX_SIZE_PROGRESSION)
        progression = generate_progression(start_of_progression, step_of_progression, size_of_progression)
        question, right_answer = delete_random_memeber_return_modified_progression_correct_answer(progression)
        result_of_round = brain_games.game_engine.ask_for_answer_check_correct_react_and_return_result(user_name, question, right_answer)
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


def generate_progression(start_of_progression, step_of_progression, size_of_progression):
    progression = []
    member_of_progression = start_of_progression
    for _ in range(size_of_progression):
        progression.append(str(member_of_progression))
        member_of_progression += step_of_progression
    return progression

def delete_random_memeber_return_modified_progression_correct_answer(progression):
    random_member_index = generate_random_number(0, (len(progression) - 1))
    deleted_member = progression[random_member_index]
    progression[random_member_index] = '..'
    modified_progression = ' '.join(progression) # вывод, как в задании без '' и []
    return modified_progression, deleted_member

    

def find_gcd_return_correct_answer(num1, num2):
    if num2 > num1: num1 , num2 = num2, num1 
    while num1 % num2 != 0:
        num1, num2 = num2, num1 % num2
    return str(num2)


if __name__ == '__main__':
    main()
