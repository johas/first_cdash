import os, sys,glob
import numpy as np
from scipy import sparse

class heat_equation(object):

    def __init__(self,m,n,cond):
        dx=1./(n+1)
        dt = 1./(m+1)
        self.dx2 = dx**2
        self.r=dt/self.dx2
        print self.dx2
        print dt
        print self.r
        if self.r >= 0.5 :
            print 'Stability rquirement not fullfilled'
            print 'dt/dx^2 < 0.5 not true'

        else :
            self.createMatrix(m,n)
            self.initial_conditions(cond,m,n)
        

    def createMatrix(self,m,n):
        dl = du = -self.r*np.ones(n)
        d0 = (1-2.*self.r)*np.ones(n)
        d = np.vstack((dl, d0, du))
        self.A = sparse.spdiags(d, (-1, 0, 1), n, n)


    def initial_conditions(self,cond,m,n):

        if cond == 'von neumann' :
            self.vmj = np.zeros((m,n))
            b = np.zeros(n)
            a = np.linspace(1,n,n)
            b = map(lambda x: -(x/(n+1)-1.)*x/(n+1), a)
            self.vmj[0][:] = b
            #print self.vmj[0][:]

        else :
            print 'not a valid condition'
            



