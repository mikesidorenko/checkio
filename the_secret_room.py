def secret_room(number):
	def convert(x):
		c = x % 10 if x % 10 != 0 else 0
		b = int(((x % 100) - c) / 10)
		a = x // 100
		strdigits = ['','one','two','three','four','five','six','seven','eight','nine',
			 'ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen',
			 'seventeen','eighteen','nineteen','twenty','thirty','forty','fifty',
			 'sixty','seventy','eighty','ninety']
		
		if x == 1000:
			door = 'one thousand'
		elif 0 <= x <= 19:
			door = strdigits[x]
		elif 19 < x < 100:
			door = strdigits[b+18] + ' ' + strdigits[c]
		else:
			door = strdigits[a] + ' hundred' + ' ' + convert(x % 100) # recursion
		return door

	doors = [convert(door) for door in range(1, number+1)]
	
	return sorted(doors).index(convert(number)) + 1