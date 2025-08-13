from itertools import permutations, product

class Solver:
    def __init__(self):
        #self.sln = [""] * 5
        self.sln = ["", "", "m", "a", ""]
        #self.yellows = {} # dict of format {index: {invalid chars}}
        self.yellows = {4: {"m, n"}}
        self.grays = set()
        self.viable_letters = set("abcdefghijklmnopqrstuvwxyz")
        self.dict = self.set_dict()

    def get_possible_guesses(self):
        possible_solutions = set()
        unknowns = self.sln.count("")
        if unknowns == 0:
            return {''.join(self.sln)}
        
        # Generate all permutations of the current solution
        self.get_permutations()

        # More code here
        return
    
    def get_permutations(self):
       # Magic
       return

    def set_dict(self, file_path="wordle_solver/curated_words.txt"):
        with open(file_path, 'r') as file:
            return { line.strip() for line in file.readlines() }

    def get_dict(self):
        return self.dict
        
# Testing
a = Solver()