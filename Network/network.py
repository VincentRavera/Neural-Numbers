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
    inputLayer = None       # For Shortcut
    outputLayer = None      # For Shortcut
    layers = list()
    bounds = list()

    # Tuple[0] must be the size of inputs
    # Tuple[-1] muste be the size of outputs
    def __init__(self, tuple_size_layers):
        """The Tuple must"""
        if len(tuple_size_layers) < 2:
            raise BadNetworkSizeException(len(tuple_size_layers))

        # Build Inner Layers
        for i in range(len(tuple_size_layers)):
            self.Layers.append(Layer(i))

        # For N Layers (including I/0) there are N-1 Bounds
        for i in range(len(tuple_size_layers)-1):
            bound = Bounds(tuple_size_layers[i], tuple_size_layers[i+1])
            self.bounds.append(bound)
            self.layers[i].bound = bound
        # Enables Quick Access
        self.inputLayer = self.layers[0]
        self.outputLayer = self.layers[-1]

    def clearNodes(self):
        for i in self.layers:
            i.clearNodes()

    def backPropagate(self):
        pass

    def compute(self, input_data):
        self.inputLayer.nodes = input_data


class Layer:
    bound = None       # If None then Layer is the Output Layer

    def __init__(self, size):
        self.size = size
        self.nodes = np.zeroes(size)

    def clearNodes(self):
        self.nodes = np.zeroes(self.size)


class Bounds:
    def __init__(self, sizein, sizeout):
        self.bounds = np.random.random((sizein, sizeout))
        self.bias = np.random.random(sizeout)


class BadNetworkSizeException(Exception):
    def __init__(self, size):
        self.msg = \
            "The Number of layer must be at least 2, and not " + str(size)
