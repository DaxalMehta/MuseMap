import inputs
class dat(object):
	def __init__(self):
		self.line=inputs.line				# Lines
		self.redshift=inputs.z 				# Metallicuty
		self.bin_size=inputs.normal_binning_size 	# Size of the bins
		self.dir=str(self.bin_size)+"_spaxels/" 	# Directory to store the necessary files
		self.dir1=inputs.fil 				# File where the data is present
		self.dir2=self.dir+"bin_inp.txt" 		# File where signal, noise for each bin is stored for the given line
		self.dir3=self.dir+"bin_out.txt" 		# File where the output of binning information is stored
		self.dir4=self.dir+"bins.txt"			# File where spectrum of bins is stored
		self.dir5=self.dir+"fitting_output.txt"	# File where output of fitting is stored.
		self.dir6=self.dir+"fits.pdf"			# Pdf where fitting plots are stored.
		self.binning=inputs.binning			# Type of binning
		self.plot=inputs.plot 				# if we want intermediate plot to check whether the code is functioning properly

		
#bin_input="bin_inp.txt"
#bin_output="bin_out.txt"
#bins="bins.txt"
#fit_out="fitting_output"
#fit_pdf="fits.pdf"

