"""
María Paula Valdés Sánchez
Hector Aaron Pivaral
Teoría electromagnetica
Polarización (2)
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import colors as c
import numpy as np

Q=3e-3
a = 1
b = 3
c = 2*b
e_0 = 8.85e-12
er = 1.00065
K = 5e-9
rad = np.linspace(0, c+1, 1000)

def desplazamiento():
    z = np.zeros(1000)
    for n in range(0,1000):
        if rad[n]>=a and rad[n]<c:
            z[n]= Q/(4*np.pi*rad[n]**2)
        else:
            z[n]=0
                   
    plt.plot(rad,z)
    plt.title("Desplazamiento eléctrico esfera")
    plt.xlabel("Distancia radial (m)")
    plt.ylabel("Desplazamiento eléctrico ")
    plt.show()
#desplazamiento()
def CampoE():
    z = np.zeros(1000)
    for n in range(0,1000):
        if rad[n]<a:
            z[n] = 0
        elif rad[n]>=a and rad[n]<b:
            z[n]= Q/(4*np.pi*rad[n]**2*er*e_0)
        elif rad[n]>=b and rad[n]<c:
            z[n] = Q/(4*np.pi*rad[n]**2*e_0)+(K*rad[n])/e_0
        else:
            z[n] = Q/(4*np.pi*e_0*rad[n]**2)
    plt.title("Campo eléctrico esfera polarizada")
    plt.xlabel("Distancia radial (m)")
    plt.ylabel("Campo eléctrico (V/m)")
    plt.plot(rad,z)
    plt.show()
#CampoE()
def densidadcarga():
    fig = plt.figure()
    ax = Axes3D(fig)
    azm = np.linspace(0, 2 * np.pi, 1000)
    r, th = np.meshgrid(rad, azm)
    w, h = 1000, 1000
    zT = [x for x in range(0, 1000)]
    for n in range(0,len(rad)):
        z =[]
        for i in range(0,len(rad)):
            if rad[i] < a:
                z.append(0)
            elif rad[i] >= (a+0.05) and  rad[i] < (a+0.2):
                z.append(-Q/(4*np.pi*a**2)*(1-1/er))
            elif rad[i] >= (a+0.2) and rad[i] <= (b-0.2):
                z.append(0)
            elif rad[i] > (b-0.2) and  rad[i] < (b-0.1):
                z.append(Q/(4*np.pi*b**2)*(1-1/er))
            elif rad[i] >= (b-0.1) and rad[i] <= (b):
                z.append(0)
            elif rad[i] > (b+0.1) and  rad[i] < (b+0.2):
                z.append(K*b)
            elif rad[i] > (c-0.2) and  rad[i] < (c-0.1):
                z.append(-K*c)
            elif rad[i] > c:
                z.append(0)
            else:
                z.append(3*K)
        zT[n] = z
    plt.subplot(projection="polar")
    plt.pcolormesh(th, r, zT, shading="auto",cmap="gist_earth")
    plt.annotate(" a= "+ str(a)+"\n b= " +str(b)+" \n c= "+str(c)+" \n k= "+str(K)+" \n er= "+str(er),
                xy=(1, 2),
                xytext=(0.05, 0.05),    # fraction, fraction
                textcoords='figure fraction',
                horizontalalignment='left',
                verticalalignment='bottom',)
    plt.plot(azm, zT, color='red', ls='none')
    plt.title("Esfera polarizada")
    plt.colorbar()
    plt.grid()
    plt.show()
densidadcarga()

    
    
    
