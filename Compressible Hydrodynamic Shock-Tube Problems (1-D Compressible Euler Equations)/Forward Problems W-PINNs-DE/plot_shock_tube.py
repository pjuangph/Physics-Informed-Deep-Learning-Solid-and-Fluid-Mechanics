from socket import ntohl
import matplotlib.pyplot as plt
from pathlib import Path
import scipy.io
import glob
import numpy as np 

def plot_results(prefix:str,t:np.ndarray, x:np.ndarray, p:np.ndarray, u:np.ndarray,rho:np.ndarray):
    """_summary_

    Args:
        t (np.ndarray): time
        x (np.ndarray): axial x coordinate 
        p (np.ndarray): pressure as matrix [time,x-coordinate]
        u (np.ndarray): velocity as matrix [time,x-coordinate]
        rho (np.ndarray): rho as matrix [time,x-coordinate]
    """
    X,T = np.meshgrid(x,t)
    gamma = 1.4 
    E = p/((gamma-1.0)*rho)+0.5*u**2

    fig,axes = plt.subplots(nrows=2, ncols=2,figsize=(12,8))
    plt.subplot(2,2,1)
    cs = plt.contourf(X,T,p,cmap="rainbow")
    fig.colorbar(cs, ax=axes[0,0], shrink=0.9)
    plt.ylabel('Normalized Pressure',fontsize=16)

    plt.subplot(2,2,2)
    cs = plt.contourf(X,T,u,cmap="rainbow")
    fig.colorbar(cs, ax=axes[0,1], shrink=0.9)
    plt.ylabel('Normalized u-velocity',fontsize=16)

    plt.subplot(2,2,3)
    cs = plt.contourf(X,T,rho,cmap="rainbow")
    fig.colorbar(cs, ax=axes[1,0], shrink=0.9)
    plt.ylabel('$rho$',fontsize=16)

    plt.subplot(2,2,4)
    cs = plt.contourf(X,T,E,cmap="rainbow")    
    fig.colorbar(cs, ax=axes[1,1], shrink=0.9)
    plt.ylabel('E',fontsize=16)
    plt.savefig(f'{prefix}-contour_plots.png')
    
    rho_bounds = (np.min(rho), np.max(rho))
    u_bounds = (np.min(u), np.max(u))
    p_bounds = (np.min(p), np.max(p))
    E_bounds = (np.min(E), np.max(E))


    for i in range(0,T.shape[0],1):
        x = X[i,:]
        t = T[i,1]
        # Plot vs time 
        fig, axes = plt.subplots(nrows=4, ncols=1,clear=True, num=1,figsize=(8.0,6.0))
        plt.subplot(4, 1, 1)
        plt.plot(x, rho[:,i], 'k-')
        plt.ylim(p_bounds[0],p_bounds[1])
        plt.ylabel('$rho$',fontsize=16)
        plt.tick_params(axis='x',bottom=False,labelbottom=False)
        plt.grid(True)

        plt.subplot(4, 1, 2)
        plt.plot(x, u[:,i], 'r-')
        plt.ylim(u_bounds[0],u_bounds[1])
        plt.ylabel('$U$',fontsize=16)
        plt.tick_params(axis='x',bottom=False,labelbottom=False)
        plt.grid(True)

        plt.subplot(4, 1, 3)
        plt.plot(x, p[:,i], 'b-')
        plt.ylim(p_bounds[0],p_bounds[1])
        plt.ylabel('$p$',fontsize=16)
        plt.tick_params(axis='x',bottom=False,labelbottom=False)
        plt.grid(True)

        plt.subplot(4, 1, 4)
        plt.plot(x, E[:,i], 'g-')
        plt.ylim(E_bounds[0],E_bounds[1])
        plt.ylabel('$E$',fontsize=16)
        plt.grid(True)
        plt.xlabel('x',fontsize=16)
        plt.subplots_adjust(left=0.2)
        plt.subplots_adjust(bottom=0.15)
        plt.subplots_adjust(top=0.95)
        plt.savefig(f'ml_plots/{prefix}-shocktube_t={t:0.4f}.png',dpi=300)
        plt.clf()

p = Path("ml_plots/")
p.mkdir(parents=True, exist_ok=True)
matfiles = glob.glob('*.mat')

for f in matfiles:
    mat = scipy.io.loadmat('Sod_Shock_Tube.mat')
    print(f'{f} loaded')
    nt = mat['t'].shape[1]
    nx = mat['x'].shape[1]
    rho = np.reshape(mat['rho'],(nt,nx))
    u = np.reshape(mat['u'],(nt,nx))
    p = np.reshape(mat['p'],(nt,nx))
    plot_results(f.replace('.mat',''), mat['t'], mat['x'], p, u , rho)