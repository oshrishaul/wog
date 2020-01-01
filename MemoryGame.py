import random, time, os
from WoG.Utils import *

def generate_sequence(difficulty):
    list_a = []
    for i in range(difficulty):
        list_a.append(random.randrange(1,101))
    print(list_a)
    time.sleep(0.7)
    screen_cleaner()
    return list_a

def get_list_from_user(difficulty):
    list_b = []
    print("After seeing the numbers enter the numbers you saw, each one separated with Enter.")
    for i in range(difficulty):
        data=int(input())
        list_b.append(data)
    return list_b

def is_list_equal(list_a, list_b):
    if list_a == list_b:
        return True
    else:
        return False

def play(difficulty):
    list_a = generate_sequence(difficulty)
    list_b = get_list_from_user(difficulty)
    is_list_equal(list_a, list_b)
