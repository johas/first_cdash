from visual import * #import the visual module
import numpy as np

#rod = cylinder(pos=(0,2,1), axis=(5,0,0), radius=1)
floor = box (pos=(0,0,0), length=6, height=0.5, width=4, color=color.white)
ball = sphere (pos=(0,4,0), radius=1, color=color.red)
ball.velocity = vector(0,-1,0)
#ball.velocity = vector(0,0,0)
A = 3.14*0.3**2*2
Cd = 0.25
dt = 0.01
rho = 1.204
m = 0.43
i=0

while 1:
    rate (100)
    ball.pos = ball.pos + ball.velocity*dt
   # print ball.velocity.y
    if ball.y < ball.radius : #and ball.velocity.y < 0.0 :
        i=i+1
        fd = 0.5*ball.velocity.y**2*Cd*A*rho
        Eny=0.5*m*abs(ball.velocity.y)**2*(1-np.exp(-0.2*ball.velocity.y**2))
        ball.velocity.y = np.sqrt(2.*Eny/m)
        #print ball.velocity.y,ball.y
        #ball.velocity.y = abs(ball.velocity.y)-2.45*dt#-fd/m*dt
    else:
        fd = 0.5*ball.velocity.y**2*Cd*A*rho
        if ball.velocity.y > 0.0 :
            ball.velocity.y = ball.velocity.y - (9.8+fd/m)*dt
        if ball.velocity.y < 0.0 :
            ball.velocity.y = ball.velocity.y - (9.8-fd/m)*dt
        #if i == 1 and ball.velocity.y < 0.0 :
        #    ball.belocity.y = 0.0
        #i = 0
