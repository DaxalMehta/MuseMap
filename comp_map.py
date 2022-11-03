import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib import cm
from astropy.io import fits
from matplotlib.backends.backend_pdf import PdfPages

fig,axs=plt.subplots(3,1)
#for k in range(N):
Intensity1,Rel_velocity1,Vel_dispersion1,Deviation1=np.genfromtxt('/home/daxal_mehta/Downloads/Akshay_Project/NGC1366/Voronoi5/[6564.6]10_Fitting_Output.txt_6564.6',usecols=(5,1,2,4),unpack=True)
Intensity2,Rel_velocity2,Vel_dispersion2,Deviation2=np.genfromtxt('/home/daxal_mehta/Downloads/Akshay_Project/NGC1366/Voronoi6/[6564.6]10_Fitting_Output.txt_6564.6',usecols=(5,1,2,4),unpack=True)
#		for i in range(len(Intensity)):
#			if Rel_velocity[i]>1500:
#				Rel_velocity[i]=1180
#			if Intensity[i]>50000:
#				Intensity[i]=50000
SNR1=Intensity1/Deviation1
SNR2=Intensity2/Deviation2
for i in range(len(Intensity1)):
	if SNR1[i]<3:
		Intensity1[i]=np.nan
		Rel_velocity1[i]=np.nan
		Vel_dispersion1[i]=np.nan
for i in range(len(Intensity2)):
	if SNR2[i]<3:
		Intensity2[i]=np.nan
		Rel_velocity2[i]=np.nan
		Vel_dispersion2[i]=np.nan
#mean_vel=np.mean(Rel_velocity)
Rel_velocity1[:]=Rel_velocity1[:]-1180
Rel_velocity2[:]=Rel_velocity2[:]-1180
Flux_map1=np.zeros((200,200),float)
Velocity_map1=np.zeros((200,200),float)
Dispersion_map1=np.zeros((200,200),float)
Flux_map2=np.zeros((200,200),float)
Velocity_map2=np.zeros((200,200),float)
Dispersion_map2=np.zeros((200,200),float)
F_map=np.zeros((400,200),float)
V_map=np.zeros((400,200),float)
D_map=np.zeros((400,200),float)
x1,y1,bin_num1=np.genfromtxt('/home/daxal_mehta/Downloads/Akshay_Project/NGC1366/Voronoi5/10_Voronoi_Output.txt', usecols=(0,1,2), unpack=True)
x2,y2,bin_num2=np.genfromtxt('/home/daxal_mehta/Downloads/Akshay_Project/NGC1366/Voronoi6/10_Voronoi_Output.txt', usecols=(0,1,2), unpack=True)
n1=np.zeros(int(max(bin_num1)+1))
n2=np.zeros(int(max(bin_num2)+1))
for i in range(0,int(max(bin_num1)+1)):
	n1[i]=np.count_nonzero(bin_num1==i+1)
for i in range(0,int(max(bin_num2)+1)):
	n2[i]=np.count_nonzero(bin_num2==i+1)
#print(len(n),len(Intensity))
for i in range(len(Intensity1)):
	Intensity1[i]/=n1[i]
for i in range(len(Intensity2)):
	Intensity2[i]/=n2[i]
for i in range(len(x1)):
	Flux_map1[int(x1[i]-1),int(y1[i]-1)]=Intensity1[int(bin_num1[i]-1)]
	Velocity_map1[int(x1[i]-1),int(y1[i]-1)]=Rel_velocity1[int(bin_num1[i]-1)]
	Dispersion_map1[int(x1[i]-1),int(y1[i]-1)]=Vel_dispersion1[int(bin_num1[i]-1)]
for i in range(len(x2)):
	Flux_map2[int(x2[i]-1),int(y2[i]-1)]=Intensity2[int(bin_num2[i]-1)]
	Velocity_map2[int(x2[i]-1),int(y2[i]-1)]=Rel_velocity2[int(bin_num2[i]-1)]
	Dispersion_map2[int(x2[i]-1),int(y2[i]-1)]=Vel_dispersion2[int(bin_num2[i]-1)]		

F_map[:200,:]=Flux_map2
F_map[200:400,:]=Flux_map1
V_map[:200,:]=Velocity_map2
V_map[200:400,:]=Velocity_map1
D_map[:200,:]=Dispersion_map2
D_map[200:400,:]=Dispersion_map1
F_map=abs(np.transpose(F_map))
V_map=np.transpose(V_map)
D_map=np.transpose(D_map)
ax=axs[0]
im0=ax.imshow(F_map,norm=colors.LogNorm())#,)vmin=1,vmax=25000,clip=True
plt.colorbar(im0,ax=ax)
ax=axs[1]
im1=ax.imshow(V_map,vmin=-250,vmax=250,cmap=cm.RdBu)
plt.colorbar(im1,ax=ax)
ax=axs[2]
im2=ax.imshow(D_map,vmin=0,vmax=250)
plt.colorbar(im2,ax=ax)
#	pdf.savefig(fig)
#	plt.close()
#	pdf.close()
#	hdu=fits.PrimaryHDU(data=Flux_map)
#	hdu.writeto('Flux.fits',overwrite=True)
plt.show()
#	w=np.arange(1,2243,1)
#	plt.scatter(w,Rel_velocity)
#	plt.show()
#plt.tight()


