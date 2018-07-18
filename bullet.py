class bullet(object):
	@staticmethod
	def getpos(x):
		return 48+x%8
	
	@staticmethod
	def updatpos(x):
		return x[0]-8

	@staticmethod
	def checkalien(tempgrid,temp):
		if tempgrid[temp[0]]=="Y" or tempgrid[temp[0]]=="y":
			return 1
		else:
			return 0

	@staticmethod
	def getbullet(move):
		if move==" ":
			draw="*"
			timedelay=0.05
		else:
			draw="|"
			timedelay=0.025

		return([draw,timedelay])


class first(bullet):
	@staticmethod
	def updscore(alientime,secbullet,tempalien,x):
		alientime[x]=-2
		if x in secbullet:
			secbullet.remove(x)
		tempalien.remove(x)
		return(alientime,secbullet,tempalien)

class second(bullet):
	@staticmethod
	def updamage(alientime,secbullet,x):
		alientime[x]=alientime[x]+5
		secbullet.append(x)
		return[alientime,secbullet]
