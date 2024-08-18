import prompt
from brain_games.const import QUANTITY_OF_ROUNDS


def run_game(get_question_and_correct_answer, game_message):
    """
    Main parts that runs the selected game.

    Initial data:
        get_question_and_answer (function): function from selected game
        that perform operations with random initial data and returns
        a tuple with condition(question) and correct answer
        (type depends on tecnical specification for output);
        game message(str): instruction for the selected game for the user:

    Workflow:
        Greetings of user (prompts for user name first);
        Game meaasge (instruction how to play the selected game)Ж
        Then several times (according to the number of rounds) runs
        get_question_and_answer (function) and compare user answer and
        correct answer;
        Depending on the result of comparison return the certain reaction
        and stops or continue the game;
        If all rounds are passed correctly greets the user and stops.
    """
    print('Welcome to the Brain Games!')
    user_name = prompt.string(prompt='May I have your name? ', empty=False)
    print(f'Hello, {user_name}!')
    print(game_message)

    for _ in range(QUANTITY_OF_ROUNDS):
        question, correct_answer = get_question_and_correct_answer()
        print(f'Question: {question}')
        user_answer = prompt.string(prompt='Your answer: ', empty=True)
        if user_answer != correct_answer:
            print(f'{user_answer} is wrong answer ;(. '
                  f'Correct answer was {correct_answer}.')
            print(f"Let's try again, {user_name}!")
            return
        print('Correct!')
    print(f'Congratulations, {user_name}!')
