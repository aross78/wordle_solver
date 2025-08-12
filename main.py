import itertools

included = "nam"
excluded = "crehu"
abc = "abcdefghijklmnopqrstuvwxyz"
for l in excluded:
    abc = abc.replace(l, "")

with open('solver\english.txt', 'r') as file:
    # Convert repo file to iterable
    lines = file.readlines()
    string_set = { line.strip() for line in lines }

    # This part's the definition of brute force :-)
    possible_solutions = set()
    for first in abc:
        for second in abc:
            possible_letters = included + first + second

            # Given a string, returns iterator of all permutations of that string ... 
            options = [ "".join(p) for p in itertools.permutations(possible_letters) ]

            # Keep permutations that are valid english words
            for o in options:
                if o in string_set:
                    possible_solutions.add(o)

    # Additional filtering
    possible_solutions -= {o for o in possible_solutions 
                 if o[4] in {'m', 'n'} or o[3] != 'a'or o[2] != 'm'}

    print(possible_solutions)