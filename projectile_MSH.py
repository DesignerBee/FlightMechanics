#Run in a Vpython IDE
#Copyrights Mayank Raj -(B17EE041),Swar Vaidya-(B17EE0XX), Harshit Sharma(B17EE033)

from visual import *
from math import *
if __name__ == '__main__':
    #Scene Essentials
    frameX = display(title='Projectile_MSH',
         x=0, y=0, width=600, height=200,
         center=(500,100,0), background=(0,0,0))
    frameX.fullscreen=True
    frameX.range=(600,600,600)

    #Info File Container-
    flight_fobj= open("flight_info.txt","w+",0)

    #creating objects
    traj_sph=sphere(pos=(0,0,0),radius=15,color=color.red,make_trail = True)
    traj_sph_drag=sphere(pos=(0,0,0),radius=15,color=color.yellow,make_trail = True)
    traj_sph_approx=sphere(pos=(0,0,0),radius=15,color=(0.498039,1,0),make_trail = True)
    t=0

    """#Test Cases- Use When Fast Debugging of the program is to be done
    theta=0.523599 #45 degrees
    g=10
    neta=0.00181
    v=150
    m=10"""


    #Data Collection- Removes quotes when dynamic data collection is required
    print("Please input the mass:")
    m=float(input())
    print("Please input the value of the radius:")
    traj_sph.radius= float(input())
    print("Angle Of projection:")
    theta=float(input())
    print("Value of g(gravitational) constant:")
    g=float(input())
    print("Value of Viscosity of the fluid:")
    neta=float(input())
    print("Initial Velocity Of launch:")
    v=float(input())
    traj_sph_drag.radius=traj_sph.radius
    traj_sph_approx.radius=traj_sph.radius

    #File Input Report-
    flight_fobj.write("Mass="+str(m)+"\n"+"Velocity="+str(v)+"\n"+"Neta="+str(neta)+"\n"+"Theta="+str(theta)+"\n"+"g="+str(g)+"\n"+"Radius(Spheres)="+str(traj_sph.radius)+"\n")

    #Constants Calculations-
    k = 6*pi*neta*traj_sph_drag.radius
    uo=k/m
    Fg=m*g
    it=0
    pos_prev=0

    #creating X-Y Axis system
    axis_box_x_n=box(pos=(500,0,0),length=10000,width=1,height=1,axis=(1,0,0))
    axis_box_y_n=box(pos=(0,500,0),length=10000,width=1,height=1,axis=(0,1,0))
                    
        
    #Computational Mechanics(Code)-(Red Ball)(No Drag)
    flight_fobj.write("Ideal Case: \n")
    vel_vector=vector(v*cos(theta),v*sin(theta))
    #print("Velocity in vectorial form")
    #print(vel_vector)

    while traj_sph.pos.y>=0:
        rate(2800)
        traj_sph.pos.x= vel_vector.x*t
        traj_sph.pos.y= vel_vector.y*t - g*t*t/2
        if(vel_vector.y-g*t<0 and vel_vector.y-g*(t-0.001)>0):
            print(traj_sph.pos)
            flight_fobj.write("Max Height Vector="+str(traj_sph.pos)+"\n")
            T_run=text(pos=traj_sph.pos, text=str(traj_sph.pos),height=10,width=10,length=10, color=color.green)
            text(pos=(1,-15,0), text=str(traj_sph.pos),height=10,width=10,length=10, color=color.green)
        t+=0.001
    print(t)
    print(traj_sph.pos.x)
    flight_fobj.write("TOF="+str(t)+"\n"+"Range="+str(traj_sph.pos.x)+"\n")
    T_run.visible=False
    del T_run

    t=0 #time reset

    #Computational Mechanics(Code)- (Yellow Ball)(Linear Drag= -kv)
    flight_fobj.write("Linear Drag Case: \n")
    while traj_sph_drag.y>=0:
        rate(3000)
        traj_sph_drag.x= (vel_vector.x*m/k)*(1-exp(-k*t/m))
        traj_sph_drag.y= (vel_vector.y*m/k)*(1-exp(-k*t/m))-(Fg/k)*(t-(m/k)*(1-exp(-k*t/m)))
        #print(traj_sph_drag.pos)
        if(pos_prev>traj_sph_drag.y and it==0):
            print(traj_sph_drag.pos)
            flight_fobj.write("Max Height Vector="+str(traj_sph_drag.pos)+"\n")
            T_run=text(pos=traj_sph_drag.pos, text=str(traj_sph_drag.pos),height=10,width=10,length=10, color=color.cyan)
            text(pos=(1,-30,0), text=str(traj_sph_drag.pos),height=10,width=10,length=10, color=color.cyan)
            it=1
        pos_prev=traj_sph_drag.y
        t+=0.001
    print(t)
    print(traj_sph_drag.pos.x)
    flight_fobj.write("TOF="+str(t)+"\n"+"Range="+str(traj_sph_drag.pos.x)+"\n")
    T_run.visible=False
    del T_run

    t=0 #reset time,iterrator and previous position
    it=0
    pos_prev=0

    #Computational Mechanics(Code)- (chartreuse Ball)(pow(pi,-u) coeff approx case)
    flight_fobj.write("Wind Case(Approx): \n")
    while traj_sph_approx.pos.y>=0:
        rate(2800)
        u=uo*(t)
        traj_sph_approx.pos.x= vel_vector.x*pow(pi,-u)*t
        traj_sph_approx.pos.y= vel_vector.y*pow(pi,-u)*t - g*pow(pi,-u)*t*t/2
        if(pos_prev>traj_sph_approx.y and it==0):
            print(traj_sph_approx.pos)
            flight_fobj.write("Max Height Vector="+str(traj_sph_approx.pos)+"\n")
            T_run=text(pos=traj_sph_approx.pos, text=str(traj_sph_approx.pos),height=10,width=10,length=10, color=color.blue)
            text(pos=(1,-45,0), text=str(traj_sph_approx.pos),height=10,width=10,length=10, color=color.blue)
            it=1
        pos_prev=traj_sph_approx.y
        t+=0.001
    print(t)
    print(traj_sph_approx.pos.x)
    flight_fobj.write("TOF="+str(t)+"\n"+"Range="+str(traj_sph_approx.pos.x)+"\n")
    T_run.visible=False
    del T_run
