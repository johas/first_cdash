import sys
from ast import literal_eval
import os
path = os.path.realpath(__file__).split('main.py')[0]
#print path
sys.path.append(path+'heat_equation')
sys.path.append(path+'linear_alg')
sys.path.append(path+'visual-effects')
sys.path.append(path+'input')
import  heateq as ht
import matrix_manipulation as matm
import animatingrod as anrod
#import read_inp as rinp
import numpy as np
from matplotlib import pyplot as plt


def energy_prop(y,m,n,outfile):
    E_t = np.zeros(m)
    for i in range(0,m):
        E_t[i] = reduce(lambda x, z: x+z**2/(n+1),y[i][:])
    itemindex = np.where(E_t == max(E_t))
    #print itemindex
    if E_t[0] == E_t[itemindex]:
        print 'E_t(0) >= E_t(t)'
        outfile.write('E_t(0) >= E_t(t)\n')
    else :
        print 'E_t(0) <= E_t(t), this is wrong'
        outfile.write('E_t(0) <= E_t(t), this is wrong\n')


inpfile = open(sys.argv[1],'r')
outfile = open(sys.argv[1].split('inp')[0]+'out','w')
readfile = inpfile.readlines()
test = 'not' 

for n in filter (lambda x: 'n =' in x, readfile): n = int(n.split('=')[1])
for m in filter (lambda x: 'm =' in x, readfile): m = int(m.split('=')[1])
for scheme in filter (lambda x: 'scheme =' in x, readfile): scheme = scheme.split('=')[1]
for test in filter (lambda x: 'testcase' in x, readfile): test = 'test' 

print n
print m
print scheme


object1 = ht.heat_equation(m,n,scheme,'von neumann',outfile)
#print 'A matrix'
#print object1.A
#print 'Initial vmj'
#print object1.vmj

object2 = matm.matrix_manipulation(object1.A,object1.vmj,m, scheme)

xv = np.zeros(n)
a=np.linspace(1,n,n)
#print a
xv = map(lambda x: x/(n+1),a)
#print xv
#print len(xv)
#print len(object2.y[0][:])
yv = object2.y[0][:]
#print yv
#plt.plot(xv,yv)

print 'max temperature',object2.y.max()
outfile.write('max temperature'+' '+str(object2.y.max())+'\n')
print 'minimum temperature',object2.y.min()
outfile.write('minimum temperature'+' '+str(object2.y.min())+'\n')
print 'minimum in time 0:', min(object2.y[0]), 'and where', np.where(object2.y == min(object2.y[0]))
print ''
print 'Where value is negative', np.where(object2.y < 0)

energy_prop(object2.y,m,n,outfile)

if 'test' not in test :
    object3 = anrod.animating(object2.y,m,xv)




