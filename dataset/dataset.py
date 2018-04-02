#!/usr/bin/env python3
# coding: utf-8

import numpy as np


class OutOfBoundDataSet(Exception):
    pass


class IllegalAccessDataSet(IndexError):
    pass


class DataSet:
    row = 0
    col = 0
    data = None
    labels = None
    nb_img = 0

    def __init__(self, nb_img, labels, row, col, data):
        self.row = row
        self.col = col
        self.data = data
        self.nb_img = nb_img
        self.labels = labels

    def getLabel(self, image_number):
        return self.labels[image_number]

    def getData(self, image_number):
        if image_number < self.nb_img:
            offset = image_number*self.row*self.col
            try:
                data = self.data[offset:offset+self.row*self.col]
            except IndexError as ie:
                raise IllegalAccessDataSet(ie)
            return data
        else:
            raise OutOfBoundDataSet()

    def getImage(self, image_number):
        output = np.zeros((self.row, self.col))
        data = self.getData(image_number)
        for i in range(self.row):
            for j in range(self.col):
                output[i, j] = data[self.row*i+self.col*j]
        return output
