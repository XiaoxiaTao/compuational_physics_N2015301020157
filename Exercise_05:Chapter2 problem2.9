from pylab import *
from math import *
g = 9.8
b2m = 1e-5
class flight_state:
    def __init__(self, _x = 0, _y = 0, _vx = 0, _vy = 0, _t = 0):
        self.x = _x
        self.y = _y
        self.vx = _vx
        self.vy = _vy
        self.t = _t

class cannon:
    def __init__(self, _fs = flight_state(0, 0, 0, 0, 0), _dt = 0.1):
        self.cannon_flight_state = []
        self.cannon_flight_state.append(_fs)
        self.dt = _dt
        print self.cannon_flight_state[-1].x, self.cannon_flight_state[-1].y, self.cannon_flight_state[-1].vx, self.cannon_flight_state[-1].vy

    def next_state(self, current_state):
        global g
        next_x = current_state.x + current_state.vx * self.dt
        next_vx = current_state.vx
        next_y = current_state.y + current_state.vy * self.dt
        next_vy = current_state.vy - g * self.dt
        return flight_state(next_x, next_y, next_vx, next_vy, current_state.t + self.dt)

    def shoot(self):
        while not(self.cannon_flight_state[-1].y < 0):#while y>0
            self.cannon_flight_state.append(self.next_state(self.cannon_flight_state[-1]))
        print self.cannon_flight_state[-1].x, self.cannon_flight_state[-1].y, self.cannon_flight_state[-1].vx, self.cannon_flight_state[-1].vy 
        r = - self.cannon_flight_state[-2].y / self.cannon_flight_state[-1].y#r=-yn/yn+1
        self.cannon_flight_state[-1].x = (self.cannon_flight_state[-2].x + r * self.cannon_flight_state[-1].x) / (r + 1)
        self.cannon_flight_state[-1].y = 0

    def show_trajectory(self):
        x = []
        y = []
        for fs in self.cannon_flight_state:
            x.append(fs.x)
            y.append(fs.y)
        plot(x,y,label='tan$v_y/v_x=$'+str(self.cannon_flight_state[1].vy/self.cannon_flight_state[1].vx))
        legend(loc='best',prop={'size':11},frameon=False)
        title('The trajectory of a cannon shell')
        xlabel('x/m')
        ylabel('y/m')
        #show()

class drag_cannon(cannon):#drag_cannon inherit cannon
    def next_state(self, current_state):
        global g, b2m#b2m is calculated from the isothermal approximation
        v = sqrt(current_state.vx * current_state.vx + current_state.vy * current_state.vy)            
        next_vx = current_state.vx - b2m * v * current_state.vx * self.dt
        next_x = current_state.x + next_vx* self.dt
        next_vy = current_state.vy - g * self.dt - b2m * v * current_state.vy * self.dt
        next_y = current_state.y + next_vy* self.dt
        return flight_state(next_x, next_y, next_vx, next_vy, current_state.t + self.dt)


class iso_drag_cannon(cannon):
    def next_state(self,current_state):
        global b2m
        b2m2=b2m*exp(-current_state.y/1e+4)
        v=sqrt(current_state.vx*current_state.vx+current_state.vy*current_state.vy)
        next_vx=current_state.vx-b2m2*v*current_state.vx*self.dt
        next_x =current_state.x+ next_vx*self.dt
        next_vy=current_state.vy-b2m2*v*current_state.vy*self.dt
        next_y=current_state.y+ next_vy*self.dt
        return flight_state(next_x,next_y,next_vx,next_vy,current_state.t+self.dt)  


class adia_drag_cannon(cannon):
    def next_state(self, current_state):
        global g,b2m
        v=sqrt(current_state.vx * current_state.vx+current_state.vy * current_state.vy)
        next_vx = current_state.vx-b2m*(1-6.5e-3*current_state.y/300)**2.5 * v * current_state.vx * self.dt
        next_x = current_state.x+ next_vx*self.dt
        next_vy = current_state.vy - g*self.dt -b2m* (1-6.5e-3*current_state.y/300)**2.5 * v * current_state.vy *self.dt
        next_y = current_state.y + next_vy* self .dt
        return flight_state(next_x, next_y, next_vx, next_vy, current_state.t +self.dt)   

        pass#pass is a null operation, just to make the program complete
a1 = adia_drag_cannon(flight_state(0,0,573.4,401.2,0),_dt=0.1)#vy/vx=tan35
a2 = adia_drag_cannon(flight_state(0,0,536.2,449.9,0),_dt=0.1)#vy/vx=tan40
a3 = adia_drag_cannon(flight_state(0,0,494.9,494.9,0),_dt=0.1)#vy/vx=tan45
a4 = adia_drag_cannon(flight_state(0,0,449.9,536.2,0),_dt=0.1)#vy/vx=tan50
a5 = cannon(flight_state(0,0,401.5,573.4,0),_dt=0.1)#vy/vx=tan55
a1.shoot()#the landing point
a2.shoot()
a3.shoot()
a4.shoot()
a5.shoot()

##b = drag_cannon(flight_state(0, 0, 700, 700, 0), _dt = 0.1)
##b.shoot()
##b.show_trajectory()
a1.show_trajectory()
a2.show_trajectory()
a3.show_trajectory()
a4.show_trajectory()
a5.show_trajectory()
show()
