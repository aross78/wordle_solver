import itertools

inc = "nam"
abc = "abcdefghijklmnopqrstuvwxyz"
out = "crehu"
for l in out:
    abc = abc.replace(l, "")

with open('solver\english.txt', 'r') as file:
    lines = file.readlines()
    string_set = {line.strip() for line in lines}

    options = set()
    for first in abc:
        for second in abc:
            possible = inc + first + second
            perm_iter = itertools.permutations(possible)
            base_options = ["".join(p) for p in perm_iter]


            for o in base_options:
                if o in string_set:
                    options.add(o)

    to_remove = {o for o in options 
                 if o[4] in {'m', 'n'} or o[3] != 'a'or o[2] != 'm'}

    options -= to_remove

    print(options)