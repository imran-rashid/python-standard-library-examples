# Indenting Blocks

# To control which lines receive the new prefix, pass a callable as the predicate argument to indent()

import textwrap
from textwrap_example import sample_text

def should_indent(line):
	print('Indent {!r}'.format(line))
	return len(line.strip()) % 2 == 0

dedented_text = textwrap.dedent(sample_text)
wrapped = textwrap.fill(dedented_text, width=50)
final_text = textwrap.indent(wrapped, 'EVEN -> ', predicate=should_indent)
print('\n', final_text)

# output:
"""
Indent ' The textwrap module can be used to format text\n'
Indent 'for output in situations where pretty-printing is\n'
Indent 'desired.  It offers programmatic functionality\n'
Indent 'similar to the paragraph wrapping or filling\n'
Indent 'features found in many text editors.'

 EVEN ->  The textwrap module can be used to format text
for output in situations where pretty-printing is
EVEN -> desired.  It offers programmatic functionality
EVEN -> similar to the paragraph wrapping or filling
EVEN -> features found in many text editors.
"""