# The default syntax for string.Template can be changed by adjusting the regular expression patterns it uses to find the variable names in the template body. 
# A simple way to do that is to change the delimiter and idpattern class attributes

from string import Template

class MyTemplate(Template):
	delimiter = '@'
	idpattern = '[a-z]+_[a-z]+'

template_text = """
Delimeter		: @@
Replaced		: @replace_value
Ignored			: @ignoredValue
"""

d = {
	'replace_value': '458',
	'ignoredValue': '789'
}

t = MyTemplate(template_text)
print('Modified ID pattern:')
print(t.safe_substitute(d))
# pattern %notunderscored is not replaced by anything, because it does not include an underscore character.
