# the function capwords() capitalizes all of the words in a string

from string import capwords

long_str = 'a quick brown fox jump over the lazy dog'
print(long_str)
print(capwords(long_str))
# this can be done also built in str method
print(long_str.title())