def navigation(seaside):
	
	path = 0          # int variable for path lenght
	coords = {}       # empty dictionary for coordinates

	for i in 'YMCS':				# log coordinates to dictionary
		for row in seaside:         # where keys = 'Y', 'M', 'C' and 'S'
			for col in row:         # and values = coordinates 'x:y'
				if col == i:
					coords[i] = str(seaside.index(row)) + ':' + str(row.index(i))

	for target in 'MCS': # abstract rect with 'Y' and target in opposite corners
		a = abs(int(coords['Y'][0]) - int(coords[target][0])) + 1 # side a
		b = abs(int(coords['Y'][2]) - int(coords[target][2])) + 1 # side b
		way = 0   # variable to store distance between 'Y' and target
		
		while a > 1 and b > 1:   # every step crops abstract rectangle's 
			a -= 1               # sides by one row and column and 
			b -= 1               # increases the way by 1 (diagonal steps)
			way +=1              # loop stops when no digonal steps left
		
		way += abs(a - b) # add what's left vertically or horizontally
		path += way # finally sum of all three path lenghts

	return path # Hooray! We found them all!