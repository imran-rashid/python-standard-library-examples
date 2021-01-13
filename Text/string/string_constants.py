# https://docs.python.org/3.9/library/string.html
# https://docs.python.org/3/library/stdtypes.html#string-methods
# https://docs.python.org/3.9/library/string.html#format-string-syntax

import string
import inspect

def is_str(value):
	return isinstance(value, str)

for name, value in inspect.getmembers(string, is_str):
	if name.startswith('_'): continue
	print(f'{name} = {value}')

def is_num(value):
	return isinstance(value, int)

for name, value in inspect.getmembers(int, is_num):
	if name.startswith('_'): continue
	print(f'{name} = {value}')