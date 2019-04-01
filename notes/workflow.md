Date: Fri, 16 Jun 2017 14:24:42 -0500
From: Raymond Arritt
To: Taleena Sines 
Subject: notes on Taleena's workflow

Hi Taleena,

Daryl and I are attempting to reconstruct your analysis workflow in 
order to get an idea of how to restructure your data for easier use.  
Here are the basic steps as I have been able to figure them out, with a 
couple of questions:

(1)  After running WRF, use the wrfncxnj.py  script to extract a subset 
of variables from the raw WRF output and write to a format that is CF 
compliant (or close to it).  This script is from 
http://www.meteo.unican.es/wiki/cordexwrf/SoftwareTools/WrfncXnj

** Question:  How did you execute wrfncxnj.py -- from the command line, 
or from a script?  There are lots of individual WRF output files so I 
have assumed you used a script instead of typing file names, but maybe not.

** Question:  It looks like the raw WRF output is written at hourly 
intervals. Is this the case?  If so, it opens up some very interesting 
possibilities for analysis.

(2)  Use 'cdo mergetime' to concatenate the individual files produced by 
step (1).

(3)  Use 'cdo daymean' to generate daily means from the file produced by 
step (2).

(4)  Use a script to generate binned precipitation intensity from the 
daily mean file produced by step (3). There is a disk labeled "Cf 1979 
Era 1940" that contains a number of scripts that could be used for 
this.  These are 'Intensity_Bins_1940.nc', 'Intensity_Bins_y2.ncl', 
'Intensity_Bins_latlon.ncl', 'Intensity_Bins_latlon2.ncl', 
'Intensity_Bins.ncl', 'IB.ncl' and 'IB_TIME.ncl'.  Do you recall which 
one of these you actually used? I've attached a tar file of these in 
case you don't have them.

So, does this seem accurate?  Is there anything that I've overlooked?  
Any comments, suggestions etc. would be very welcome!

Ray



In directory ~/ERA_1940_CF/CFs there are netCDF files containing prc, 
prls, tas and hufs.

Running 'ncdump -h' on one of these shows
history  = "Created by wrfncxnj.py on Tue Jun  7 11:50:17 2016".

The wrfncxnj.py  script is "WRF NetCDF Extract&Join".  It converts WRF 
output files to variables following CF conventions. See 
http://www.meteo.unican.es/wiki/cordexwrf/SoftwareTools/WrfncXnj
See disk labeled "CF TRS Fluxes"  ~/ WRF_to_CP_Package for  wrfncxnj

In directory ~/ERA_1940_CF see NCL script 'IB_TIME.ncl'.
This operates on './ERA_1940_daymean.nc' and puts amounts into bins
'Intensity_Bins.ncl' is essentially similar, but also computes hour, 
minute, second

ncdump of  './ERA_1940_daymean.nc'
Contains prc, prls, tas and hufs
Times are 24 hr apart
      :history = "Fri Jul 01 12:47:04 2016: cdo daymean ERA_1940.nc 
ERA_1940_daymean.nc\n",
                         "Sun Jun 12 14:26:21 2016: cdo mergetime 
ERA1940_CF_1.ncl ERA1940_CF_2.ncl ERA1940_CF_3.ncl ERA1940_CF_4.ncl 
ERA1940_CF_5.nc ERA1940_CF.ncl ERA_1940.nc\n",
                         "Created by wrfncxnj.py on Mon Jun  6 15:53:10 
2016" ;

ncdump of 'ERA_1940.nc'
                :history = "Sun Jun 12 14:26:21 2016: cdo mergetime 
ERA1940_CF_1.ncl ERA1940_CF_2.ncl ERA1940_CF_3.ncl ERA1940_CF_4.ncl 
ERA1940_CF_5.nc ERA1940_CF.ncl ERA_1940.nc\n",
                         "Created by wrfncxnj.py on Mon Jun  6 15:53:10 
2016" ;


