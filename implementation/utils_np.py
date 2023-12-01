

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm

def hat(x):
    A = np.zeros((3,3))
    A[0,1:] = [-x[2],x[1]]
    A[1,::2] = [x[2],-x[0]]
    A[2,:2] = [-x[1],x[0]]
    return A

def hat_inv(S):
    x = np.zeros(S.shape[0])
    x[0] = S[2,1]
    x[1] = S[0,2]
    x[2] = S[1,0]
    return x


def check_orth(A):
    return np.linalg.norm(np.eye(A.shape[0]) - A@A.T,ord="fro")

def get_orth(n,seed = 1):
    np.random.seed(seed)
    Q,R = np.linalg.qr(np.random.rand(n,n))
    return Q

def cay(A):
    I = np.eye(A.shape[0])
    return np.linalg.inv(I - .5*A)@(I + .5*A)

def rodrigues(A):
    alpha = (1/np.sqrt(2))*np.linalg.norm(A,ord="fro")
    return np.eye(A.shape[0]) + (np.sin(alpha)/alpha)*A + ((1-np.cos(alpha))/alpha**2)*A@A

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




def frob_log(A):
    alpha = (1/np.sqrt(2))*np.linalg.norm(A,ord="fro")
    if alpha < 1e-14:
        return 0
    elif np.abs(alpha) < np.pi:
        return np.abs((alpha/(2*np.sin(alpha))))*np.linalg.norm((A-A.T),ord="fro")
    else:
        return np.sqrt(2)*np.abs(alpha)

def dist_so3(R1,R2):
    return (1/np.sqrt(2))*frob_log(R1.T@R2)

def dist_trajectory(Rs):
    dist = 0
    for R1,R2 in zip(Rs[0:-1],Rs[1:]):
        dist += dist_so3(R1,R2)
    return dist


    