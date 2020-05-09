import numpy as np

class Particle:
    def __init__(pos):
        self.pos = pos
        self.vec = np.zeros(3)
        self.mass = 1.0
'''
  4------5
 /      /
0------1
  6------7
 /      /
2------3
'''
    def trilinerinterpolate(grids):
       xlerp0 = np.interp( self.pos[0] ,[grids[0].pos[0],grids[1].pos[0]] , [grids[0].mass,grids[1].mass] )
       xlerp1 = np.interp( self.pos[0] ,[grids[2].pos[0],grids[3].pos[0]] , [grids[2].mass,grids[3].mass] )
       xlerp2 = np.interp( self.pos[0] ,[grids[4].pos[0],grids[6].pos[0]] , [grids[4].mass,grids[5].mass] )
       xlerp3 = np.interp( self.pos[0] ,[grids[6].pos[0],grids[7].pos[0]] , [grids[6].mass,grids[7].mass] )

       ylerp0 = np.interp( self.pos[1] ,[grids[0].pos[1],grids[2].pos[1]] , [xlerp0,xlerp1] )
       ylerp1 = np.interp( self.pos[1] ,[grids[0].pos[1],grids[2].pos[1]] , [xlerp2,xlerp3] )

       zlerp = np.interp( self.pos[2] ,[grids[0].pos[2],grids[4].pos[2]] , [ylerp0,ylerp1] )
       self.mass = zlerp

       xlerp0 = np.interp( self.pos[0] ,[grids[0].pos[0],grids[1].pos[0]] , [grids[0].vec,grids[1].vec] )
       xlerp1 = np.interp( self.pos[0] ,[grids[2].pos[0],grids[3].pos[0]] , [grids[2].vec,grids[3].vec] )
       xlerp2 = np.interp( self.pos[0] ,[grids[4].pos[0],grids[6].pos[0]] , [grids[4].vec,grids[5].vec] )
       xlerp3 = np.interp( self.pos[0] ,[grids[6].pos[0],grids[7].pos[0]] , [grids[6].vec,grids[7].vec] )

       ylerp0 = np.interp( self.pos[1] ,[grids[0].pos[1],grids[2].pos[1]] , [xlerp0,xlerp1] )
       ylerp1 = np.interp( self.pos[1] ,[grids[0].pos[1],grids[2].pos[1]] , [xlerp2,xlerp3] )

       self.vec = np.interp( self.pos[2] ,[grids[0].pos[2],grids[4].pos[2]] , [ylerp0,ylerp1] )

    def EulerIntegral(deltaTime):
        self.pos += self.vec*deltaTime