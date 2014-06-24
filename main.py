import sys
import os
path = os.path.realpath(__file__)
path = path.split('main.py')[0]
print path
sys.path.append(path+'heat_equation')
sys.path.append(path+'linear_alg')
sys.path.append(path+'visual-effects')
import  heateq as ht
import matrix_manipulation as matm
import animatingrod as anrod
import numpy as np
from matplotlib import pyplot as plt


def energy_prop(y,m,n):
    E_t = np.zeros(m)
    for i in range(0,m):
        E_t[i] = reduce(lambda x, z: x+z**2/(n+1),y[i][:])
    itemindex = np.where(E_t == max(E_t))
    #print itemindex
    if E_t[0] == E_t[itemindex]:
        print 'E_t(0) >= E_t(t)'
    else :
        print 'E_t(0) <= E_t(t), this is wrong'


object1 = ht.heat_equation(24000,100,'von neumann')
#print 'A matrix'
#print object1.A
#print 'Initial vmj'
#print object1.vmj

object2 = matm.matrix_manipulation(object1.A,object1.vmj,24000)

xv = np.zeros(100)
a=np.linspace(1,100,100)
#print a
xv = map(lambda x: x/101,a)
#print xv
#print len(xv)
#print len(object2.y[0][:])
yv = object2.y[0][:]
#print yv
#plt.plot(xv,yv)


energy_prop(object2.y,24000,100)
object3 = anrod.animating(object2.y,24000,xv)




