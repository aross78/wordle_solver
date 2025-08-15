from Hints import Hints

alphabet = set("abcdefghijklmnopqrstuvwxyz")    

# Make all possible permutations 
def getPermutations(hints: Hints):
    permutations = []

    # Make all possible permutations
    base = [""]*5
    
    # Set green guesses
    for i, char in hints.green.items():
        base[i] = char
    
    # Get valid letters
    valid = alphabet.difference(hints.gray)

    # Recursively create all possible permutations from given details
    def backtrack(i, path):
        # Skip fixed letters
        while i < 5 and path[i] != "":
            i += 1

        # Base case
        if i == 5:
            permutations.append("".join(path))
            return

        # For each valid letter, try to make all combinations
        for c in valid:
            # Skip if know that yellow cannot be on that place
            if (c in hints.yellow) and (i in hints.yellow[c]):
                continue

            path[i] = c
            backtrack(i + 1, path)
            path[i] = ""
    
    backtrack(0, base)
    
    return permutations