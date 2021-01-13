# Removing Existing Indentation

from textwrap_example import sample_text
import textwrap

# it removes the common whitespace prefix from all of the lines of string
dedented_text = textwrap.dedent(sample_text)
print(dedented_text)

# output -> 
"""
The textwrap module can be used to format text for output in
situations where pretty-printing is desired.  It offers
programmatic functionality similar to the paragraph wrapping
or filling features found in many text editors.
"""

print(sample_text)

# output -> 
"""
    The textwrap module can be used to format text for output in
    situations where pretty-printing is desired.  It offers
    programmatic functionality similar to the paragraph wrapping
    or filling features found in many text editors.
"""
