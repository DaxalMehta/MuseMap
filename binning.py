import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from vorbin.voronoi_2d_binning import voronoi_2d_binning
import white_stat
import os
from matplotlib.backends.backend_pdf import PdfPages
import aux
def binning(gc,dat,header):
	if gc.binning=="Voronoi": 
		if os.path.exists(gc.dir2)==True: #and os.path.exists(gc.white)==True: 
			x,y,Signal,Noise=np.genfromtxt(gc.dir2,usecols=(0,1,2,3),unpack=True)
		else :#os.path.exists(gc.dir2)==False:
			white_stat.snr(gc,dat,header)
			x,y,Signal,Noise=np.genfromtxt(gc.dir2,usecols=(0,1,2,3),unpack=True)
		if os.path.exists(gc.dir3)==False:
			bin_number, x_gen, y_gen, x_bar, y_bar, sn, nPixels, scale = voronoi_2d_binning(x, y, Signal, Noise, gc.snr, cvt=True, pixelsize=1, plot=False, quiet=True, sn_func=None, wvt=True) # Voronoi binning.
			np.savetxt(gc.dir3, np.column_stack([x, y, bin_number]),fmt=b'%4i %4i %8i')	
			print('Voronoi Binning Done')	
		if gc.plot==True:
			x,y,bin_num=np.genfromtxt(gc.dir3, usecols=(0,1,2), unpack=True)
			N=max(x)
			M=max(y)
			vor=np.zeros((int(N+1),int(M+1)),dtype=float)
			for i in range(len(x)):
				vor[int(x[i]),int(y[i])]=bin_num[i]
			plt.imshow(vor,norm=colors.LogNorm())
			plt.colorbar()
			plt.show()
	elif gc.binning=="Normal": 
		f = open(gc.dir3,'w')
		for i in range(gc.grid_size):
			if i<gc.bin_size:
				x=int(gc.grid_size/gc.bin_size*10)*(int(i/gc.bin_size))
			if i>gc.bin_size-1:
				x=(gc.grid_size/gc.bin_size)*int(i/gc.bin_size)
			for j in range(gc.grid_size):
				y=int(j/gc.bin_size)+1
				bin_number=x+y
				print(i,j,bin_number,file=f)

		f.close()
		print('Normal Binning Done')
		if gc.plot==True:
			x,y,bin_num=np.genfromtxt(gc.dir3, usecols=(0,1,2), unpack=True)
			N=max(x)
			M=max(y)
			vor=np.zeros((int(N+1),int(M+1)),dtype=float)
			for i in range(len(x)):
				vor[int(x[i]),int(y[i])]=bin_num[i]
			plt.imshow(vor)
			plt.show()

def bins(gc,data,header):
#	if os.path.exists(gc.dir4)==True:
#		return
#		print('Spectrums Printed')
	if os.path.exists(gc.dir4)==False:
		x,y,bin_num=np.genfromtxt(gc.dir3, usecols=(0,1,2), unpack=True)
		b1,b2,slices=aux.slice_range(gc,header)
		L=max(bin_num)
		K=len(data[b1:b2,0,0])
		bins=np.zeros((int(L+1),int(K)),float)
		for i in range(len(x)):
			bins[int(bin_num[i]),:]+=data[b1:b2,int(x[i]),int(y[i])]
		np.savetxt(gc.dir4, np.column_stack([bins]), fmt=b'%10.2f') #This saves an array into a text file.
		print('Bins Created')	
"""		pdf = PdfPages(gc.dir5)
		x=spectral_range(gc)
		b1,b2,slices=slice_range(gc,header)
		for i in range(len(bins)):
			d=bins[i,b1:b2]	
			fig = plt.figure(figsize =(5, 4))
			plt.plot(x,d)
			pdf.savefig(fig)
			plt.close()
		pdf.close()
		print('Spectrums Printed')	
	for i in range(len(gc.line)):
		x1,x2,x=aux.spectral_range(gc)
		b1,b2,slices=aux.slice_range(gc,header)
		if gc.plot==True:	
			n=np.random.randint(1,len(bins))
			fig = plt.figure(figsize =(5, 4))
			plt.plot(x,bins[n,spectral_range])
			plt.show()
"""

