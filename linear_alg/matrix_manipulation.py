import os, sys,glob
import numpy as np
from scipy import sparse

class matrix_manipulation(object):

    def __init__(self,A,y,m,scheme):
        self.A = A
        self.y=y
        if 'implicit' in scheme: 
            self.solve_linear(y,m)
        if 'explicit' in scheme:
            self.mat_mult_time(y,m)


    def solve_linear(self,y,m):
        for i in range(0,m-1) :
            self.y[i+1][:] = np.linalg.solve(self.A, y[i])

    def mat_mult_time(self,y,m):
        print m
        for i in range(0,m-1) :
            #print i
            j=i+1
            b= y[i][:]
            self.y[j][:] = self.A.dot(b)
            #d = self.A*b
            #if i == 0 :
                #print d
                #print 'bye'
            
            #self.y[j][:] = d



        
        


