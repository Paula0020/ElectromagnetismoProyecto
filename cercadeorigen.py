import numpy as np
import matplotlib.pyplot as plt

# Cartesian axis system with origin at the dipole (m)
X = np.linspace(-2.5,2.5,100)
Y =  np.linspace(-2.5,2.5,100)
phi = np.linspace(0,2*np.pi,100)
#r = np.linspace(0.1,2*np.pi,200)
x,y = np.meshgrid(X, Y)
theta = [np.linspace(0,np.pi,100) for x in range(0, 100)]
r = np.hypot(x,y)
e_o = 8.85e-12    #degree
def potencial():
    phi = 1/(4*np.pi*e_o)*(1/r+1/r**3*(3-9*np.cos(theta)**2))
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # Draw contours at values of Phi given by levels
    levels = np.array([10**pw for pw in np.linspace(0,5,20)])
    levels = sorted(list(-levels) + list(levels))
    # Monochrome plot of potential
    ax.contour(x, y, phi,levels=levels, colors='k', linewidths=2)
    ax.set_title("Potencial cercano al origen", fontsize=15)
    ax.text(-1,-2,"grid (-2.5,2.9)")
    plt.show()
potencial()