# if you delete all the comments, the code will look pretty short
# i learned this linear graphs shit more than 20 fuckin' years
# ago, so it took дохуя (much) time for me to solve this :)

def wild_dogs(dogs):
	distance = [] # list to store results
	i = 0         # counter
	
	# if we kill two dogs with one shot, the shooting line 
	# must be a function of type y=ax+b (linear function graph)
	# that's why we create a dict f{}, where we will store
	# strings 'a:b' as keys
	f = {}
	
	# here we loop through all dogs pairs
	while i <= len(dogs) - 2:           # first dog in pair
		x1, y1 = dogs[i][0], dogs[i][1] # coords of first dog in pair
		for dog in dogs[i+1:]:          # second dog in pair
			x2, y2 = dog[0], dog[1]     # coords of second dog in pair
			
			# here we find func (y=ax+b) modifiers 'a' and 'b'
			# and if x1=x2 (vertical graph) we set 'a' as zero
			# for not to catch a ZeroDivisionError later
			a = (y1 - y2) / (x1 - x2) if x1 - x2 !=0 else 0
			b = y1 - a * x1
			
			# create a string "a:b" to store it as a key in dict
			k = str(a) + ':' + str(b) 
			
			# store 'a:b' as key and set value = number of pairs
			# if later another dog apperar on the same line
			# the counter increments by 1
			if k not in f.keys():
				f[k] = 1
			else:
				f[k] += 1
		i += 1

	kills = [f[j] for j in f.keys()] # list of all values
	multikill = max(kills)   # the biggest value = most dogs on line
	# there can be more than one such line, remember that
	# i.e. there are 2 lines containing three dogs each

	# so we have keys 'a:b' and each of them correspond to
	# a & b of linear graph 'y=ax+b' and their values
	# contain number of points (dogs) standing on that graph
	
	for key in f.keys(): # loop through graphs
		if f[key] == multikill: 
			
			# if line contains 'multikill' quantity of dogs
			# we build graph that is perpendicular to given line
			# such graph is (y=a1*x+b1), but we need it to include
			# the zero-zero point (0:0), so we exclude b1 from it
			# then we find these graphs intersection point which 
			# satisfies both graphs (y=ax+b) and y=(a1*x)
			a1, b1 = float(key.split(':')[0]), float(key.split(':')[1])
			
			# x0 & y0 - coords of intersection point
			x0 = -b1 / (a1 + 1 / a1)
			y0 = a1 * x0 + b1
			
			# 'distance' list will contain all distances from
			# zero point to graphs with most dogs
			# distance is hypothenuse of triangle where legs
			# are x0 and y0 values
			distance.append((x0 ** 2 + y0 ** 2) ** 0.5)
	
	return round(min(distance), 2) # return shortest distance