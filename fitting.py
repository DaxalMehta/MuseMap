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

def fitting(gc,x,spectrum_range,k):
	bins=np.genfromtxt(gc.dir4)
#	bins=bins[:,spectrum_range]
	N=len(bins)
	p=np.zeros((N,6),float)
	pdf = PdfPages(gc.dir7)
	for i in range(len(bins)):
		data=bins[i]
		m=np.mean(data)
		l=int((gc.line[k]*(1+gc.redshift)-x[0])/1.25)
		mm=max(data[l-4],data[l-3],data[l-2],data[l-1],data[l],data[l+1],data[l+2],data[l+3],data[l+4])
		guess = [mm-m,gc.line[k]*(1+gc.redshift),2.,m]
		res = sopt.minimize(chi_squared, guess, args=(x,data))
		p[i,:4] = res.x    # output in variabile new_p
		data_fit = line_profile(p[i,:], x)
		p[i,1]=(p[i,1]/gc.line[k]-1)*299793.4
		p[i,2]=abs(p[i,2])
		p[i,5]=(p[i,0]*p[i,2]*2.5)
		p[i,2]=p[i,2]/gc.line[k]*299793.4
		n1=data[:l-4]
		n2=data[l+4:]
		noise=np.concatenate((n1,n2))
		p[i,4]=np.std(noise)
		fig = plt.figure(figsize =(5, 4))
		plt.plot(x,data)
		plt.plot(x,data_fit)
		pdf.savefig(fig)
		plt.close()
	pdf.close()	
	np.savetxt(gc.dir6, np.column_stack([p]), fmt=b'%10.6f')	
	print(str(gc.line[k])+'_Fitting Done')
