import os, time
def screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')

def ERROR_MESSAGE():
    print("Something went wrong..")

SCORES_FILE_NAME = "C:/Users/oshris/PycharmProjects/general_env/WoG/scores.txt"