import numpy as np

def calculate(list):
    if len(list)<9:
        raise ValueError("List must contain nine numbers.")
    nlist = np.asarray(list)
    nlist = nlist.reshape((3,3))
    dict = {
        "mean":[nlist.mean(axis=0).tolist(),nlist.mean(axis=1).tolist(),nlist.mean()],
        "variance":[nlist.var(axis=0).tolist(),nlist.var(axis=1).tolist(),nlist.var()],
        "standard deviation":[nlist.std(axis=0).tolist(),nlist.std(axis=1).tolist(),nlist.std()],
        "max":[np.amax(nlist,axis=0).tolist(),np.amax(nlist,axis=1).tolist(),np.amax(nlist)],
        "min":[np.amin(nlist,axis=0).tolist(),np.amin(nlist,axis=1).tolist(),np.amin(nlist)],
        "sum":[nlist.sum(axis=0).tolist(),nlist.sum(axis=1).tolist(),nlist.sum()]
    }
    return dict
  
    
  