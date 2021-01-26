# For very deep data structures, it may not be desirable for the output to 
# include all of the details. The data may not be formatted properly, the 
# formatted text might be too large to manage, or some of the data may be extraneous.

from pprint import pprint
from pprint_data import data

# pprint(data)
pprint(data, depth=1) # [(...), (...), (...), (...), (...)]
pprint(data, depth=2) # [(1, {...}), (2, {...}), (3, [...]), (4, [...]), (5, [...])]