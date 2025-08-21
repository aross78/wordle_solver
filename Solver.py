from itertools import product
import Game

ABC = "abcdefghijklmnopqrstuvwxyz"

class Solver:
    def __init__(self, game:Game=None):
        self.dict = self.init_dict()
        self.viable_letters = [ set(ABC) for _ in range(5) ]
        self.sln = [""] * 5
        self.yellows = {} # dict of format {letter: (invalid positions)}, can maybe be improved to encode multiples         
        self.blacks = set() # this prob needs to be changed to a structure that can encode guessing multiples
        self.game = game

    def is_unsolved(self):
        """
        Checks if any unknown letters remain in sln
        """
        return self.sln.count("")

    def get_guesses(self):
        """
        Based on remaining viable letters, 
        Returns list of format [(guess, frequency)] sorted by freq defined in self.dict
        """
        guesses = set()
        for p in product(*self.viable_letters):
           w = "".join(p)
           if w in self.dict.keys():
                # Lazily checks that all yellows (and greens, implicitly) are in the word and blacks NOT in the word
                # Have not thought through edge cases nor considered more efficient approaches
                # The blacks check should be able to be done implicitly too I think
                if set(self.yellows.keys()).issubset(set(w)):
                    guesses.add(w)

        guesses = { w : self.dict[w] for w in guesses }
        return sorted(guesses.items(), key=lambda item: item[1])

    
    def suggest_guess(self, guesses:list):
        """
        Suggests a guess by the following algorithm:
        1. Of viable guesses, look at the 20 or 25% "most common" words
        2. Determine which letters appear the most in those words
        3. Return guesses, if any, that include the five most common letters
        ...In attempt to eliminate as many remaining guesses as possible
        """
        common_letters = { l : 0 for l in ABC}
        top = 20 if len(guesses) >= 20 else int(len(guesses) * .25)
        for w in guesses[:top]:
            for l in w:
                common_letters[l] += w.count(l)

        common_letters = sorted(common_letters.items(), key=lambda item: item[1], reverse=True)
        most_common_letters = set([ i[0] for i in common_letters[:5] ])
        words_w_all_5_letters = [ w for w in guesses if set(w) == most_common_letters ]
        print(f"Suggested guesses: {words_w_all_5_letters}")

        return words_w_all_5_letters
    
    def submit_guess(self, guess):
        """
        Interfaces with Game to submit a guess
        And then update Solver's internal viable_letters model
        """
        if self.game:
            result = self.game.score_guess(guess)
        else:
            result = input(f"Input result in format \"gybbg\" where g: green, y: yellow, b: black for guess \"{guess}\": ")
            while len(result) != 5:
                result = input(f"Input 5-char result in format \"gybbg\" where g: green, y: yellow, b: black for guess \"{guess}\": ")

        # Update "greens", yellows, and blacks tracking according to response
        # Does not currently handle 2 yellows of the same letter rigorously
        # nor one green, one black of same letter in same guess
        # Or a lot of other edge cases...
        for i in range(5):
            c = guess[i]
            score = result[i]

            if score == "g":
                self.sln[i] = c
                self.viable_letters[i] = set(self.sln[i])
            
            elif score == "y":
                self.yellows.setdefault(c, set())
                self.yellows[c].add(i)
                self.viable_letters[i].discard(c)

            else:
                # I did this part v lazily
                # DO NOT TRUST AGAINST EDGE CASES
                appears_elsewhere = False
                if c in self.yellows.keys():
                    appears_elsewhere = True
                    self.yellows[c].add(i)
                    for pos in self.yellows[c]:
                        self.viable_letters[pos].discard(c)
                    
                if c in self.sln:
                    appears_elsewhere = True
                    for pos in range(5):
                        if self.sln[pos] != c:
                            self.viable_letters[pos].discard(c)
                
                if guess[i:].count(c) > 1:
                    appears_elsewhere = True
                    self.viable_letters[i].discard(c)
                    
                if not appears_elsewhere:
                    self.blacks.add(c)
                    for pos in self.viable_letters:
                        pos.discard(c)
        
        # For testing but also kinda useful for visualizing results from CLI
        print(f"Blacks: {self.blacks}, yellows: {self.yellows}, greens: {self.sln}")
        _ = [ print(r) for r in self.viable_letters ]
        
        if not self.is_unsolved():
            print(f"The solution is {"".join(self.sln).upper()}")
        else:
            guesses = [w[0] for w in self.get_guesses()]
            print(f"Possible next guesses in order: {guesses}")
            self.suggest_guess(guesses)
        return
    
    
    def init_dict(self, file_path="curated_sorted.txt"):
        """
        Given a file path for words sorted by descending commonness, 
        Populate dict of format {word: frequency_rank}
        """
        with open(file_path, 'r') as file:
            return { line[1].strip() : line[0] for line in enumerate(file) }