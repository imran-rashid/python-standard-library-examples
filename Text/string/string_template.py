# String templates were added as part of `PEP 292` and are intended as an alternative to the built-in interpolation syntax.

from string import Template

values = {
	'var': 'foo'
}

str_template = Template("""
Variable        : ${var}
Escape          : $$
Variable in text: ${var}iable
""")

print("Template:", str_template.substitute(values))

replace = {
	'fox': 'cow',
	'dog': 'lion'
}

temp_str = Template('A brown ${fox} jump over the lazy ${dog}')
print(temp_str.substitute(replace))

# str.format()
str_template = """
Variable        : {var}
Escape          : {{}}
Variable in text: {var}iable
"""
print('Format:', str_template.format(**values))

str_text = 'A brown {fox} jump over the lazy {dog}'
print(str_text.format(fox='cow', dog='lion'))