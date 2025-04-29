import re
import pandas as pd
import matplotlib.pyplot as plt

# set plot labels
plt.title("Frequency of elements in chess moves")
plt.xlabel("Atomic number")
plt.ylabel("Frequency")

# get moves from chess file
chess = open('input/chess', 'r')
move_pattern = re.compile(r'[RNBKQ]?x?[a-h][1-8]\+?')
moves = [re.search(move_pattern, line).group() for line in chess if 'sol:' in line]
chess.close()

# get info from elements file
elements = pd.read_csv('elements.csv').set_index('Symbol')

# get elements that could show up in chess moves
element_pattern = re.compile(r'^[RNBKQ][a-hx]?$')
sneaky_elements = [ele for ele in elements.index if re.search(element_pattern, ele)]
# sort so two-letter elements are first
sneaky_elements = sorted(sneaky_elements, key=len, reverse=True)

def first_matching_term(string, terms):
    """Return the first list item appearing in the string.
    >>> first_matching_term('Ne', ['Rg', 'Ne', 'N'])
    'Ne'"""
    for term in terms:
        if term in string:
            return term
    return None

def get_atomic_number(element):
    """Return the atomic number of an element, or 0 if None."""
    try:
        return elements.loc[element, 'Atomic Number']
    except KeyError:
        return 0

# list the element if any for each move
elements_in_moves = [first_matching_term(move, sneaky_elements) for move in moves]
# and the corresponding atomic number
move_data = pd.DataFrame({'Element': elements_in_moves,
'Atomic Number': [get_atomic_number(ele) for ele in elements_in_moves]},
index=moves)

# print results
print("Total moves:", len(moves))
print("Moves ending in check:", len([move for move in moves if '+' in move]))
print("Moves containing an element:", sum([bool(ele) for ele in move_data['Element']]), "\n")
print(move_data.value_counts())

# plot results
plt.hist(move_data['Atomic Number'], bins=range(118))
plt.show()
