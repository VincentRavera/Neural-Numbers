#!/usr/bin/env python3
# coding: utf-8


class Network:
    inputLayer = None
    outputLayer = None
    inners = list()

    def __init__(self, nb_inputs, nb_outputs, tuple_size_layers):
        self.inputLayer = InputLayer(nb_inputs)
        self.outputLayer = OutputLayer(nb_outputs)

        for i in tuple_size_layers:
            self.inners.append(InnerLayer(i))


class Layer:
    def __init__(self, size):
        self.size = size


class InputLayer(Layer):
    pass


class OutputLayer(Layer):
    pass


class InnerLayer(Layer):
    pass
