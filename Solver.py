from itertools import product

class Solver:
    def __init__(self):
        self.abc = set("abcdefghijklmnopqrstuvwxyz")
        self.viable_letters = [ set(self.abc) for _ in range(5) ]

        self.sln = [""] * 5
        self.yellows = {} # dict of format {letter: (invalid positions)}          
        self.grays = set()

        #self.sln = ["", "", "m", "a", ""] #for testing
        #self.yellows = {'m': {4}, 'n':{4}} #for testing
        #self.grays = set("cre") #testing
        
        self.dict = self.init_dict("solver/curated_words.txt")

    def update_viable_letters(self):
        # Handle greens
        for i in range(5):
            # If we have a letter at that pos in sln, it's the only possible letter at that index
            if self.sln[i]:
                self.viable_letters[i] = set(self.sln[i])

        # Handle yellows
        for letter, invalids in self.yellows.items():
            for i in invalids:
                self.viable_letters[i].remove(letter)
        
        # Handle grays
        for i in range(5):
            self.viable_letters[i] -= self.grays
    
        return

    def get_guesses(self):
        guesses = set()
        for p in product(*self.viable_letters):
           w = "".join(p)
           if w in self.dict:
               guesses.add(w)
        return guesses

    def init_dict(self, file_path="curated_words.txt"):
        with open(file_path, 'r') as file:
            return { line.strip() for line in file.readlines() }
        
# Testing
a = Solver()
a.update_viable_letters()
a.get_guesses()