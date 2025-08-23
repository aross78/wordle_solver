from Hints import Hints

alphabet = set("abcdefghijklmnopqrstuvwxyz")    

# Make all possible permutations, then select the ones that are words
def getGuesses(hints, words):
    permutations = []

    # Make all possible permutations
    base = [""]*5

    # Get valid letters
    valid = alphabet.difference(hints.gray)

    # Recursively create all possible permutations
    def backtrack(i, path):

        # Base case
        if i == 5:
            word = "".join(path)
            if word in words: 
                permutations.append(word)
            return

        # For each valid letter, try to make all combinations
        for c in valid:

            path[i] = c
            backtrack(i + 1, path)
            path[i] = ""
    
    backtrack(0, base)

    return permutations