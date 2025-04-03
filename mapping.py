import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib import cm
from astropy.io import fits


def mapping(gc):
	N = len(gc.line)
	fig, axs = plt.subplots(N, 3)
	for k in range(N):
		Intensity, Rel_velocity, Vel_dispersion, Deviation=np.genfromtxt(gc.dir6,usecols=(5,1,2,4),unpack=True)
		SNR = Intensity / Deviation
		a = np.where(SNR < 3)[0]
		Intensity[a] = np.nan
		Rel_velocity[a] = np.nan
		Vel_dispersion[a] = np.nan
		mean_vel = np.mean(Rel_velocity)
		Rel_velocity[:] = Rel_velocity[:] - 1200 # 1200 km/s is the speed of the galaxy going away from us.
		Flux_map = np.zeros((gc.grid_size, gc.grid_size), float)
		Velocity_map = np.zeros((gc.grid_size, gc.grid_size), float)
		Dispersion_map = np.zeros((gc.grid_size,gc.grid_size), float)
		x,y,bin_num = np.genfromtxt(gc.dir3, usecols=(0,1,2), unpack=True)
		n = np.zeros(int(max(bin_num) + 1))
		for i in range(0,int(max(bin_num) + 1)):
			n[i] = np.count_nonzero(bin_num == i + 1)
		print(len(n), len(Intensity))
		for i in range(len(Intensity)):
			Intensity[i] /= n[i]
		for i in range(len(x)):
			Flux_map[int(x[i] - 1), int(y[i] - 1)] = Intensity[int(bin_num[i] - 1)]
			Velocity_map[int(x[i] - 1), int(y[i] - 1)] = Rel_velocity[int(bin_num[i] - 1)]
			Dispersion_map[int(x[i] - 1),int(y[i] - 1)] = Vel_dispersion[int(bin_num[i] - 1)]		
		Flux_map = abs(np.transpose(Flux_map))
		Velocity_map = np.transpose(Velocity_map)
		Dispersion_map = np.transpose(Dispersion_map)
		ax = axs[0]
		im0 = ax.imshow(Flux_map, vmin=0, vmax=700)#norm=colors.LogNorm())#,)vmin=1,vmax=25000,clip=True
		plt.colorbar(im0, ax=ax)
		ax = axs[1]
		im1 = ax.imshow(Velocity_map, vmin=-250, vmax=250, cmap=cm.RdBu)
		plt.colorbar(im1, ax=ax)
		ax = axs[2]
		im2 = ax.imshow(Dispersion_map, vmin=0, vmax=200)
		plt.colorbar(im2, ax=ax)
		plt.savefig(gc.dir8)
		plt.close()
#	plt.show()
#	w=np.arange(1,2243,1)
#	plt.scatter(w,Rel_velocity)
#	plt.show()
#plt.tight()


