import numpy as np

def calculate(lista):
    if len(lista) != 9:
        raise ValueError("List must contain nine numbers.")
    mtx = np.array(lista).reshape(3,3)
    result = {
        "mean" : [list(mtx.mean(axis=0)),list(mtx.mean(axis=1)),mtx.mean()],
        "variance" : [list(mtx.var(axis=0)),list(mtx.var(axis=1)),mtx.var()],
        "standard deviation" : [list(mtx.std(axis=0)),list(mtx.std(axis=1)),mtx.std()],
        "max" : [list(mtx.max(axis=0)),list(mtx.max(axis=1)),mtx.max()],
        "min" : [list(mtx.min(axis=0)),list(mtx.min(axis=1)),mtx.min()],
        "sum" : [list(mtx.sum(axis=0)),list(mtx.sum(axis=1)),mtx.sum()]
    }
    return result
