# Recursive data structures are represented with a reference to the original 
# source of the data, given in the format <Recursion on typename with id=number>.

from pprint import pprint

local_data = [1, 2, 'a', 'b']
local_data.append(local_data)

print(local_data) # [1, 2, 'a', 'b', [...]]

print(f'Id of the local_data => {id(local_data)}')
pprint(local_data) # [1, 2, 'a', 'b', <Recursion on list with id=51605672>]