import random
from brain_games.game_engine import run_game
from brain_games.const import CALC_GAME_MESSAGE, \
    RND_BETWEEN_NUM1, RND_BETWEEN_NUM2, MATH_OPERATIONS_LIST


def perform_operation_return_correct_answer():
    '''
    Function chose two random numbers and the math operations form
    the list (the range and the list of operations stored in const.py file);
    Create full_expression as a condition (first str in return tuple)
    and perform math operations with correct answer as a second str in tuple.
    '''
    num1 = random.randint(RND_BETWEEN_NUM1, RND_BETWEEN_NUM2)
    num2 = random.randint(RND_BETWEEN_NUM1, RND_BETWEEN_NUM2)
    operation = random.choice(MATH_OPERATIONS_LIST)
    full_expression = f'{num1} {operation} {num2}'
    correct_answer = str(eval(full_expression))
    # use of eval function is safe without external input
    return full_expression, correct_answer


def run_calc_game():
    run_game(perform_operation_return_correct_answer, CALC_GAME_MESSAGE)
