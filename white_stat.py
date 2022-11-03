import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
import os
def snr(gc,data,header):
#	print(gc.grid_size)
	Signal=np.zeros((gc.grid_size,gc.grid_size),float)
	Noise=np.zeros((gc.grid_size,gc.grid_size),float)
#	data=data[:,200:400,200:400]
	fout = open(gc.dir2,'w')
	N=len(data)
	if os.path.exists(gc.white)==True and os.path.exists(gc.stat)==True:
		white=fits.open(gc.white)
		white=white[0].data
#		white=white[200:400,200:400]
		stat=fits.open(gc.stat)
		stat=stat[0].data
		if gc.plot==True:
			plt.imshow(white)
			plt.show()
			plt.imshow(stat)
			plt.show()
		for i in range(gc.grid_size):
			for j in range(gc.grid_size):
				Signal[i,j]=white[i,j]
				Noise[i,j]=stat[i,j]
				if Noise[i,j]==0: Noise[i,j]=0.1	
				if Signal[i,j]==0: Signal[i,j]=0.01
				print(i,j,Signal[i,j],Noise[i,j],file=fout)
	else:
		for i in range(gc.grid_size):
			for j in range(gc.grid_size):
				l=int((gc.line[0]*(1+gc.redshift)-header[33])/1.25)
				#print(l)
				dat1=data[:l-3,i,j]
				dat2=data[l+3:,i,j]
				dat=np.concatenate((dat1,dat2))
				Noise[i,j]=np.std(dat)
				Signal[i,j]=np.sum((data[l-3:l+3,i,j]))
				if Noise[i,j]==0: Noise[i,j]=0.1	
				if Signal[i,j]==0: Signal[i,j]=0.01
				print(i,j,Signal[i,j],Noise[i,j],file=fout)
		hdu=fits.PrimaryHDU(data=Signal)
		hdu.writeto(gc.white,overwrite=True)
		hdu=fits.PrimaryHDU(data=Noise)
		hdu.writeto(gc.stat,overwrite=True)
		print("White.fits, Stat.fits, and Voronoi_Input created.")
	fout.close()

