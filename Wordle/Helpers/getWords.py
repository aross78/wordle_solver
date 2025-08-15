import os

def getWords():
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "word_bank.txt")

    with open(file_path) as file:
        lines = file.readlines()
        words = {line.strip() for line in lines}
    return words