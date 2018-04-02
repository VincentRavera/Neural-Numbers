#!/usr/bin/env python3
# coding: utf-8

from dataset.dataset import DataSet
import numpy as np


def extractLabelFile(path):
    # Structure is as follows:
    # [offset] [type]          [value]          [description]
    # 0000     32 bit integer  0x00000801(2049) magic number (MSB first)
    # 0004     32 bit integer  60000            number of items
    # 0008     unsigned byte   ??               label
    # 0009     unsigned byte   ??               label
    # ........
    # xxxx     unsigned byte   ??               label
    # The labels values are 0 to 9.
    f = open(path, "rb")
    f.close()
    return 0


def extractImageFile(path_img, path_labels):
    # Structure is as follows:
    # [offset] [type]          [value]          [description]
    # 0000     32 bit integer  0x00000803(2051) magic number
    # 0004     32 bit integer  60000            number of images
    # 0008     32 bit integer  28               number of rows
    # 0012     32 bit integer  28               number of columns
    # 0016     unsigned byte   ??               pixel
    # 0017     unsigned byte   ??               pixel
    # xxxx     unsigned byte   ??               pixel
    f = open(path_img, "rb")
    # HEADER
    int.from_bytes(f.read(4), byteorder="big")
    number_of_images = int.from_bytes(f.read(4), byteorder="big")
    row = int.from_bytes(f.read(4), byteorder="big")
    col = int.from_bytes(f.read(4), byteorder="big")
    labels = extractLabelFile(path_labels)
    # DATA
    data = np.zeros(number_of_images*row*col)
    EOF = b''
    byte = f.read(1)
    i = 0
    while byte != EOF:
        data[i] = int.from_bytes(byte, byteorder="big")
        byte = f.read(1)
        i += 1
    dataset = DataSet(number_of_images, labels, row, col, data)
    f.close()
    return dataset
