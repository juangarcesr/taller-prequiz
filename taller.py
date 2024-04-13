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
