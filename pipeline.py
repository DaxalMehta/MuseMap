import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
import os
import cla
import binning
import fitting
import mapping
import time

a=cla.dat()
if not os.path.exists(a.dir):
    os.mkdir(a.dir)
dat=fits.open(a.dir1)
header=dat[0].header
dat=dat[0].data
dat=dat[:,:580,:580]
N=len(a.line)
t1=time.time()
binning.binning(a)
binning.bins(dat,a)
for i in range(N):
	x1=round((a.line[i]-150)/100)*100
	x2=round((a.line[i]+150)/100)*100
	diffx=x2-x1
	x=x=np.linspace(x1,x2,int(diffx/1.25))
	b1=int((x1-header[33])/1.25)
	b2=int((x2-header[33])/1.25)
	spectral_range=np.arange(b1,b2,1)
#	binning.binning(a) Inside the loop when do intelligent binning
	if a.plot==True:
		binning.spectrum(a,x,spectral_range)
#	fitting.fitting(a,x,spectral_range,i)

#mapping.mapping(a)
t2=time.time()
print(t2-t1)

