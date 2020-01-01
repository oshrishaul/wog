import random
from WoG.Score import add_score
def generate_number(difficulty):
    return (random.randint(1,difficulty))

def get_guess_from_user(difficulty):
    guess = input('Please guess a number between 1 to ' + str(difficulty))
    return guess

def compare_results(difficulty, secret_number):
    if difficulty == secret_number:
        return True
    else:
        return False

def play(difficulty):
    difficulty = generate_number(difficulty)
    secret_number = int(get_guess_from_user(difficulty))
    compare_results(difficulty, secret_number)