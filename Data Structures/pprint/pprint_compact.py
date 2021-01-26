# The compact flag tells pprint() to try to fit more data on each individual line

# when a data structure does not fit on a line, it is split up (as with the 
# second item in the data list). When multiple elements can fit on a line, as
# with the third and fourth members, they are placed that way.

from pprint import pprint
from pprint_data import data

print('Default =>')
pprint(data, compact=False)
print()

print('compact =>')
pprint(data, compact=True)