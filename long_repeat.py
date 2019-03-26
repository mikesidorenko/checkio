def long_repeat(line):
	if line == '':
		return 0
	else:
		import re
		fuck = re.compile(r'(.)\1+')
		refuck = [match.group() for match in fuck.finditer(line)]
		if refuck == []:
			return 1
		else:
			return max(len(x) for x in refuck)