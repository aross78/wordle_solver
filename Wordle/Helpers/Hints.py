from dataclasses import dataclass

@dataclass
class Hints:
    green:  dict   # Dictionary of correct letter and     pos - index: char
    yellow: dict   # Dictionary of correct letter but not pos - char: list(index(es))
    gray:   set    # Set of invalid chars