def stone_wall(wall):
	wall = wall.split('\n')[1:-1] #split wall in rows, cut empties
	width = [0] * len(wall[0])    #generate list with weak points quantity
	
	for i in range(len(wall[0])): #iterate through width...
		for j in range(len(wall)):#...and depth of the wall
			if wall[j][i] == '0': #if weak block found...
				width[i] += 1     #...increase counter in corresponding index

	return width.index(max(width)) #Voila!