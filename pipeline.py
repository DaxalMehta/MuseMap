import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
import os
import cla
import binning
import fitting
import mapping
import time
import aux
gc=cla.dat()
if not os.path.exists(gc.dir):
    os.mkdir(gc.dir)
dat=fits.open(gc.dir1)
header=dat[0].header
dat=dat[0].data
#dat=dat[:,200:400,200:400]
#if gc.binning=="Voronoi":
dat=dat[:,gc.xpos-int(gc.grid_size/2):gc.xpos+int(gc.grid_size/2),gc.ypos-int(gc.grid_size/2):gc.ypos+int(gc.grid_size/2)]
#print(gc.xpos-gc.grid_size/2,gc.xpos+gc.grid_size/2)
#if gc.binning=="Normal":
#	dat=dat[:,:gc.grid_size,:gc.grid_size]
N=len(gc.line)
t1=time.time()
#print(header)
#print(os.path.exists(gc.dir2))
#"""
binning.binning(gc,dat,header)
binning.bins(gc,dat,header)

for i in range(N):
	x1,x2,x=aux.spectral_range(gc,header)
	b1,b2,slices=aux.slice_range(gc,header)
	fitting.fitting(gc,x,slices,i)
#"""
mapping.mapping(gc)

t2=time.time()
print(t2-t1)

