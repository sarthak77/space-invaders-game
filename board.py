import os

class board:
        """
         _______________
        |Y Y Y Y Y Y Y Y|
        |y Y Y Y Y   Y Y|
        |      *        |
        |  |            |
        |            *  |
        |               |
        |               |
        |      ^        |
         ---------------
         KILLS:1
         """
        score=0
        def __init__(self):
                 self.__grid=[' ']*64

        def getgrid(self):
                return self.__grid

        @staticmethod
        def printrow(r):
                print("|{} {} {} {} {} {} {} {}|".format(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7]))

        def render(self):
                os.system('clear')
                print(" _______________")
                for i in range(8):
                        board.printrow(self.__grid[i*8:i*8+8])
                print(" ---------------")
                print("KILLS:",self.score)

        def update(self,pos,character):
                self.__grid[pos]=character


