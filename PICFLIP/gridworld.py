import numpy as np
import grid.grid as grid

#init 4 particles for each grid
class GridWorld:
    def __init__(gridsize,xcount,ycount,zcount):
        self.xcount = xcount
        self.ycount = ycount
        self.zcount = zcount
        self.grids = np.array((self.xcount,self.ycount,self.zcount))
        for i in range(xcount):
            for j in range(ycount):
                for k in range(zcount):
                    self.grids[i][j][k] = grid(i,j,k,gridsize)

    def InitEnviroment(solids,waters,airs):
        for solid in solids:
            self.grids[solid].type = 1
        for water in waters:
            self.grids[water].type = 0
        for air in airs:
            self.grids[air].type = 2

    def GenerateVecDivergenceMat():
        divergenceNum = np.array(((self.xcount,self.ycount,self.zcount)))
        for i in range(xcount):
            for j in range(ycount):
                for k in range(zcount):
                    


    def GenerateLaplaceOpMat():


