#!/usr/bin/env python3
# coding: utf-8

import numpy as np

# Network:
# input(I)    bound0(I*K)   layer0(K)  blb layerN(M)   boundN(M,J)    output(J)
#   i(0)    x(0,0)...x(0,K)    l0(0)   ...   lN(0)   x(0,0)...x(0,J)     o(0)
#   i(1)    x(1,0)...x(1,K)    l0(1)   ...   lN(1)   x(1,0)...x(1,J)     o(1)
#   i(2)    x(2,0)...x(2,K)    l0(2)   ...   lN(2)   x(2,0)...x(2,J)     o(2)
#    .      ...............      .     ...     .     ...............      .
#   i(i)         x(i,k)        l0(k)   ...   lN(m)        x(m,k)         o(j)
#    .      ...............      .     ...     .     ...............      .
#   i(I)    x(I,0)...x(I,K)    l0(K)   ...   lN(m)   x(M,0)...x(I,J)     o(J)


class Network:
    inputLayer = None
    outputLayer = None
    layers = list()
    bounds = list()

    # An Idea is to include I/O in the tuple
    def __init__(self, nb_inputs, nb_outputs, tuple_size_layers):

        # Manually set I/O
        self.inputLayer = Layer(nb_inputs)
        self.outputLayer = Layer(nb_outputs)

        if tuple_size_layers is None:
            # Manually set I/O
            self.bounds.append(Bounds(nb_inputs, nb_outputs))
        else:
            # Manually set IN
            self.bounds.append(Bounds(nb_inputs, tuple_size_layers[0]))

            # Build Inner Layers
            for i in range(len(tuple_size_layers)):
                self.Layers.append(Layer(i))

            # Since Bounds 0 and N are set manualy because they are linked to
            # I/O we can iterate over N-2
            for i in tuple_size_layers[1:-1]:
                self.bounds.append(Bounds(tuple_size_layers[i],
                                          tuple_size_layers[i+1]))
            # Manually set OUT
            self.bounds.append(Bounds(tuple_size_layers[-1], nb_outputs))

    def clearNodes(self):
        self.inputLayer.clearNodes()
        self.outputLayer.clearNodes()
        for i in self.layers:
            i.clearNodes()

    def backPropagate(self):
        pass

    def compute(self, input_data):
        self.inputLayer.nodes = input_data


class Layer:
    def __init__(self, size):
        self.size = size
        self.nodes = np.zeroes(size)

    def clearNodes(self):
        self.nodes = np.zeroes(self.size)


class Bounds:
    def __init__(self, sizein, sizeout):
        self.bounds = np.random.random((sizein, sizeout))
        self.bias = np.random.random(sizeout)
