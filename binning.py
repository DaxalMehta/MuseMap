import numpy as np
import matplotlib.pyplot as plt
from vorbin.voronoi_2d_binning import voronoi_2d_binning
def snr(data, signal_range, directory):
	fout = open(directory.dir2,'w')
	N=len(data)
	for i in range(580):
		for j in range(580):
			dm=np.mean(data[:,i,j]) # For H-alpha line, we take 1419:1427
			Noise=np.sum((data[:,i,j]-dm)**2)
			Noise=np.sqrt(Noise/N)
			Signal=np.sqrt(np.sum(np.square(data[signal_range,i,j])))
			if Noise==0: Noise=10	
			if Signal==0: Signal=1
			SNR= Signal/Noise
			print(i,j,Signal,Noise,SNR,file=fout)
	fout.close()
	print(np.amax(Signal),np.amin(Signal))
	print(np.amax(Noise),np.amin(Noise))
def binning(directory):
	if directory.vor==True: 
		x, y, signal, noise = np.genfromtxt(directory.dir2, usecols=(0,1,2,3),unpack=True)# Extract the required data to perform vornoi binning,
		bin_number, x_gen, y_gen, x_bar, y_bar, sn, nPixels, scale = voronoi_2d_binning(x, y, signal, noise, 20, cvt=True, pixelsize=0.2)#, plot=True, quiet=True, sn_func=None, wvt=True) # Voronoi binning.
		np.savetxt(directory.dir3, np.column_stack([x, y, bin_number]),fmt=b'%4i %4i %8i')
		print('Voronoi Binning done')
	else: 
		f = open(directory.dir3,'w')
		for i in range(580):
			if i<10:
				x=int(580/directory.bin_size*10)*(int(i/directory.bin_size))
			if i>9:
				x=(580/directory.bin_size)*int(i/directory.bin_size)
			for j in range(580):
				y=int(j/directory.bin_size)+1
				bin_number=x+y
				print(i,j,bin_number,file=f)

		f.close()
		print('Normal Binning done')
	if directory.plot==True:
		x,y,bin_num=np.genfromtxt(directory.dir3, usecols=(0,1,2), unpack=True)
		N=max(x)
		M=max(y)
		vor=np.zeros((int(N+1),int(M+1)),dtype=float)
		for i in range(len(x)):
			vor[int(x[i]),int(y[i])]=bin_num[i]
		plt.imshow(vor)
		plt.show()

def bins(data,directory):
	x,y,bin_num=np.genfromtxt(directory.dir3, usecols=(0,1,2), unpack=True)
	L=max(bin_num)
	K=len(data[:,0,0])
	#This plot can show how the bins are separated.
	bins=np.zeros((int(L+1),int(K)),float)
	for i in range(len(x)):
		bins[int(bin_num[i]),:]+=data[:,int(x[i]),int(y[i])]
	np.savetxt(directory.dir4, np.column_stack([bins]), fmt=b'%10.6f') #This saves an array into a text file.
	print('Spectrums created')
def spectrum(directory,axis,spectrum_range):
	bins=np.genfromtxt(directory.dir4)
	n=np.random.randint(1,len(bins))
	fig = plt.figure(figsize =(5, 4))
	plt.plot(axis,bins[n,spectrum_range])
	plt.show()


