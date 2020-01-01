from WoG.Live import load_game, welcome
from WoG.Score import add_score
name = input("Please insert your name:") #getting the player's name
print(welcome(name))
while True:
    try:
        points = int(load_game())
    except AttributeError:
        continue
    if points in (1,5):
        break
add_score(points)