# Lines prefixed with - were in the first sequence, but not the second.
# Lines prefixed with + were in the second sequence, but not the first.
# If a line has an incremental difference between versions, an extra line 
# prefixed with ? is used to highlight the change within the new version.
# If a line has not changed, it is printed with an extra blank space on the 
# left column so that it is aligned with the other output that may have differences.


import difflib
from difflib_data import *

d = difflib.Differ()
diff = d.compare(text1_lines, text2_lines)
print('\n'.join(diff))