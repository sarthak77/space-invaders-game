from board import *
from alien import *
from spaceship import *
from bullet import *

class engine(object):

	def __init__(self):
		self.__board=board()

	def run(self):

		#creating initial board
		for i in range(6,16,16):#initial alien at 6
			self.__board.update(i,"Y")
		self.__board.update(56+3,"^")#initial spaceship at 3


		#calculating temp variables
		tempalien=[]#stores index of aliens
		secbullet=[]#store second bullet hit aliens
		tempgrid=self.__board.getgrid()
		for i in range(16):
			if tempgrid[i]=="Y":
				tempalien.append(i)
		x=3#index of spaceship
		q=1#to exit game
		alientime=['']*16#stores time 
		for i in range(16):
			if i in tempalien:
				alientime[i]=time.time();
			if i not in tempalien:
				alientime[i]=0;

		prevtime=time.time()
		while(q):
			self.__board.render()
			move=input()
			
			
			#controling spaceship
			if move=="d" or move=="a":
				x=spaceship().control(x,move)
				for i in range(56,64,1):
					self.__board.update(i," ")
				self.__board.update(56+x%8,"^")

			
			#for exit
			elif move=="q":
				q=0


			#for firing missiles
			elif (move=="s" or move==" "):

				temp=[bullet().getpos(x)]

				while(temp[0]>=0):#loop till bullet reaches top

					#checking for aliens
					flag=0
					tempgrid=self.__board.getgrid()
					flag=bullet().checkalien(tempgrid,temp)

					self.__board.update(temp[0],bullet().getbullet(move)[0])
					self.__board.render()
	

					#first missile
					if move==" ":
						#incrementing score
						if flag==1:
							[alientime,secbullet,tempalien]=first().updscore(alientime,secbullet,tempalien,temp[0])
							self.__board.score=self.__board.score+1;
						self.__board.update(temp[0]," ")

					#second missile
					else:
						if flag==1:
							second().updamage(alientime,secbullet,temp[0])
							self.__board.update(temp[0],"y")
						else:
							self.__board.update(temp[0]," ")

					#delay for bullet
					time.sleep(bullet().getbullet(move)[1])
					self.__board.render()

					#when hits alien stop moving up
					if flag==1:
						break

					temp[0]=bullet().updatpos(temp)
		

			#add aliens after 10 seconds
			#1s for delay in other proceses
			elapsedtime=time.time()-prevtime
			if(elapsedtime>11):
				[tempalien,alientime]=alien().updal(self,tempalien,1,alientime)
				for i in range(16):
					if(i in tempalien):
						self.__board.update(i,"Y")
				prevtime=time.time()

			#remove aliens after 8 seconds
			#1s for delay in other proceses
			[tempalien,alientime,secbullet]=alien().updal(self,secbullet,0,alientime)
			for i in range(16):

				if i in tempalien:
					if i not in secbullet:
						self.__board.update(i,"Y")
					else:
						self.__board.update(i,"y")
				if i not in tempalien:
					self.__board.update(i," ")

#running program
if __name__=="__main__":
	x=engine()
	x.run()
