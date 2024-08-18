import random
from brain_games.game_engine import run_game
from brain_games.const import PROGRESSION_GAME_MESSAGE, \
    RND_BETWEEN_NUM1, RND_BETWEEN_NUM2, MAX_STEP_PROGRESSION, \
    MIN_STEP_PROGRESSION, MIN_SIZE_PROGRESSION, MAX_SIZE_PROGRESSION


def generate_progression_delete_random_memeber_return_correct_answer():
    '''
    Function generate random progression with the data from const.py file;
    Select the member with random index get it as correct answer
    and replace with '..';
    Convert the progression into string for correct output;
    Return tuple with modified progression and correct andwer.
    '''
    start_of_progression = random.randint(RND_BETWEEN_NUM1, RND_BETWEEN_NUM2)
    step_of_progression = random.randint(MIN_STEP_PROGRESSION,
                                         MAX_STEP_PROGRESSION)
    size_of_progression = random.randint(MIN_SIZE_PROGRESSION,
                                         MAX_SIZE_PROGRESSION)
    progression = []
    member_of_progression = start_of_progression
    for _ in range(size_of_progression):
        progression.append(str(member_of_progression))
        member_of_progression += step_of_progression

    random_member_index = random.randint(0, (len(progression) - 1))
    deleted_member = progression[random_member_index]
    progression[random_member_index] = '..'
    modified_progression = ' '.join(progression)
    # convertion to str for correct output without '' and []

    return modified_progression, deleted_member


def run_progression_game():
    run_game(generate_progression_delete_random_memeber_return_correct_answer,
             PROGRESSION_GAME_MESSAGE)
