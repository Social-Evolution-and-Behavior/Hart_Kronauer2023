import tifffile as tiff
import os
from pynwb import NWBHDF5IO


# this script re-writes .nwb files as .tif files, for analysis in ImageJ. 
# source data: https://dandiarchive.org/dandiset/000467
# written by Taylor Hart


indir_path = "/Volumes/My Passport/test_output1/"
outdir_path = "/Volumes/My Passport/test_reconstituted_tifs/"

if not os.path.exists(outdir_path):
        os.mkdir(outdir_path)

for daydir in os.listdir(indir_path):
        if not os.path.exists(outdir_path+daydir+'/'):
                os.mkdir(outdir_path+daydir+'/')
        print("daydir "+daydir)
        for antdir in os.listdir(indir_path+daydir):
                if not os.path.exists(outdir_path+daydir+'/'+antdir+'/'):
                        os.mkdir(outdir_path+daydir+'/'+antdir+'/')


                print("antdir "+antdir)
                for trialdir in os.listdir(indir_path+daydir+'/'+antdir+'/'):
                        if not os.path.exists(outdir_path+daydir+'/'+antdir+'/'+trialdir):
                                os.mkdir(outdir_path+daydir+'/'+antdir+'/'+trialdir+'/')

                        files = os.listdir(indir_path+daydir+'/'+antdir+'/'+trialdir+'/')
                        
                        for file in files:
                                if file.endswith(".nwb"):
                                        nwb_file = file
                                        out_file_final = nwb_file.split("/")
                                        out_file_path2 = out_file_final[-1].split(".")
                                        outfile_path = out_file_path2[0]+'-'+out_file_path2[1] + '.tif'
                                        io = NWBHDF5IO(indir_path+daydir+'/'+antdir+'/'+trialdir+'/'+nwb_file, 'r')
                                        nwb_data = io.read()
                                        image_series_key = 'TwoPhotonSeries1'
                                        image_series = nwb_data.acquisition[image_series_key]
                                        image_data = image_series.data
                                        timestamps = image_series.timestamps
                                        output_path = outdir_path+daydir+'/'+antdir+'/'+trialdir+'/'+outfile_path  
                                        if not os.path.exists(output_path):
                                                tiff.imwrite(output_path, image_data)
