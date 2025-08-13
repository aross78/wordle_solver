from itertools import product
import Game

class Solver:
    def __init__(self, game=None):
        self.abc = set("abcdefghijklmnopqrstuvwxyz")
        self.viable_letters = [ set(self.abc) for _ in range(5) ]

        self.sln = [""] * 5
        self.yellows = {} # dict of format {letter: (invalid positions)}          
        self.blacks = set()

        self.game = game

        # For testing
        #self.sln = ["", "", "m", "a", ""]
        #self.yellows = {'m': {4}, 'n':{4}}
        #self.blacks = set("cre")
        
        self.dict = set(self.init_dict("curated_words.txt"))

    def update_viable_letters(self):
        # Handle greens
        for i in range(5):
            # If we have a letter at that pos in sln, it's the only possible letter at that index
            if self.sln[i]:
                self.viable_letters[i] = set(self.sln[i])

        # Handle yellows
        for letter, invalids in self.yellows.items():
            for i in invalids:
                self.viable_letters[i].discard(letter)
        
        # Handle grays
        for i in range(5):
            self.viable_letters[i] -= self.blacks
    
        return
    
    def order_by_freq(words):
        
        return

    def get_guesses(self):
        guesses = set()
        for p in product(*self.viable_letters):
           w = "".join(p)
           if w in self.dict:
               guesses.add(w)
        return guesses
    
    def submit_guess(self, guess):
        if self.game:
            result = self.game.score_guess(guess)
        else:
            result = input(f"Input result in format \"gybbg\" where g: green, y: yellow, b: black for guess \"{guess}\": ")

        for i in range(5):
            c = guess[i]
            score = result[i]

            if score == "g":
                self.sln[i] = c
            
            elif score == "y":
                self.yellows.setdefault(c, set())
                self.yellows[c].add(i)

            else:
                self.blacks.add(c)
        
        self.update_viable_letters()
        print(f"Blacks: {self.blacks}, yellows: {self.yellows}, greens: {self.sln}")
        print(f"By posn: { [ print(r) for r in self.viable_letters ]}")
        
        if not self.sln.count(""):
            w = "".join(self.sln)
            print(f"The solution is {w}")
        else:
            next_guesses = self.get_guesses()
            print(f"Possible next guesses in order: {next_guesses}")
        return
    
    def is_unsolved(self):
        return self.sln.count("")

    def init_dict(self, file_path="curated_sorted.txt"):
        with open(file_path, 'r') as file:
            return [ line.strip() for line in file.readlines() ]
        
# Testing
# a = Solver()
# a.update_viable_letters()
# a.get_guesses()