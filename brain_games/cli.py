# def main():
#     print('Welcome to the Brain Games!')
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    user_name = prompt.string(prompt='May I have your name? ', empty=False)
    print(f'Hello, {user_name}!')


# # if __name__ == '__main__':
#     main()
