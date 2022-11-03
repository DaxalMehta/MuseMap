import numpy as np

def spectral_range(gc,header):
	x1=round((gc.line[0]-150)/100)*100
	x2=round((gc.line[0]+150)/100)*100
	if x1<header[33]:
		x1=header[33]
	diffx=x2-x1
	x=x=np.linspace(x1,x2,int(diffx/1.25))
	return x1,x2,x
def slice_range(gc,header):
	x1,x2,x=spectral_range(gc,header)
	b1=int((x1-header[33])/1.25)
	b2=int((x2-header[33])/1.25)
	slices=np.arange(b1,b2,1)
	return b1,b2,slices
