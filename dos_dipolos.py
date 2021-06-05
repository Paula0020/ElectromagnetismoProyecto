import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

po = 6.7e-7
e_0 = 8.85e-12
a = 5
# Grid of x, y points on a Cartesian grid
nx, ny = 64, 64
XMAX, YMAX = 40, 40
x = np.linspace(-XMAX, XMAX, nx)
y = np.linspace(-YMAX, YMAX, ny)
X, Y = np.meshgrid(x, y)
r, phi = np.hypot(X, Y), np.arctan2(Y, X)
theta = [np.linspace(0,np.pi,nx) for x in range(0, nx)]
multi = po/(4*np.pi*e_0*r**3)
# Vectores unitarios
ru = np.array([np.sin(theta)*np.cos(phi),np.sin(theta)*np.sin(phi),np.cos(theta)])
thetau = np.array([np.cos(theta)*np.cos(phi),np.cos(theta)*np.sin(phi),-np.sin(theta)])
norm = np.cos(theta)/np.cos(theta)
phiu = np.array([-np.sin(phi)*norm,np.cos(phi)*norm,np.cos(theta)*0])
# Cartesian axis system with origin at the dipole (m)
Theta = np.linspace(0,np.pi,100)
#r = np.linspace(0.1,2*np.pi,200)
def potencial(n):
    a1 = a
    a2 = -a1
    V1 = np.abs(po/(4*np.pi*e_0)*r*np.cos(theta)/(r**2-a1*r*np.sin(theta)*np.sin(phi)+a1**2/4)**(3/2))
    V2 = np.abs(po/(4*np.pi*e_0)*r*np.cos(theta)/(r**2-a2*r*np.sin(theta)*np.sin(phi)+a2**2/4)**(3/2))
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # Draw contours at values of Phi given by levels
    levels = np.array([10**pw for pw in np.linspace(0,5,20)])
    levels = sorted(list(-levels) + list(levels))
    # Monochrome plot of potential
    ax.contour(x, y, V1+V2,levels=levels, colors='k', linewidths=2)
    ax.set_title(r"Potencial--dipolos$^2$", fontsize=20)
    plt.show()
#potencial(0)
def CampoE(eje1,eje2):
    nombres = ["$x$","$y$","$z$"]
    rep1 = 4*r**2-4*a*r*np.sin(theta)*np.sin(phi)+a**2
    Br1 = -po*np.cos(theta)*(2*a*r*np.sin(theta)*np.sin(phi)-8*r**2+a**2)/(2*np.pi*e_0*(rep1)**(5/2))*ru
    Btheta1 = -po/(2*np.pi*e_0)*((6*r*a*np.sin(phi)*np.cos(theta)**2-np.sin(theta)*(rep1))/(rep1)**(5/2))*thetau
    Bphi1 = (1/np.tan(theta))*po/(12*np.pi*e_0)*((r*a*np.sin(phi)*np.sin(theta)/rep1**(5/2)))*phiu
    #
    rep2 = np.abs(4*r**+4*a*r*np.sin(theta)*np.sin(phi)+a**2)
    Br2 = po*np.cos(theta)*(2*a*r*np.sin(theta)*np.sin(phi)+8*r**2-a**2)/(2*np.pi*e_0*(rep2)**(5/2))*ru
    Btheta2 = po/(2*np.pi*e_0)*((6*r*a*np.sin(phi)*np.cos(theta)**2+np.sin(theta)*(rep2))/(rep2)**(5/2))*thetau
    Bphi2 = (1/np.tan(theta))*po/(12*np.pi*e_0)*((r*a*np.sin(phi)*np.sin(theta)/rep2**(5/2)))*phiu
    fig, ax = plt.subplots()
    Hax = Br1[eje1]+Btheta1[eje1]+Bphi1[eje1]+Br2[eje1]+Btheta2[eje1]+Bphi2[eje1]
    Bax = Br1[eje2]+Btheta1[eje2]+Bphi1[eje2]+Br2[eje2]+Btheta2[eje2]+Bphi2[eje2]
    # Plot the streamlines with an appropriate colormap and arrow style
    color = 3* np.log2(np.hypot(Br1[2], Btheta1[1]))
    ax.streamplot(x, y, Hax, Bax, color=color, linewidth=1, cmap=plt.cm.inferno,density=2, arrowstyle='->', arrowsize=1.5)
    # Add a filled circle for the Earth; make sure it's on top of the streamlines.
    # ax.add_patch(Circle((0,0), RE, color='b', zorder=100))
    ax.set_xlabel(nombres[eje1])
    ax.set_ylabel(nombres[eje2])
    ax.set_xlim(-XMAX, XMAX)
    ax.set_ylim(-YMAX, YMAX)
    ax.set_title ("Campo eléctrico dipolo")
    plt.show()
CampoE(1,2)