import time
import random


class alien(object):
        @staticmethod
        def updal(self,grid,flag,alientime):
                if flag==1:
                        while(1):
                                i=random.randint(0,15)
                                if(i not in grid):
                                        grid.append(i)
                                        alientime[i]=time.time()
                                        break
                        return ([grid,alientime])

                if flag==0:
                        destroy=time.time()
                        a=[]
                        for i in range(16):
                                if(destroy-alientime[i]<9 and alientime[i]>-1):
                                        a.append(i)
                                else:
                                        if i in grid:
                                                grid.remove(i)
                                        alientime[i]=-2
                        return ([a,alientime,grid])


