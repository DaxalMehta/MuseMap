import inputs
class dat(object):
	def __init__(self):
		self.line=inputs.line
		self.bin_size=inputs.normal_binning_size #Size of the bins
		self.dir=str(self.bin_size)+"_spaxels/"
		self.dir1=inputs.fil #directory where the data is present
		self.dir2=self.dir+inputs.bin_input # directory where signal, noise for each bin is stored for the given line
		self.dir3=self.dir+inputs.bin_output # directory where the output of binning information is stored
		self.dir4=self.dir+inputs.bins#+"_"+str(self.line) # directory where spectrum of bins is stored
		self.redshift=inputs.z
		self.dir5=self.dir+inputs.fit_out#+"_"+str(self.line) #directory where output of fitting is stored.
		self.dir6=self.dir+inputs.fit_pdf#+"_"+str(self.line) # Pdf where fitting plots are stored.
#		self.signal=inputs.signal_range # the range where emission line is present
		self.vor=inputs.vor	#to see what type of binning we are doing
		self.plot=inputs.plot # to see whether we want to plot intermediate plot to check whether the code is functioning properly
#		self.spectrum_range=inputs.spectrum_range # the range where fitting is to be done
		
