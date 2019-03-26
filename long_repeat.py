def long_repeat(line):
	import re
	a = re.split(r'(.+)', line)
	return max(len(b) for b in a)


print(long_repeat('abababaab'))