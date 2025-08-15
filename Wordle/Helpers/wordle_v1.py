# Save included with pos (green), just included (yellow) and invalid (gray) 
# For every guess, update these 3.
# To make a guess,

# Strat 1 - Random:
# Get all valid letters, make all possible permutations
# Select all the ones that are words
# Submit random one

# Strat 2 - Chaos:
# Submit the one with the least 'included' letters

# Strat 3 - Hardmode:
# Get all valid letters, fix green ones, make permutations that include yellow ones
# Submit either random or one with least 'included' letters

from getPermutations import getPermutations
from getWords import getWords
from getInfo import getInfo
from Hints import Hints
import random



words = getWords()

def getGuess(hints: Hints):

    permutations = getPermutations(hints)

    # Select only valid words
    guesses = []
    for permutation in permutations:
        if permutation in words:
            guesses.append(permutation)
    
    guess_count = len(guesses)
    print(f"Valid guesses: {guess_count}")
    if guess_count <= 20:
        print(guesses, " ")
    
    # Submit random one
    guess = random.choice(guesses)

    return guess

def Game(answer=""):
    # If none given, initally pick random word as the answer
    if not answer:
        answer = random.choice(list(words))
    # print(f"Answer is: {answer}")

    green = {}   # Dictionary of items - index: char
    yellow = {}  # Dictionary of items - char: list(index(es))
    gray = set() # Set of invalid chars

    hints = Hints(green, yellow, gray)

    guesses = []
    count = 0
    while count < 10:
        # guess = input("Please write a 5 letter word: ")

        # if guess == answer:
        #     print("You've won!")
        #     break        
        
        ai_guess = getGuess(hints)
        guesses.append(ai_guess)
        print(f"AI's guess: {ai_guess}")
        if ai_guess == answer:
            print(f"AI guessed {answer}! Took {count + 1} attempts. Guesses: {guesses}", end='')
            return count + 1
        

        hints = getInfo(hints, ai_guess, answer)

        # print(f"Green hints: {hints.green}")
        # print(f"Yellow hints: {hints.yellow}")
        # print(f"Gray hints: {hints.gray}")

        count += 1
    return count + 1

# import time

# times = []
# total_attempts = []
# for i in range(10):
#     start = time.time()    
#     attempts = Game()
#     tot = time.time() - start
#     print(f". Time: {round(tot, 2)}s")
#     times.append(tot)
#     total_attempts.append(attempts)

# avg_time = sum(times) / len(times)
# avg_attempts = sum(total_attempts) / len(total_attempts)
# print(f"Average Time: {round(avg_time, 2)}s")
# print(f"Average Attempts: {round(avg_attempts, 2)}")

Game("kefir")
