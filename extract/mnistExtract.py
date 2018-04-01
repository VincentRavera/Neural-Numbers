#!/usr/bin/env python3
# coding: utf-8

from dataset.dataset import dataset


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
    data = dataset()
    return data


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
    rows = int.from_bytes(f.read(4), byteorder="big")
    cols = int.from_bytes(f.read(4), byteorder="big")
    labels = extractLabelFile(path_labels)
    # DATA
    data = dataset(number_of_images, rows, cols, labels)
    return data
