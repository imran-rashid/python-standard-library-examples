import textwrap
from textwrap_example import sample_text

dedented_text = textwrap.dedent(sample_text).strip()
wrapped = textwrap.fill(dedented_text, width=50)
wrapped += '\n\nSecond paragraph after a blank line.'
final = textwrap.indent(wrapped, '> ')

print(final)

# output ->
"""
> The textwrap module can be used to format text for
> output in situations where pretty-printing is
> desired.  It offers programmatic functionality
> similar to the paragraph wrapping or filling
> features found in many text editors.

> Second paragraph after a blank line.
"""

# indent() is added prefix
string = 'Hello, World'
print(textwrap.indent(string, '😊 ')) # 😊 Hello, World