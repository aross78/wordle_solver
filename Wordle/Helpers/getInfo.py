from Hints import Hints

# TODO: Check details / edge cases (what if repeated greens, or green and yellow, and such)
def getInfo(hints: Hints, guess: str, answer: str):
    
    for i in range(len(guess)):
        c = guess[i]

        # Check if it was already invalid
        if c in hints.gray:
            continue
        
        # Check if it is now invalid
        if c not in answer:
            hints.gray.add(c)
            continue

        # Check if green
        if guess[i] == answer[i]: 
            hints.green.setdefault(i, c)
            
            # Remove the hint from yellow if needed
            if (c in hints.yellow) and (i in hints.yellow[c]):
                hints.yellow[c].remove(i)
            continue

        # Otherwise yellow
        hints.yellow.setdefault(c, [])
        if i not in hints.yellow[c]:
            hints.yellow[c].append(i)
    
    return hints
