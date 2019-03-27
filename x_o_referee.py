from typing import List

def checkio(gr: List[str]) -> str:   
# I renamed input list variable 'game_result' > 'gr' 
# to shorten code lines
		
	for i in range(3):
		if gr[0][i] == gr[1][i] == gr[2][i] != '.': #check if columns are equal and not '.'
			result = gr[0][i]
			break
		#check if diagonals are equal and not '.'
		elif (gr[0][0] == gr[1][1] == gr[2][2] != '.') or (gr[0][2] == gr[1][1] == gr[2][0] != '.'):
			result = gr[1][1]
			break
		#check rows
		elif gr[i] == 'XXX' or gr[i] == 'OOO':
			result = gr[i][0]
			break
		else:
			result = 'D' #if none of above matched
	
	return result