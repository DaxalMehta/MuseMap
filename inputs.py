import numpy as np
#####Data dir####
fil="NGC1366.fits"
x_pos=295
y_pos=295

####Line####
line=[5006.843] #Halpha=6562.801, OIII=5006.843 NII=6583.45 Hbeta=4861.363
z=0.003949

###Binning type###
binning="Voronoi" 		#Type of binning
SNR=20
normal_binning_size=10		#length of one square bin
Pixel_Grid_Size=200 		#200 when Voronoi binning because of limited computation power.
###plots###
plot=True
