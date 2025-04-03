import inputs
class dat(object):
	def __init__(self):
		self.line = inputs.line					# Lines
		self.redshift = inputs.z 					# Metallicuty
		self.grid_size = inputs.Pixel_Grid_Size
		self.bin_size = inputs.normal_binning_size 		# Size of the bins
		self.binning = inputs.binning
		self.dir1 = inputs.fil					# File where the data is present
		self.xpos = inputs.x_pos
		self.ypos = inputs.y_pos
		if self.binning == "Voronoi":
			self.snr = inputs.SNR
			self.dir = self.binning + "_" + str(self.grid_size) + "/"						# Type of binning
			self.dir2 = self.dir + str(self.line) + str(self.snr) + "_Signal_Noise.txt" 			# File where signal, noise for each bin is stored for the given line
			self.dir3 = self.dir + str(self.line) + str(self.snr) + "_Voronoi_Output.txt" 			# File where the output of binning information is stored
			self.dir4 = self.dir + str(self.line) + str(self.snr) + "_Bins.txt"				# File where spectrum of bins is stored
			self.dir5 = self.dir + str(self.line) + str(self.snr) + "_Spectrums.pdf"
			self.dir6 = self.dir + str(self.line) + str(self.snr) + "_Fitting_Output.txt"	# File where output of fitting is stored.
			self.dir7 = self.dir + str(self.line) + str(self.snr) + "_Fits.pdf"
			self.dir8 = self.dir + str(self.line) + str(self.snr) + "_Maps.pdf"
			self.white = self.dir + "White.fits"
			self.stat = self.dir + "Stat.fits"
		elif self.binning == "Normal":
			self.dir = str(self.bin_size) + "_spaxels/" 	# Directory to store the necessary files
			self.dir2 = self.dir + "Binning_Input.txt" 		# File where signal, noise for each bin is stored for the given line
			self.dir3 = self.dir + "Binning_Output.txt" 	# File where the output of binning information is stored
			self.dir4 = self.dir + str(self.line) + "_Bins.txt"			# File where spectrum of bins is stored
			self.dir5 = self.dir + str(self.line) + "_Spectrums.pdf"
			self.dir6 = self.dir + str(self.line) + "Fitting_Output.txt"		# File where output of fitting is stored.
			self.dir7 = self.dir + str(self.line) + "_Fits.pdf"			# Pdf where fitting plots are stored.
					
		self.plot = inputs.plot 					# if we want intermediate plot to check whether the code is functioning properly
		
		
