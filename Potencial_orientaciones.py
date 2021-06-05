import numpy as np
import matplotlib.pyplot as plt

# Cartesian axis system with origin at the dipole (m)
X = np.linspace(-3,3,100)
Y =  np.linspace(-3,3,100)
phi,theta = np.linspace(0,2*np.pi,100),np.linspace(0,np.pi,100)
#r = np.linspace(0.1,2*np.pi,200)
x,y = np.meshgrid(X, Y)
r = np.hypot(x,y)
nombres = ["$y^j$","$x^i$","$z^k$"]
e_o = 8.85e-12    #degree
po = 6.7e-10
Phi = [po/(4*np.pi*e_o*r**2)*np.sin(theta)*np.sin(phi),po/(4*np.pi*e_o*r**2)*np.sin(theta)*np.cos(phi),po/(4*np.pi*e_o*r**2)*np.cos(theta)]
def potencial(n):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # Draw contours at values of Phi given by levels
    levels = np.array([10**pw for pw in np.linspace(0,5,20)])
    levels = sorted(list(-levels) + list(levels))
    # Monochrome plot of potential
    ax.contour(x, y, Phi[n],levels=levels, colors='k', linewidths=2)
    ax.set_title(r'Potencial--dipolo en '+ nombres[n], fontsize=20)
    plt.show()
potencial(1)