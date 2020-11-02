# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 00:09:20 2020

@author: usuario
"""



import matplotlib.pyplot as plt
import nengo
import numpy as np

from nengo_extras.plot_spikes import (
    cluster, merge, plot_spikes, preprocess_spikes, sample_by_variance)

with nengo.Network(seed=1) as model:
    inp = nengo.Node(lambda t: [2*np.sin(16*t), 0.5])
    ens = nengo.Ensemble(10, 2)
    nengo.Connection(inp, ens)

    p = nengo.Probe(ens, synapse=0.01)
    p_spikes = nengo.Probe(ens.neurons, 'spikes')

with nengo.Simulator(model) as sim:
    sim.run(1.)
    
plt.figure()

plt.subplot(2, 1, 1)
plt.plot(sim.trange(), sim.data[p])

plt.subplot(2, 1, 2)
plot_spikes(sim.trange(), sim.data[p_spikes])
plt.xlabel("Time [s]")
plt.ylabel("Neuron number")
