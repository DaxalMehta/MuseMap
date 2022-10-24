import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import scipy.optimize as sopt

def line_profile(p,x):
	y=p[0]*np.exp(-0.5*((x-p[1])/p[2])**2)+p[3]#+p[4]#+sky1
	###p[0]=intensity, p[1]=velocity, p[2]=velocity dispersion, p[3]=background
	return y
def residual(p, x, y):
     wres = (line_profile(p, x)-y)
     wres
     return wres

def chi_squared(p, x, y):
     wres = residual(p, x, y)
     chi2 = np.sum(wres*wres)
     return chi2

def fitting(directory,x,spectrum_range,k):
	bins=np.genfromtxt(directory.dir4+"_"+str(directory.line[k]))
	bins=bins[:,spectrum_range]
	N=len(bins)
	p=np.zeros((N,4),float)
	pdf = PdfPages(directory.dir6+"_"+str(directory.line[k]))
	for i in range(len(bins)):
		data=bins[i]
		m=np.mean(data)
		l=int((directory.line[k]*(1+directory.redshift)-x[0])/1.25)
		mm=max(data[l-4],data[l-3],data[l-2],data[l-1],data[l],data[l+1],data[l+2],data[l+3],data[l+4])
		guess = [mm-m,directory.line[k]*(1+directory.redshift),1.,m]
		res = sopt.minimize(chi_squared, guess, args=(x,data))
		p[i,:] = res.x    # output in variabile new_p
		data_fit = line_profile(p[i,:], x)
		fig = plt.figure(figsize =(5, 4))
		plt.plot(x,data)
		plt.plot(x,data_fit)
		pdf.savefig(fig)
		plt.close()
	pdf.close()	
	np.savetxt(directory.dir5+"_"+str(directory.line[k]), np.column_stack([p]), fmt=b'%10.6f')	
	print('Fitting Done')
