""" Examples based on the readme.md
"""

import pandas as pd

# Example ne():
money = [0, 0, 1, 2, 3, 0, 1, 1, 3, 5, 0]
user = ["name_b", "name_b", "name_a", "name_b", "name_b", "name_b", "name_b", "name_c", "name_a", "name_a", "name_a"]

example = pd.DataFrame({'name':user,
                              'money': money})

print(example)
print('Example operator with ne:')
example_filtered = example.loc[example['money'].ne(0).idxmax():]
print(example_filtered)

# Example nsmallest():
example_nsmallest_first = example.nsmallest(n=5, columns=['money'], keep='first')
print('Example n-smallest with keep first')
print(example_nsmallest_first)

example_nsmallest_last = example.nsmallest(n=5, columns=['money'], keep='last')
print('Example n-smallest with keep last')
print(example_nsmallest_last)

# Example sort_values():
example_sorted = example.sort_values(by=['name', 'money'], inplace=False)
print('Example sort_values')
print(example_sorted)