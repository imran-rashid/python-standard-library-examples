# the default width is 80 char but we can control it

from pprint import pprint
from pprint_data import data

for width in [80, 5]:
	print(f'Width {width}')
	pprint(data, width=width)
	print()