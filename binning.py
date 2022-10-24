import numpy as np
import matplotlib.pyplot as plt
from vorbin.voronoi_2d_binning import voronoi_2d_binning
def snr(gc,data,x,k):
	fout = open(gc.dir2+str(gc.line[k]),'w')
	N=len(data)
	for i in range(580):
		for j in range(580):
			l=int((gc.line[k]*(1+gc.redshift)-x[0])/1.25)
			dm=np.mean(data[:,i,j]) # For H-alpha line, we take 1419:1427
			Noise=np.sum((data[:,i,j]-dm)**2)
			Noise=np.sqrt(Noise/N)
			Signal=np.sqrt(np.sum(np.square(data[l-4:l+4,i,j])))
			if Noise==0: Noise=10	
			if Signal==0: Signal=1
			SNR= Signal/Noise
			print(i,j,Signal,Noise,SNR,file=fout)
	print("Signal and Noise Found")
	fout.close()
def binning(gc,k):
	if gc.binning=="Adaptive": 
		x,y,Signal,Noise=np.genfromtxt(gc.dir2+str(gc.line[k]),usecols=(0,1,2,3),unpack=True)
		i=0
		f = open(gc.dir3+str(gc.line[k]),'w')
		bin_number=0
		while i!=len(x):
			snr=Signal[i]/Noise[i]
			bin_number+=1
			while  snr<5:
				i+=1
				snr+=Signal[i]/Noise[i]
				print(x[i],y[i],bin_number,file=f)
		f.close()	
		print('Adaptive Binning Done')
		if gc.plot==True:
			x,y,bin_num=np.genfromtxt(gc.dir3+str(gc.line[k]), usecols=(0,1,2), unpack=True)
			N=max(x)
			M=max(y)
			vor=np.zeros((int(N+1),int(M+1)),dtype=float)
			for i in range(len(x)):
				vor[int(x[i]),int(y[i])]=bin_num[i]
			plt.imshow(vor)
			plt.show()
	elif gc.binning=="Normal": 
		f = open(gc.dir3,'w')
		for i in range(580):
			if i<10:
				x=int(580/gc.bin_size*10)*(int(i/gc.bin_size))
			if i>9:
				x=(580/gc.bin_size)*int(i/gc.bin_size)
			for j in range(580):
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
	x,y,bin_num=np.genfromtxt(gc.dir3, usecols=(0,1,2), unpack=True)
	L=max(bin_num)
	K=len(data[:,0,0])
	#This plot can show how the bins are separated.
	bins=np.zeros((int(L+1),int(K)),float)
	for i in range(len(x)):
		bins[int(bin_num[i]),:]+=data[:,int(x[i]),int(y[i])]
	np.savetxt(gc.dir4, np.column_stack([bins]), fmt=b'%10.2f') #This saves an array into a text file.
	print('Spectrums Created')	
	for i in range(len(gc.line)):
		x1=round((gc.line[i]-150)/100)*100
		x2=round((gc.line[i]+150)/100)*100
		diffx=x2-x1
		x=x=np.linspace(x1,x2,int(diffx/1.25))
		b1=int((x1-header[33])/1.25)
		b2=int((x2-header[33])/1.25)
		spectral_range=np.arange(b1,b2,1)					
		if gc.plot==True:	
			n=np.random.randint(1,len(bins))
			fig = plt.figure(figsize =(5, 4))
			plt.plot(x,bins[n,spectral_range])
			plt.show()


