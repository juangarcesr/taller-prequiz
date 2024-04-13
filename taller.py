#taller pre quiz
import numpy as np
import pandas as pd
import scipy as sio
#1
matriz=np.random.randint(1200000,size=(30,40,10,1000))
#2
matrizc=matriz[:,:,:,2].copy()
#3
print("forma",matrizc.shape)
print("size",matrizc.size)
print("dimension",matrizc.ndim)
print("tipo",matrizc.dtype)
print("bytes",matrizc.nbytes)
#4
x=matrizc.reshape(30,400)
print("la nueva dimension es: ",x.ndim)
#5
def data(matrizs):
    return pd.DataFrame(matrizs)
print(data(x))
#6
def cargar_mar(url):
    if url.endwith(".mat"):
        return sio.loadmat(url)
def cargar_csv(url):
    if url.endwith(".csv"):
        return pd.read_csv(url)
#7
def suma(a, axis=None):
    return np.sum(a, axis=axis)

def resta(a, axis=None):
    return np.subtract.reduce(a, axis=axis)

def multiplicacion(a, axis=None):
    return np.prod(a, axis=axis)

def division(a, axis=None):
    return np.divide.reduce(a, axis=axis)

def logaritmo(a):
    return np.log(a)

def promedio(a, axis=None):
    return np.mean(a, axis=axis)

def desviacion_estandar(a, axis=None):
    return np.std(a, axis=axis)