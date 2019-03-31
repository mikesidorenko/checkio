def count_consecutive_summers(num):
	result = 0
	sum = 0

	for i in range(1, num // 2 + 2):
		sum = i
		for j in range(i+1, num//2+2):
			sum += j
			if sum == num:
				result += 1
			elif sum > num:
				continue
	
	return result + 1 if num != 1 else 1