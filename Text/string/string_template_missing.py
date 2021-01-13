# safe_substitute() method makes it possible to avoid exceptions if not all of the values needed by the template are provided as arguments.

from string import Template

values = {
	'var': 'foo',
}

str_temp = Template('$var is here but $missing is not provided')

try:
	print(str_temp.substitute(values))
except KeyError as err:
	print('Error:', str(err))

# Instead of raising the error, safe_substitute() catches it and leaves the variable expression alone in the text.
print(str_temp.safe_substitute(values))