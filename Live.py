from WoG.GuessGame import play as guess_play
from WoG.MemoryGame import play as memory_play
from WoG.Utils import ERROR_MESSAGE as error_message

def welcome(name):
    return 'Hello ' + name + ' and welcome to the World of Games (WoG).\nHere you can find many cool games to play.'

def load_game():
    print("Please choose a game to play:\n1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n2. Guess Game - guess a number and see if you chose like the computer")
    while True:
        try:
            game = int(input("Please choose a game to play - 1/2"))
        except ValueError:
            continue
        if game > 2 or game < 1:
         error_message()
        if game in (1, 2):
            break
    difficulty = int(input("Please choose game difficulty from 1 to 5:"))
    if game == 1:
        memory_play(difficulty)
    if game == 2:
        guess_play(difficulty)
    return difficulty