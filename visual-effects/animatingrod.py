import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


class animating(object):

    def __init__(self,tmj,m,x):
        fig = plt.figure() #create figure window
        ax = plt.axes(xlim=(0,1), ylim=(0,1e-5)) #x and y limits
        self.line, = ax.plot([],[], lw=1) #empty line, wide = 1
        self.x = x

        self.tmj=tmj
        #print self.tmj[4][:]

        #self.init_line(line)

        anim = animation.FuncAnimation(fig,self.animate,
                init_func=self.init_line, frames=24000, interval=20,blit=True)

        plt.show()
        #plt.plot(x,self.tmj[0][:])
        #plt.show()
        #print x

    def init_line(self):
        self.line.set_data([],[])
        return self.line,


    def animate(self,i) :
        self.line.set_data(self.x,self.tmj[i][:])
        return self.line,


