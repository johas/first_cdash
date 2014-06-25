import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


class animating(object):

    def __init__(self,tmj,m,x):
        fig = plt.figure() #create figure window
        ax = plt.axes(xlim=(0,1), ylim=(0,1e-5)) #x and y limits
        self.line, = ax.plot([],[], lw=1) #empty line, wide = 1
        self.x = x
        y = np.zeros(100)
        c = np.linspace(0,1e-5,100)
        self.scat = plt.scatter(x, y, c=c, s=100)

        self.tmj=tmj
        #print self.tmj[4][:]

        #self.init_line(line)

        #anim1 = animation.FuncAnimation(fig,self.animate1,
        #        init_func=self.init_line, frames=24000, interval=20,blit=True)

        anim2 = animation.FuncAnimation(fig, self.animate2, 
                frames=24000, interval = 150)

        plt.show()
        #plt.plot(x,self.tmj[0][:])
        #plt.show()
        #print x

    def init_line(self):
        self.line.set_data([],[])
        return self.line,


    def animate1(self,i) :
        self.line.set_data(self.x,self.tmj[i][:])
        return self.line,

    def animate2(self,i) :
        self.scat.set_array(self.tmj[i])

