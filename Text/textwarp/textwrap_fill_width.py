# Combining Dedent and Fill

# the dedented text can be passed through fill() with a few different width values

from textwrap_example import sample_text
import textwrap

# dedent() keeps the first whitespace that's why strip() for removing space
dedented_text = textwrap.dedent(sample_text).strip()

for width in [50, 60]:
	print(f'{width} column:')
	print(textwrap.fill(dedented_text, width))

# output:
"""
50 column:
The textwrap module can be used to format text for
output in situations where pretty-printing is
desired.  It offers programmatic functionality
similar to the paragraph wrapping or filling
features found in many text editors.
60 column:
The textwrap module can be used to format text for output in
situations where pretty-printing is desired.  It offers
programmatic functionality similar to the paragraph wrapping
or filling features found in many text editors.
"""