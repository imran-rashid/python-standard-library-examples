#  A unified diff includes only the modified lines and a bit of context

import difflib
from difflib_data import *

diff = difflib.unified_diff(
	text1_lines,
	text2_lines,
	lineterm=''
)

# The lineterm argument is used to tell unified_diff() to skip appending 
# newlines to the control lines that it returns because the input lines do not include them.
print('\n'.join(diff))