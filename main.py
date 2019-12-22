""" Examples based on the readme.md
"""

import pandas as pd

# Example ne():
money = [0, 0, 0, 2, 3, 0, 1, 1, 3, 5, 0]
example_money = pd.DataFrame({'money': money})
print(example_money)
print('Example operator with ne:')
example_filtered = example_money.loc[example_money['money'].ne(0).idxmax():]
print(example_filtered)