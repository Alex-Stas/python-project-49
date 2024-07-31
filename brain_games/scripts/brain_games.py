#!/usr/bin/env python3
# from brain_games.cli import welcome_user
import brain_games.cli


def main():
    # print('Welcome to the Brain Games!')
    # welcome_user()
    brain_games.cli.welcome_user()


def greet(who):
    print(f'Hello, {who}!')


if __name__ == '__main__':
    main()
