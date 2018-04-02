#!/usr/bin/env python3
# coding: utf-8

import extract.mnistExtract as xtract


data = xtract.extractImageFile("t10k-images-idx3-ubyte",
                               "t10k-labels-idx1-ubyte")
data.getData(1)
