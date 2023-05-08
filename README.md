# Hart_Kronauer2023
Processing code for calcium imaging data from "Sparse and stereotyped encoding implicates a core glomerulus for ant alarm behavior".

Raw data with .nwb files can be found at https://dandiarchive.org/dandiset/000467

To re-analyze data, first download the archived data at the above link. Next, run the python script "generate_tif_files.py" on the downloaded archive to convert .nwb files to .tif files. Finally, install and run the ImageJ macro script "macro_calcium_imaging.txt". In each case you will need to enter the directory containing the source data into the scripts before running..
