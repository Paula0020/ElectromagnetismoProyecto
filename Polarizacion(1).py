"""
María Paula Valdés Sánchez
Hector Aaron Pivaral
Teoría electromagnetica
Polarización (1)
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import colors as c
import numpy as np

a = 2
b = 5
K = 3e-9
alfa = 20
e_0 = 8.85e-12
rad = np.linspace(0.01, 6, 1000)
def densidadesC():
    fig = plt.figure()
    azm = np.linspace(0, 2 * np.pi, 1000)
    r, th = np.meshgrid(rad, azm)
    zT = [x for x in range(0, 1000)]
    for n in range(0,len(rad)):
        z =[]
        for i in range(0,len(rad)):
            if rad[i] < a:
                z.append(0)
            elif rad[i] >= (a+0.1) and  rad[i] < (a+0.2):
                z.append(-K*np.exp(-a**2/alfa))
            elif rad[i] > (b-0.3) and  rad[i] < (b-0.2):
                z.append(K*np.exp(-b**2/alfa))
            elif rad[i] > b:
                 z.append(0)
            else:
                z.append((-K/rad[i]*np.exp(-rad[i]**2/alfa)*(1-2*rad[i]**2/alfa)))
        zT[n] = z
    plt.subplot(projection="polar")
    plt.pcolormesh(th, r, zT, shading="auto",cmap="gist_earth")
    plt.annotate(" a= "+str(a)+" \n b= "+str(b)+" \n k= "+str(K)+" \n alpha= "+str(alfa),
                xy=(1, 2),
                xytext=(0.05, 0.05),    # fraction, fraction
                textcoords='figure fraction',
                horizontalalignment='left',
                verticalalignment='bottom',)
    plt.title("Cilindro polarizado")
    plt.plot(azm, zT, color='red', ls='none')
    plt.colorbar()
    plt.grid()
    plt.show()
#densidadesC()
def CampoEl():
    z = []
    for n in range(0,1000):
        if rad[n]<a:
            z.append(0)
        elif rad[n]>=a and rad[n]<b:
            z.append(-K/e_0*(np.exp(-rad[n]**2/alfa)))
        else:
            z.append(0)     
    plt.plot(rad,z)
    plt.title("Campo eléctrico de cilindro polarizado")
    plt.xlabel("Distancia radial (m)")
    plt.ylabel("Campo eléctrico (V/m)")
    plt.show()
CampoEl()
    