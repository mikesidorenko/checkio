import string
coltrans = str.maketrans('abcdefgh', '12345678')   #used to translate column literals to numbers
backtrans = str.maketrans('12345678', 'abcdefgh')  #used to translate back to literals

def safe_pawns(pawns):
	
	def is_safe(pawn: str): #built-in func that checks if given pawn	 is safe
		
		column, defrow = pawn[0], int(pawn[1]) - 1 #column literal and back row (defending  row) number
		
		#column number in order: a=1, b=2, ..., h=8
		col_num = int(column.translate(coltrans))
		
		# check if back-left or back-right square has a defender pawn
		if defrow == 0 or (str(col_num - 1).translate(backtrans) + str(defrow) not in pawns) and (str(col_num + 1).translate(backtrans) + str(defrow) not in pawns):
			return 0 #given pawn is unsafe
		else:
			return 1 #this means the given pawn is safe
	
	return sum(is_safe(pawn) for pawn in pawns)