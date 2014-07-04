import os, sys,glob
import numpy as np
from scipy import sparse

class heat_equation(object):

    def __init__(self,m,n,scheme,cond,outfile):
        dx=1./(n+1)
        dt = 1./(m+1)
        self.dx2 = dx**2
        self.r=dt/self.dx2
        print self.dx2
        print dt
        print self.r

        if 'explicit' in scheme:
            outfile.write('explicit\n')
            if self.r >= 0.5 :
                print 'Stability rquirement not fullfilled'
                outfile.write('Stability rquirement not fullfilled\n')
                outfile.write('dt/dx^2 < 0.5 not true\n')
                outfile.write('Program exits\n')
                print 'dt/dx^2 < 0.5 not true'
                print 'Program exits'
                sys.exit()

            else :
                self.initial_conditions(cond,m,n)
                self.create_expli_Matrix(m,n)
        if 'implicit' in scheme: 
            outfile.write('implicit\n')
            self.initial_conditions(cond,m,n)
            self.create_impli_Matrix(m,n)

        if 'implicit' not in scheme and 'explicit' not in scheme:
            print 'Not a recognized scheme'
            print 'scheme either implicit or explicit'
            print 'Program exits'
            sys.exit()


    def create_expli_Matrix(self,m,n):
        dl =  self.r*np.ones(n-1)
        d0 = (1-2.*self.r)*np.ones(n)
        self.A = np.diag(dl,-1) + np.diag(d0,0) + np.diag(dl,1)
        #self.A = self.tridiag(dl,d0,dl)
        #d = np.vstack((dl, d0, du))
        #self.A = sparse.spdiags(d, (-1, 0, 1), n, n)
        #print self.A

    def create_impli_Matrix(self,m,n):
        dl =  -self.r*np.ones(n-1)
        d0 = 2.*self.r*np.ones(n)
        #d = np.vstack((dl, d0, du))
        self.A = np.diag(dl,-1) + np.diag(d0,0) + np.diag(dl,1)
        self.A = np.identity(n)+self.A

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
            



