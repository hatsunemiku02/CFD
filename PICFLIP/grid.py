import numpy as np

#init 4 particles for each grid
class Grid:
    def __init__(xidx,yidx,zidx,gridsize):
        self.mass = 0
        self.vec = np.zeros(3)
        self.momentum = np.zeros(3)
        self.type = 0  #water 0 , solid 1 ,air 2
        self.xidx = xidx
        self.yidx = yidx
        self.zidx = zidx
        self.centerpos = [self.xidx*gridsize,self.yidx*gridsize,self.zidx*gridsize]+[gridsize/2,gridsize/2,gridsize/2]
        self.gaussexp = 0
        self.gausserr = 1

    def GaussWeight(pos):
        offset = pos - self.centerpos
        length = np.sqrt(np.sum(offset))
        return  np.exp( np.power(length-self.gaussexp,2)/(2*np.power(self.gausserr,2)) )/(np.power(2*np.pi,0.5)*self.gausserr)

    def UpdateFromParticles(particles):
        self.mass = 0
        self.vec = np.zeros(3)
        for par in particles:
            weight = self.GaussWeight(par.pos)
            self.mass += weight*par.mass
            self.vec += weight*par.vec
            self.momentum = weight*par.mass*par.vec