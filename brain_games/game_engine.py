import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    user_name = prompt.string(prompt='May I have your name? ', empty=False)
    print(f'Hello, {user_name}!')
    return user_name


def ask_for_answer_check_correct_react_and_return_result (user_name, question, correct_answer):
        print(f'Question: {question}')
        user_answer = prompt.string(prompt='Your answer: ', empty=True)
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            return False
        else:
            print('Correct!')
            return True