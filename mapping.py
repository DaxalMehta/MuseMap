import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib import cm
def mapping(directory):
	N=len(directory.line)
	fig,axs=plt.subplots(N,3)
	for l in range(N):
		Intensity,Rel_velocity,Vel_dispersion=np.genfromtxt(directory.dir5+"_"+str(directory.line[l]),usecols=(0,1,2),unpack=True)
		Rel_velocity=(Rel_velocity/directory.line[l]-1)*299793.4
		mean_vel=np.mean(Rel_velocity)
		Rel_velocity[:]=Rel_velocity[:]-1280
		Vel_dispersion=(Vel_dispersion/directory.line[l])*299793.4
		Flux_map=np.zeros((580,580),float)
		Velocity_map=np.zeros((580,580),float)
		Dispersion_map=np.zeros((580,580),float)
		x,y,bin_num=np.genfromtxt(directory.dir3, usecols=(0,1,2), unpack=True)
		for i in range(len(x)):
			Flux_map[int(x[i]-1),int(y[i]-1)]=Intensity[int(bin_num[i]-1)]
			Velocity_map[int(x[i]-1),int(y[i]-1)]=Rel_velocity[int(bin_num[i]-1)]
			Dispersion_map[int(x[i]-1),int(y[i]-1)]=Vel_dispersion[int(bin_num[i]-1)]		
		Flux_map=abs(np.transpose(Flux_map))
		Velocity_map=np.transpose(Velocity_map)
		Dispersion_map=np.transpose(Dispersion_map)
		ax=axs[l,0]
		im0=ax.imshow(Flux_map,norm=colors.LogNorm())#,vmin=0,vmax=5000)
		plt.colorbar(im0,ax=ax)
		ax=axs[l,1]
		im1=ax.imshow(Velocity_map,vmin=-250,vmax=250,cmap=cm.RdBu)
		plt.colorbar(im1,ax=ax)
		ax=axs[l,2]
		im2=ax.imshow(Dispersion_map,vmin=0,vmax=200)
		plt.colorbar(im2,ax=ax)
#plt.tight()
	plt.show()

