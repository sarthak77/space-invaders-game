class spaceship(object):
	@staticmethod
	def control(x,move):
		if move=="d":
			return x+1
		elif move=="a":
			return x-1
