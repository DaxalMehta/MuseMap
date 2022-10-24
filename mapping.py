import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib import cm
def mapping(gc):
	N=len(gc.line)
	fig,axs=plt.subplots(N,3)
	for k in range(N):
		Intensity,Rel_velocity,Vel_dispersion,Deviation=np.genfromtxt(gc.dir5+"_"+str(gc.line[k]),usecols=(5,1,2,4),unpack=True)
#		Rel_velocity=(Rel_velocity/gc.line[k]-1)*299793.4
#		mean_vel=np.mean(Rel_velocity)
#		print(mean_vel)
#		Vel_dispersion=(Vel_dispersion/gc.line[k])*299793.4
		SNR=Intensity/Deviation
		for i in range(len(Intensity)):
			if SNR[i]<3:
				Intensity[i]=np.nan
				Rel_velocity[i]=np.nan
				Vel_dispersion[i]=np.nan
		mean_vel=np.mean(Rel_velocity)
		Rel_velocity[:]=Rel_velocity[:]-1180
		Flux_map=np.zeros((580,580),float)
		Velocity_map=np.zeros((580,580),float)
		Dispersion_map=np.zeros((580,580),float)
		x,y,bin_num=np.genfromtxt(gc.dir3, usecols=(0,1,2), unpack=True)
		for i in range(len(x)):
			Flux_map[int(x[i]-1),int(y[i]-1)]=Intensity[int(bin_num[i]-1)]
			Velocity_map[int(x[i]-1),int(y[i]-1)]=Rel_velocity[int(bin_num[i]-1)]
			Dispersion_map[int(x[i]-1),int(y[i]-1)]=Vel_dispersion[int(bin_num[i]-1)]		
		Flux_map=abs(np.transpose(Flux_map))
		Velocity_map=np.transpose(Velocity_map)
		Dispersion_map=np.transpose(Dispersion_map)
		ax=axs[k,0]
		im0=ax.imshow(Flux_map,norm=colors.LogNorm())#,vmin=0,vmax=5000)
		plt.colorbar(im0,ax=ax)
		ax=axs[k,1]
		im1=ax.imshow(Velocity_map,vmin=-250,vmax=250,cmap=cm.RdBu)
		plt.colorbar(im1,ax=ax)
		ax=axs[k,2]
		im2=ax.imshow(Dispersion_map,vmin=0,vmax=300)
		plt.colorbar(im2,ax=ax)
#plt.tight()
	plt.show()

