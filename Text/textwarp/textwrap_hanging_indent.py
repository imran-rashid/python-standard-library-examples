# Hanging Indents

# the indent of the first line can be controlled independently of subsequent lines.

import textwrap
from textwrap_example import sample_text

dedented_text = textwrap.dedent(sample_text).strip()
wrapped = textwrap.fill(dedented_text, initial_indent='_',
                    subsequent_indent=' ' * 4, width=50)

print(wrapped)

# output 
"""
_The textwrap module can be used to format text
    for output in situations where pretty-printing
    is desired.  It offers programmatic
    functionality similar to the paragraph
    wrapping or filling features found in many
    text editors.
"""