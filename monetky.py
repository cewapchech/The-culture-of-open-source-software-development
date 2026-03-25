import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label
import collections

def area(labeled,label=1):
    return(labeled==label).sun()

data=np.load("coins.npy")
data_label=label(data)
coins={}
summ=0
values=[1,2,5,10]



print(coins)
coins=dict(sorted(coins.items(), key=lambda item: int(item[0])))
for i in range(len(values)):
