# Here's second try for 'count_consecutive_summers' task
# 
# If we have some consecutive numbers, and their sum 
# results in given number, then 
# given_number = a * min + sum([x for x in range(a))
# 'min' is the number from which consecution begins
# 'a' is the quantity of summers
# sum([x for x in range(a)) is sum of numbers from 1 to 'a'
# 'a' must be positive integer
# This all means that for every 'given_number' there can be
# only one solution for every possible number of summers
# for example 'given_number' is 15 and we want to find 5 consecutive
# numbers which sum will result in 15. 
# sum(x for x in range(5)) = sum (1,2,3,4,5)
# 15 == 4 * min + sum(1,2,3,4,5)
# We see that only one 'min' value is possible for five summers
# So, number of possible 'min's is equal to number of possible 'a's
# min = (given_number - sum([x for x in range(a)]) / a

def count_consecutive_summers(num):
	res = 0
	for i in range(1, num // 2 + 2):       # iterate from 1 to half of num + 2
		a = (num - sum([x for x in range(i)])) / i  # described above
		if a.is_integer() and a > 0:   # check if 'a' is positive integer
			res += 1
	return res