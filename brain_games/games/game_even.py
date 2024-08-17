import random
from brain_games.game_engine import run_game
from brain_games.const import EVEN_GAME_MESSAGE, \
    RND_BETWEEN_NUM1, RND_BETWEEN_NUM2


def is_even_return_correct_answer():
    number = random.randint(RND_BETWEEN_NUM1, RND_BETWEEN_NUM2)
    if number % 2 == 0:
        return number, 'yes'
    return number, 'no'


def run_even_game():
    run_game(is_even_return_correct_answer, EVEN_GAME_MESSAGE)
