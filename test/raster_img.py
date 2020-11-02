# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 00:00:24 2020

@author: LeoCampos
"""

import numpy as np

from nengo.utils.matplotlib import rasterplot


from PIL import Image
import matplotlib.pyplot as plt



import nengo


class MyClass:
    def __init__(self, name):
        self.name = name



def read_img(img,n):
    temp = Image.open(img)
    x,y=temp.size
    size=[x/n,y/n]
    temp.thumbnail(size)
    temp_1 = np.asarray(temp)
    #im = Image.fromarray(a)
    
    fig, ax = plt.subplots(1,4)
    ax[0].imshow(q_0, cmap = 'gray',vmin=0, vmax=255)
    ax[1].imshow(temp_1[:,:,0], cmap = 'gray',vmin=0, vmax=255)
    ax[2].imshow(temp_1[:,:,1], cmap = 'gray',vmin=0, vmax=255)
    ax[3].imshow(temp_1[:,:,2], cmap = 'gray',vmin=0, vmax=255)
    fig.set_size_inches(20,10)
    
    
    return (temp_1)




    
    
type_img='int8'

t=1 #tiempo de sim
n=10 #tamaño de resolucion img/n

q_0 = read_img('Lenna.jpg',n)


print(q_0.shape,q_0.size,'px')

#print(q_0.min(),q_0.max())
#print(q_45.min(),q_45.max())
#print(q_90.min(),q_90.max())
#print(q_135.min(),q_135.max())

#S_0= q_0.astype(type_img) + q_90.astype(type_img)
#plot_show(q_0,q_90,S_0)
#S_1= q_0.astype(type_img) - q_90.astype(type_img)
#plot_show(q_0,q_90,S_1)
#S_2= q_45.astype(type_img) - q_135.astype(type_img)
#plot_show(q_45,q_135,S_2)




# model = nengo.Network(label='q_0')
# #q_0
# NeuronaL = {}
# with model:
#     for i in range(0,q_0.shape[0]):
#         name = i
#         NeuronaL[name] = NeuronaL.get(name, MyClass(name = name))
#         NeuronaL[name] = nengo.Ensemble(1, dimensions=q_0.shape[1])
#         input = nengo.Node(output=q_0.tolist()[name])  
#         nengo.Connection(input, NeuronaL[name]) 
        
# sim = nengo.Simulator(model)

# sim.run(t)


# # Plot the spiking output of the ensemble
# plt.figure(figsize=(10, 8))
# plt.subplot(221)
# rasterplot(sim.trange(), sim.data[1])
# plt.ylabel("Neuron")
# plt.xlim(0, 1)

