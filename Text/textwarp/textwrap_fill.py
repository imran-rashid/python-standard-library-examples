# Filling Paragraphs

from textwrap_example import sample_text
import textwrap

# The fill() function takes text as input and produces formatted text as output.
print(textwrap.fill(sample_text, width=50))

# output :=
"""
     The textwrap module can be used to format
text for output in     situations where pretty-
printing is desired.  It offers     programmatic
functionality similar to the paragraph wrapping
or filling features found in many text editors.
"""
