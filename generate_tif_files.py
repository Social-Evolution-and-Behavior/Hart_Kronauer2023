import tifffile as tiff
import os
from pynwb import NWBHDF5IO


# this script reads .nwb files and writes corresponding new .tif files, for analysis in ImageJ. 
# source data: https://dandiarchive.org/dandiset/000467
# written by Taylor Hart
# specify the input and output directories below:


indir_path = "/Volumes/My Passport/test_download/000467/"
outdir_path = "/Volumes/My Passport/test_convert/"

if not os.path.exists(outdir_path):
	os.mkdir(outdir_path)

for antnum in os.listdir(indir_path):


	if not os.path.isdir(indir_path+antnum+'/'):
		continue
	files = os.listdir(indir_path+antnum+'/')

	for file in files:
		if file.endswith(".nwb"):
			file_items  = file.split('-')
				
			date = file_items[2]+'-'+file_items[3]+'-'+file_items[4]
			ant_id = file_items[5]
			z_plane1 = file_items[-1]
			z_plane = z_plane1.split('_')[0]
			trial_id = file_items[-2]
			new_file_name = file.split('.')[0]+'.tif'

			if not (trial_id == "t288" or trial_id == "t293" or trial_id == "t284" or trial_id == "t290"):
				continue


			trial_name = "trial"

			for item in file_items[6:-1]:
				trial_name = trial_name+"-"+item
			
			
			io = NWBHDF5IO(indir_path+antnum+'/'+file, 'r')
			nwb_data = io.read()
			image_series_key = 'TwoPhotonSeries1'
			image_series = nwb_data.acquisition[image_series_key]
			image_data = image_series.data
                                
			if not os.path.exists(outdir_path+'/'+date+'/'):
				os.mkdir(outdir_path+'/'+date+'/')
			if not os.path.exists(outdir_path+'/'+date+'/'+ant_id+'/'):
				os.mkdir(outdir_path+'/'+date+'/'+ant_id+'/')
			if not os.path.exists(outdir_path+'/'+date+'/'+ant_id+'/'+trial_name+'/'):
				os.mkdir(outdir_path+'/'+date+'/'+ant_id+'/'+trial_name+'/')			

			output_path = outdir_path+'/'+date+'/'+ant_id+'/'+trial_name+'/'+new_file_name 
			if not os.path.exists(output_path):
				tiff.imwrite(output_path, image_data)
