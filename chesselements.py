import re
import pandas as pd
import matplotlib.pyplot as plt
from captchasums import plot_frequency

def first_matching_term(string, terms):
    """Return the first list item appearing in the string, or None if none.
    >>> first_matching_term('Ne', ['Rg', 'Ne', 'N'])
    'Ne'"""
    for term in terms:
        if term in string:
            return term
    return None

def main():
    # get moves from chess file
    chess = open('input/chess', 'r')
    move_pattern = re.compile(r'[RNBKQ]?x?[a-h][1-8]\+?')
    moves = [re.search(move_pattern, line).group() for line in chess if 'sol:' in line]
    chess.close()

    # get info from elements file
    elements = pd.read_csv('input/elements.csv').set_index('Symbol')

    # get elements that could show up in chess moves
    element_pattern = re.compile(r'^[RNBKQ][a-hx]?$')
    sneaky_elements = [ele for ele in elements.index if re.search(element_pattern, ele)]
    # sort so two-letter elements are first
    sneaky_elements = sorted(sneaky_elements, key=len, reverse=True)

    # list the element if any for each move
    elements_in_moves = [first_matching_term(move, sneaky_elements) for move in moves]
    # and the corresponding atomic number
    atomic_numbers = [elements.loc[ele, 'Atomic Number'] if ele else 0 
    for ele in elements_in_moves]

    move_data = pd.DataFrame({'Atomic Number': atomic_numbers,
    'Element': elements_in_moves})

    # print results
    print("Total moves:", len(moves))
    print("Moves ending in check:", sum(['+' in move for move in moves]))
    print("Moves containing an element:", move_data['Element'].astype(bool).sum(), "\n")
    print(move_data.value_counts(sort=False))

    # plot results
    plot_frequency(move_data['Atomic Number'], 'Atomic number', 'Elements in chess moves')

if __name__ == '__main__':
    main()
