import prompt
from brain_games.const import QUANTITY_OF_ROUNDS

def run_game(get_question_and_correct_answer, game_message):
    print('Welcome to the Brain Games!')
    user_name = prompt.string(prompt='May I have your name? ', empty=False)
    print(f'Hello, {user_name}!')
    print(game_message)
    
    for _ in range(QUANTITY_OF_ROUNDS):
        question, correct_answer = get_question_and_correct_answer()       
        print(f'Question: {question}')
        user_answer = prompt.string(prompt='Your answer: ', empty=True)
        if user_answer == correct_answer:
            print('Correct!')
        else:      
            print(f'{user_answer} is wrong answer ;(. '
            f'Correct answer was {correct_answer}.')
            print(f"Let's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')
