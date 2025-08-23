import os
import time
import random
from Hints import Hints
from getGuesses import getGuesses

def getWords():
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "word_bank.txt")

    with open(file_path) as file:
        lines = file.readlines()
        words = {line.strip() for line in lines}
    return words

def getTrie(words: set):
    trie = dict()
    pointer = trie
    for word in words:
        for c in word:
            pointer.setdefault(c, {})
            pointer = pointer[c]
        pointer = trie
    return trie


alphabet = set("abcdefghijklmnopqrstuvwxyz")    

# Make all possible permutations, then select the ones that are words
def getGuessesTrie(hints, words):
    permutations = []

    # Make all possible permutations
    base = [""]*5

    # Get valid letters
    valid = alphabet.difference(hints.gray)

    # Recursively create all possible permutations
    def backtrack(i, path, trie):

        # Base case
        if i == 5:
            word = "".join(path)
            permutations.append(word)
            return

        # For each valid letter, try to make all combinations
        for c in valid:
            if c in trie: 
                # Not sure if it makes more sense to loop through letters in trie and checking if those are valid, or doing it this way
                # Might also be interesting to look into deleting the branches with invalid starts / continuations
                path[i] = c
                backtrack(i + 1, path, trie[c])
                path[i] = ""
    
    backtrack(0, base, words)

    return permutations

words = getWords()
start = time.time()   
trie = getTrie(words)
tot = time.time() - start
print(f"Time to make Trie: {round(tot, 2)}s")


for hint in [False, True]: 
    for attempt in range(10):
        times_normal = []
        times_trie = []
        
        green = {}   # Dictionary of items - index: char
        yellow = {}  # Dictionary of items - char: list(index(es))
        gray = set() # Set of invalid chars
        
        # Add one hint
        if hint:
            word = random.choice(list(words))
            for c in word: 
                if c not in gray:
                    gray.add(c)
        
        hints = Hints(green, yellow, gray)

        # Time normal function
        start = time.time()   
        guesses_1 = getGuesses(hints, words) 
        tot = time.time() - start
        times_normal.append(tot)
        # print(f"Time without Trie: {round(tot, 2)}s. Found {len(guesses_1)} guesses")

        # Time trie one
        start = time.time()   
        guesses_2 = getGuessesTrie(hints, trie) 
        tot = time.time() - start
        times_trie.append(tot)
        # print(f"Time with Trie: {round(tot, 2)}s. Found {len(guesses_2)} guesses")

    avg_time_normal = sum(times_normal) / len(times_normal)
    avg_time_trie = sum(times_trie) / len(times_trie)
    print(f"Average Time without Trie: {round(avg_time_normal, 2)}s")
    print(f"Average Time with Trie: {round(avg_time_trie, 4)}s")



                
