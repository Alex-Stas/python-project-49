import random
from brain_games.game_engine import run_game
from brain_games.const import PRIME_GAME_MESSAGE, \
    RND_BETWEEN_NUM1, RND_BETWEEN_NUM2


def is_prime_return_correct_answer():
    number = random.randint(RND_BETWEEN_NUM1, RND_BETWEEN_NUM2)
    i = 2
    while i <= pow(number, 0.5):
        if number % i == 0:
            return number, 'no'
        i += 1
    return number, 'yes'


def run_prime_game():
    run_game(is_prime_return_correct_answer, PRIME_GAME_MESSAGE)
