import numpy as np
from matplotlib import pyplot as plt
from utils_np import check_orth


def get_sphere_energy(energy,l):

    u = np.linspace(0, 2*np.pi,200)
    v = np.linspace(0, np.pi, 200)
    x = np.outer(np.cos(u), np.sin(v)) 
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))

    WW = x.copy()
    for i in range( len( x ) ):
        for j in range( len( x ) ):
            xx = x[ i, j ]
            yy = y[ i, j ]
            zz = z[ i, j ]
            WW[ i, j ] = energy(np.array( [xx, yy, zz ] ),l)
    WW = WW / np.amax( WW )
    myheatmap = WW

    fig = plt.figure(figsize=(10,10))
    ax = plt.axes(projection='3d')
    ax.plot_surface(x, y, z, color='g',alpha=0.2,cmap=plt.cm.YlGnBu_r,facecolors=cm.jet( myheatmap ))

    return ax


def get_sphere():

    u = np.linspace(0, 2*np.pi,200)
    v = np.linspace(0, np.pi, 200)
    x = np.outer(np.cos(u), np.sin(v)) 
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))

    fig = plt.figure(figsize=(10,10))
    ax = plt.axes(projection='3d')
    ax.plot_surface(x, y, z, color='g',alpha=0.2,cmap=plt.cm.YlGnBu_r)

    return ax



def plot_discrete_energy_balance(H,yTu,dt,ws,Rs):
    ytu = np.array([dt*yTu(R0,w0,w1) for w0,R0,w1,R1 in zip(ws[:-1],Rs[:-1],ws[1:],Rs[1:])])
    dh = [(H(w1)-H(w0)) for w0,R0,w1,R1 in zip(ws[:-1],Rs[:-1],ws[1:],Rs[1:])]

    ts = np.linspace(0,dt*len(ytu),len(ytu))

    plt.plot(ts,dh,label=r"$H(x_{n+1}) - H(x_n)$")
    plt.plot(ts,ytu,"--",label=r"$hy_n^Tu_n$",)
    plt.legend()
    plt.ylabel("Energy")
    plt.xlabel(r"Time $t_n$")
    plt.title("Discrete energy balance")
    plt.show()



    plt.semilogy(ts,np.abs(ytu - dh),label=r"$|H(x_{n+1}) - H(x_n) - hy_n^Tu_n|$")
    plt.legend()
    plt.ylabel("Energy")
    plt.xlabel(r"Time $t_n$")
    plt.title("Energy balance error")
    plt.show()

def plot_energy_orth(H,dt,ws,Rs,H_ref = None):
    ts = np.linspace(0,dt*len(ws),len(ws))


    plt.semilogy(ts,[check_orth(R) for R in Rs],label=r"$|| I - R_n^TR_n ||$")
    plt.semilogy(ts,[H(w) for w in ws],label=r"Kinetic energy $H(x_n)$")
    if H_ref:
        plt.semilogy(ts,[H_ref(R) for R in Rs],label=r"Control energy $H_{ref}(x_n)$")
    plt.legend()
    plt.xlabel(r"Time $t_n$")
    plt.title("Energy and orthogonality")
    plt.show()

def plot_trajectory_S2(R0,Rs,Rref=None,i=0):
    ax = get_sphere()
    ax.plot3D(R0[0,i],R0[1,i],R0[2,i],'o',c="blue",label="Initial orientation")
    if type(Rref) == np.ndarray:
        ax.plot3D(Rref[0,i],Rref[1,i],Rref[2,i],'o',c="red",label="Desired orientation")
    ax.plot3D(Rs[:,0,i],Rs[:,1,i],Rs[:,2,i],'k-',label="Trajectory")
    plt.legend()
    plt.title(f"Orientation given by $r_{i} \in S^2$")
    plt.show()