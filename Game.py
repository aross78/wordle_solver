from random import choice
import Solver

class Game:
    def __init__(self, sln=""):
        if sln:
            self.sln = sln
        else:
            self.sln = self.get_random_sln()
        print(f"Initiated with sln {self.sln}")

    def score_guess(self, guess):
        yellow_budget = { c : self.sln.count(c) for c in self.sln } # {letter: count}
        response = []
        
        for i in range(5):
            c = guess[i]

            if c == self.sln[i]:
                yellow_budget[c] -= 1
                response.append("g")
            elif c in self.sln:
                if not yellow_budget[c]:
                    response.append("b")
                    continue
                yellow_budget[c] -= 1
                response.append("y")
            else:
                response.append("b")

        return response

    
    def get_random_sln(self):
        with open("curated_words.txt", 'r') as file:
            return choice([line.strip() for line in file])
        
    def solve(self):
        solver = Solver(self) # this feels illegal
        # Magic
        return

# Testing 
# a = Game("ovals")
# print(a.score_guess("boots"))
