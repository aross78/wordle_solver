from Game import Game
from Solver import Solver

def get_todays_word():
    from datetime import datetime as dt
    import requests

    url = f"https://www.nytimes.com/svc/wordle/v2/{dt.now().strftime("%Y-%m-%d")}.json"
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    return resp.json()['solution']
    
########################################

menu = """
        1. Play today's wordle
        2. Play a randomly-generated game 
        3. Play with unknown sln
        4. Play with a chosen word
        """

print("Welcome to Wordle Solver")
choice = int(input(menu))

if choice == 1:
    game = Game(get_todays_word())
elif choice == 2:
    game = Game()
elif choice == 3:
    game = None
else:
    s = input("Choose sln: ").lower()
    game = Game(s)

solver = Solver(game)
round = 1
while solver.is_unsolved():
    print(f"Round {round}")
    guess = input("Guess: ").lower()
    solver.submit_guess(guess)

    round += 1