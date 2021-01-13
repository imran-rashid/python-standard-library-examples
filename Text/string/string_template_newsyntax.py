import re
from string import Template

class MyTemplate(Template):
    delimiter = '{{'
    pattern = r'''
    \{\{(?:
    (?P<escaped>\{\{)|
    (?P<named>[_a-z][_a-z0-9]*)\}\}|
    (?P<braced>[_a-z][_a-z0-9]*)\}\}|
    (?P<invalid>)
    )
    '''

template_text = '''
{{{{
{{var}}
'''

t = MyTemplate(template_text)
print('MATCHES:', t.pattern.findall(t.template))
print(t.safe_substitute(var='replacement'))