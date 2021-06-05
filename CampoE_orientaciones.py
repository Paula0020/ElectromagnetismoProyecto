import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

po = 6.7e-7
e_0 = 8.85e-12
alfaangle = 30
alfa = alfaangle*np.pi/180
# Grid of x, y points on a Cartesian grid
nx, ny = 64, 64
XMAX, YMAX = 40, 40
x = np.linspace(-XMAX, XMAX, nx)
y = np.linspace(-YMAX, YMAX, ny)
X, Y = np.meshgrid(x, y)
r, phi= np.hypot(X, Y), np.arctan2(Y, X)
theta = [np.linspace(0,np.pi,nx) for x in range(0, nx)]
nombres = ["$x$","$y$","$z$"]
multi = po/(4*np.pi*e_0*r**3)
# Vectores unitarios
ru = np.array([np.sin(theta)*np.cos(phi),np.sin(theta)*np.sin(phi),np.cos(theta)])
thetau = np.array([np.cos(theta)*np.cos(phi),np.cos(theta)*np.sin(phi),-np.sin(theta)])
norm = np.cos(theta)/np.cos(theta)
phiu = np.array([-np.sin(phi)*norm,np.cos(phi)*norm,np.cos(theta)*0])
###
def campoEZ(eje1,eje2):
    Br = multi*2*np.cos(theta)*ru
    Btheta = multi*np.sin(theta)*thetau
    fig, ax = plt.subplots()
    Hax = Br[eje1]+Btheta[eje1]
    Bax = Br[eje2]+Btheta[eje2]
    # Plot the streamlines with an appropriate colormap and arrow style
    color = 2 * np.log(np.hypot(Br[2], Btheta[2]))
    ax.streamplot(x, y, Hax, Bax, color=color, linewidth=1, cmap=plt.cm.inferno,density=2, arrowstyle='->', arrowsize=1.5)
    # Add a filled circle for the Earth; make sure it's on top of the streamlines.
    # ax.add_patch(Circle((0,0), RE, color='b', zorder=100))
    ax.set_title ("Campo eléctrico-- z")
    ax.set_xlabel(nombres[eje1])
    ax.set_ylabel(nombres[eje2])
    ax.set_xlim(-XMAX, XMAX)
    ax.set_ylim(-YMAX, YMAX)
    plt.show()
campoEZ(1,2)
def campoEY(eje1,eje2):
    Br = multi*2*np.sin(theta)*np.sin(phi)*ru
    Btheta = multi*-np.cos(theta)*np.sin(phi)*thetau
    Bphi = -multi*np.cos(phi)*phiu
    fig, ax = plt.subplots()
    Hax = Br[eje1]+Btheta[eje1]+Bphi[eje1]
    Bax = Br[eje2]+Btheta[eje2]+Bphi[eje2]
    # Plot the streamlines with an appropriate colormap and arrow style
    color = 3* np.log2(np.hypot(Br[2], Btheta[1]))
    ax.streamplot(x, y, Hax, Bax, color=color, linewidth=1, cmap=plt.cm.inferno,density=2, arrowstyle='->', arrowsize=1.5)
    # Add a filled circle for the Earth; make sure it's on top of the streamlines.
    # ax.add_patch(Circle((0,0), RE, color='b', zorder=100))
    ax.set_xlabel(nombres[eje1])
    ax.set_ylabel(nombres[eje2])
    ax.set_xlim(-XMAX, XMAX)
    ax.set_ylim(-YMAX, YMAX)
    ax.set_title ("Campo eléctrico-- y")
    plt.show()
#campoEY(1,2)
def campoEX(eje1,eje2):
    Br = multi*2*np.sin(theta)*np.cos(phi)*ru
    Btheta = multi*-np.cos(theta)*np.cos(phi)*thetau
    Bphi = multi*np.sin(phi)*phiu
    fig, ax = plt.subplots()
    Hax = Br[eje1]+Btheta[eje1]+Bphi[eje1]
    Bax = Br[eje2]+Btheta[eje2]+Bphi[eje2]
    # Plot the streamlines with an appropriate colormap and arrow style
    color = 3* np.log2(np.hypot(Br[2], Btheta[1]))
    ax.streamplot(x, y, Hax, Bax, color=color, linewidth=1, cmap=plt.cm.inferno,density=2, arrowstyle='->', arrowsize=1.5)
    # Add a filled circle for the Earth; make sure it's on top of the streamlines.
    # ax.add_patch(Circle((0,0), RE, color='b', zorder=100))
    ax.set_xlabel(nombres[eje1])
    ax.set_ylabel(nombres[eje2])
    ax.set_xlim(-XMAX, XMAX)
    ax.set_ylim(-YMAX, YMAX)
    ax.set_title ("Campo eléctrico-- x")
    plt.show()
#campoEX(1,2)
def dipolo(eje1,eje2):
    Br = multi*2*(np.sin(alfa)*np.sin(phi)*np.sin(theta)+np.cos(alfa)*np.cos(theta))*ru
    Btheta = multi*(np.cos(alfa)*np.sin(theta)-np.sin(alfa)*np.cos(theta)*np.sin(phi))*thetau
    Bphi = multi*-np.sin(alfa)*np.cos(phi)*phiu
    fig, ax = plt.subplots()
    Hax = Br[eje1]+Btheta[eje1]+Bphi[eje1]
    Bax = Br[eje2]+Btheta[eje2]+Bphi[eje2]
    # Plot the streamlines with an appropriate colormap and arrow style
    color = 3* np.log2(np.hypot(Br[2], Btheta[1]))
    ax.streamplot(x, y, Hax, Bax, color=color, linewidth=1, cmap=plt.cm.inferno,density=2, arrowstyle='->', arrowsize=1.5)
    # Add a filled circle for the Earth; make sure it's on top of the streamlines.
    # ax.add_patch(Circle((0,0), RE, color='b', zorder=100))
    ax.set_xlabel(nombres[eje1])
    ax.set_ylabel(nombres[eje2])
    ax.set_xlim(-XMAX, XMAX)
    ax.set_ylim(-YMAX, YMAX)
    ax.text(20,-50,"Alfa: "+ str(alfaangle)+"°")
    ax.set_title ("Campo eléctrico dipolo")
    plt.show()
#dipolo(1,2)