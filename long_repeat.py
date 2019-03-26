def sun_angle(time):
	dpm = 180 / (12 * 60) #degrees per minute
	a = time.split(':')
	minutes = int(a[0]) * 60 + int(a[1])
	if minutes < 360 or minutes > 1080:
		return "I don't see the sun!"
	else:
		return round((minutes - 360) * dpm, 2)