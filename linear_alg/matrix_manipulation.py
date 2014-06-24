import os, sys,glob
import numpy as np
from scipy import sparse

class matrix_manipulation(object):

    def __init__(self,A,y,m):
        self.A = A
        self.y=y
        #self.solve_linear(A,y)
        self.mat_mult_time(y,m)
        

    def solve_linear(self,y):
        np.linalg.solve(self.A, y)

    def mat_mult_time(self,y,m):
        print m
        for i in range(0,m-1) :
            #print i
            j=i+1
            b= y[i][:]
            self.y[j][:] = self.A*b
            #d = self.A*b
            #if i == 0 :
                #print d
                #print 'bye'
            
            #self.y[j][:] = d

        
        


