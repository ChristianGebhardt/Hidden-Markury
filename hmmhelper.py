import oshelper as oh
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import hmmlearn

# (universal) function to load data-file
def load_trace(data_path,DD_col=1,DA_col=2,E_col=-1,delimiter=None,orientation=None):
    """The function is a universal import function for FRET time traces, which can handle csv and tsv file formats.
    It detects automatically if a header was specified or not and if the x/y data are stored as rows or as columns.
    The return values are
    - T_values as numpy-array : time axis of the FRET trace
    - DD_values as numpy-array : donor channel photons per time bin (optional)
    - DA_values as numpy-array : acceptor channel photons per time bin (optional)
    - E_values as numpy-array : FRET efficiency values (optional)
    - header as list (if detected) or None (if not detected)
    """
    #data_path = os.path.join(folder, filename)
    if delimiter is not None:
        df = pd.read_csv(data_path, header=None, skiprows=0, sep=delimiter)
    elif data_path[-4:]==".csv":
        df = pd.read_csv(data_path, header=None, skiprows=0)
    elif data_path[-4:]==".tsv":
        df = pd.read_csv(data_path, header=None, skiprows=0, sep='\t')
    else:
        warnings.warn("unknown file format....import might return wrong values", Warning)
        df = pd.read_csv(data_path, header=None, skiprows=0)
        
    #extract header and data
    assert (DD_col>0 and DA_col>0) or E_col>0, "The trace must contain either DD & DA photon counts or E values"
    if (df.shape[0]<df.shape[1] and orientation==None) and orientation=='h': #data are horizontally orientated (2 rows)
        horizontal = True
        header = list(df[df.columns[0]])
    elif (df.shape[0]>df.shape[1] and orientation==None) or orientation=='v':              #data are vertically orientated (2 columns)
        horizontal = False
        header = list(df.iloc[0])
    # check for header
    if not isinstance(header[0],str):
        header = None
        header_idx = 0
        #print("-- no header --")
    else:
        header_idx = 1
        #print("-- header --")
        #print(header)
    DD_values, DA_values, E_values = np.array([]), np.array([]), np.array([])
    if horizontal:     #take first row for x-values and second row for y-values
        #print("-- horizontal orientation --")
        T_values = np.array(df.iloc[0].values[header_idx:])
        if DD_col>0:
            DD_values = np.array(df.iloc[DD_col].values[header_idx:])
        if DA_col>0:
            DA_values = np.array(df.iloc[DA_col].values[header_idx:])
        if E_col>0:
            E_values = np.array(df.iloc[E_col].values[header_idx:])
    else:              #take first column for x-values and second column for y-values
        #print("-- vertical orientation --")
        T_values = np.array(df[df.columns[0]][header_idx:])
        if DD_col>0:
            DD_values = np.array(df[df.columns[DD_col]][header_idx:])
        if DA_col>0:
            DA_values = np.array(df[df.columns[DA_col]][header_idx:])
        if E_col>0:
            E_values = np.array(df[df.columns[E_col]][header_idx:])
        
    T_values = T_values.astype('float64') 
    DD_values = DD_values.astype('float64')
    DA_values = DA_values.astype('float64')
    E_values = E_values.astype('float64')
    
    return T_values, DD_values, DA_values, E_values, header

# (plot selected traces
def plot_traces(N_traces,start=0, traces_DD=[], traces_DA=[], traces_E=[],prediction=False):
    plt_rows = 0
    if len(traces_DD)>0 and len(traces_DA)>0:
        DD_min = min([min(t[:,1]) for t in traces_DD])
        DD_max = max([max(t[:,1]) for t in traces_DD])
        DA_min = min([min(t[:,1]) for t in traces_DA])
        DA_max = max([max(t[:,1]) for t in traces_DA])
        pr = [DD_min, DD_max, DA_min, DA_max]
        plt_rows += 2
    if len(traces_E)>0:
        plt_rows += 1
    fig, axes = plt.subplots(plt_rows,N_traces,figsize=(15,plt_rows*3))
    if N_traces==1 and plt_rows==1:
        axes=[[axes]]
    elif N_traces==1 and plt_rows>1:
        axes = [[axes[i]] for i in range(len(axes))]
    elif N_traces>1 and plt_rows==1:
        axes = [axes]    
    fig.text(0.5, 0.01, 'Time, t [s]', ha='center')
    fig.text(0.04, 0.5, 'Intensity, [a.u.]', va='center', rotation='vertical')
    for i in range(N_traces):
        if len(traces_DD)>0 and len(traces_DA)>0:
            axes[0][i % N_traces].plot(traces_DD[start+i][0], traces_DD[start+i][1],color='green')
            axes[0][i % N_traces].set_ylim([pr[0],pr[1]])
            axes[1][i % N_traces].plot(traces_DA[start+i][0], traces_DA[start+i][1],color='red')
            axes[1][i % N_traces].set_ylim([pr[2],pr[3]])
            axes[0][0].set_ylabel('DD')
            axes[1][0].set_ylabel('DA')
            if prediction:
                axes[0][i % N_traces].plot(traces_DD[start+i][0], traces_DD[start+i][2])
                axes[1][i % N_traces].plot(traces_DA[start+i][0], traces_DA[start+i][2])
        if len(traces_E)>0:
            axes[plt_rows-1][i % N_traces].plot(traces_E[start+i][0], traces_E[start+i][1])
            axes[plt_rows-1][i % N_traces].set_ylim(-0.1,1.1)
            axes[plt_rows-1][0].set_ylabel('E')
            if prediction:
                axes[plt_rows-1][i % N_traces].plot(traces_E[start+i][0], traces_E[start+i][2])
        #elif len(traces_E)>0 and plt_rows==1:
        #    axes[i % N_traces].plot(traces_E[start+i][0], traces_E[start+i][1])
        #    axes[i % N_traces].set_ylim(-0.1,1.1)            
        #    axes[0].set_ylabel('E')
        #    if prediction:
        #        axes[i % N_traces].plot(traces_E[start+i][0], traces_E[start+i][2])
    plt.show()
    plt.close()
    
def grouped_list(iterable, n):
    "s -> (s0,s1,s2,...sn-1), (sn,sn+1,sn+2,...s2n-1), (s2n,s2n+1,s2n+2,...s3n-1), ..."
    return zip(*[iter(iterable)]*n)

def print_gaussians(guess, mode='2D'):
    print("---------------------------------------\nGaussian parameter")
    if mode=='2D':
        gaussians = grouped_list(guess, 5)
        for i, gauss in enumerate(gaussians):
            print("Gaussian {0:d}: A{0:d}:{1:.0f}, mu_DD{0:d}:{2:.2f}, sigma_DD{0:d}:{3:.2f}, mu_DA{0:d}:{4:.2f}, sigma_DA{0:d}:{5:.2f}".format(i,*gauss))
    if mode=='1D':
        gaussians = grouped_list(guess, 3)
        for i, gauss in enumerate(gaussians):
            print("Gaussian {0:d}: A{0:d}:{1:.0f}, mu_E{0:d}:{2:.2f}, sigma_E{0:d}:{3:.2f}".format(i+1,*gauss))
    print("---------------------------------------")
    
def gauss_2D(xy, *params):
    #print(xy)
    (x, y) = xy
    z = np.zeros_like(x)
    for i in range(0, len(params), 5):
        amp = params[i]
        mu = params[i+1]
        sigma = params[i+2]
        mu2 = params[i+3]
        sigma2 = params[i+4]
        z = z + amp * np.exp( -0.5*((x - mu)/sigma)**2)* np.exp( -0.5*((y - mu2)/sigma2)**2)
    return z

def gauss_1D(x, *params):
    y = np.zeros_like(x)
    #print(params)
    for i in range(0, len(params), 3):
        amp = abs(params[i])
        mu = params[i+1]
        sigma = abs(params[i+2])
        #print(sigma)
        y = y + amp * np.exp( -0.5*((x - mu)/sigma)**2)
    return y

def func_exp(x,A,lmd):
    y = np.zeros_like(x)
    y = A*np.exp(-lmd*x)
    return y

def generate_hmm_initials(gauss_fits, degeneration, mode):
    states_N = sum(degeneration)
    if mode=='2D':
        gauss_N = 5
    else:
        gauss_N = 3
    gauss_select = []
    for pos, deg in enumerate(degeneration):
        for not_used in range(deg):
            gauss_select += list(gauss_fits[gauss_N*pos:gauss_N*(pos+1)])
    if mode=='2D':
        #GAUSS_N = 5
        means = [[mu,mu2] for A,mu,sigma,mu2,sigma2 in grouped_list(gauss_select, gauss_N)]
        covs = [[[sigma**2,0],[0,sigma2**2]] for A,mu,sigma,mu2,sigma2 in grouped_list(gauss_select, gauss_N)]
        starts = np.array([A*sigma*sigma2 for A,mu,sigma,mu2,sigma2 in grouped_list(gauss_select, gauss_N)])
    else:
        #GAUSS_N = 5
        means = [[mu] for A,mu,sigma in grouped_list(gauss_select, gauss_N)]
        covs = [[[sigma**2]] for A,mu,sigma in grouped_list(gauss_select, gauss_N)]
        starts = np.array([A*sigma for A,mu,sigma in grouped_list(gauss_select, gauss_N)])
    starts = starts/np.sum(starts)

    trans_mat = np.zeros((states_N,states_N))
    for i in range(0,states_N):
        for j in range(0,states_N):
            if i==j:
                trans_mat[i,j] = 0.96
            else:
                trans_mat[i,j] = 0.04/(states_N-1)
    return means, covs, trans_mat, starts

def split_trace(trace,nbr_max=None,skip_last=True):
    if nbr_max == None:
        nbr_max = max(trace)

    lifetimes = [[] for s in range(nbr_max+1)]
    for s in range(nbr_max):
        lifetimes[s] = []
    state = trace[0]
    lt = -1
    for idx in range(1,len(trace)):
        lt +=1
        if trace[idx] == state:
            continue
        else:
            lifetimes[state].append(lt)
            lt = -1
            state = trace[idx]
    if not skip_last:
        lifetimes[state].append(lt)
    return lifetimes

def cumulate_lifetimes(lifetimes_traces):
    lifetimes_cum = [l for l in lifetimes_traces[0]]
    for l in lifetimes_traces[1:]:
        for idx in range(len(lifetimes_cum)):
            lifetimes_cum[idx] = lifetimes_cum[idx]+l[idx]
    return lifetimes_cum

def save_model(model,path):
    with open(path,'w') as f:
        f.write('HMM\n')
        f.write('---------------------------------\n\n')
        f.write('Means\n')
        f.write(str(model.means_)+'\n')
        f.write('---------------------------------\n\n')
        f.write('Covariances (sigma^2)\n')
        f.write(str(model.covars_)+'\n')
        f.write('---------------------------------\n\n')
        f.write('Start probability\n')
        f.write(str(model.startprob_)+'\n')   
        f.write('---------------------------------\n\n')
        f.write('Transition matrix\n')
        f.write(str(model.transmat_)+'\n')
    