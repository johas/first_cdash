from visual import * #import the visual module

rod1 = cylinder(pos=(1.,10.,0.0), axis=(0,1.0,0), radius=0.1)
rod2 = cylinder(pos=(-1.,10.,0.0), axis=(0,1.0,0), radius=0.1)
floor = box (pos=(0,0,0), length=10, height=10.0, width=10, color=color.green)
ball = sphere (pos=(0,0.1,0.1), radius=0.2, color=color.red)
#ball.velocity = vector(0,-1,0)
##ball.velocity = vector(0,0,0)
#A = 3.14*0.3**2*2
#Cd = 0.25
#dt = 0.01
#rho = 1.204
#m = 0.43
#
#while 1:
#    rate (100)
#    ball.pos = ball.pos + 0.5*ball.velocity*dt
#    if ball.y < ball.radius:
#        fd = 0.5*ball.velocity.y**2*Cd*A*rho
#        ball.velocity.y = abs(ball.velocity.y)-fd/m*dt
#    else:
#        fd = 0.5*ball.velocity.y**2*Cd*A*rho
#        if ball.velocity.y > 0.0 :
#            ball.velocity.y = ball.velocity.y - (9.8+fd/m)*dt
#        if ball.velocity.y < 0.0 :
#            ball.velocity.y = ball.velocity.y - (9.8-fd/m)*dt
