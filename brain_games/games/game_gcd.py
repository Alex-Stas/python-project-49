import random
from brain_games.game_engine import run_game
from brain_games.const import GCD_GAME_MESSAGE, \
    RND_BETWEEN_NUM1, RND_BETWEEN_NUM2


def find_gcd_return_correct_answer():
    '''
    Function chose two random numbers
    (the range stored in const.py file);
    Create string with these numbers as a condition
    (first str in return tuple);
    Find the GCD with correct answer as a second str in tuple.
    '''
    num1 = random.randint(RND_BETWEEN_NUM1, RND_BETWEEN_NUM2)
    num2 = random.randint(RND_BETWEEN_NUM1, RND_BETWEEN_NUM2)
    question = f'{num1} {num2}'
    if num2 > num1:
        num1, num2 = num2, num1
    while num1 % num2 != 0:
        num1, num2 = num2, num1 % num2
    return question, str(num2)


def run_gcd_game():
    run_game(find_gcd_return_correct_answer, GCD_GAME_MESSAGE)
