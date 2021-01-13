# Truncating Long Text

# To truncate text to create a summary or preview, use shorten(). All existing whitespace, such as tabs, newlines, and series of multiple spaces, 
# will be standardized to a single space. Then the text will be truncated to a length less than or equal to what is requested, 
# between word boundaries so that no partial words are included.

import textwrap
from textwrap_example import sample_text

dedented_text = textwrap.dedent(sample_text).strip()
original = textwrap.fill(dedented_text, width=50)
print('original text: ')
print(original, '\n')

shortend = textwrap.shorten(original, 100)
print(shortend)
# output
"""
The textwrap module can be used to format text for output in situations where pretty-printing [...]
"""

shortend_wrapped = textwrap.fill(shortend, width=50)
print(shortend_wrapped)
# output
"""
The textwrap module can be used to format text for
output in situations where pretty-printing [...]
"""
