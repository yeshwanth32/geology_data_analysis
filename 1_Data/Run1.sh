#! /bin/sh
##
\rm MFS1.out
\rm control
\rm MFS1.results
\rm baro.mfs2
\rm data.mfs1

## 14950 data points
## 6168 data points
# shift of 2016 is 14 days
# shift of 1008 is 7 days
# shift of  4320 is 30 days
# span of 4464 is 31 days

## lat 42 26' 56" N
## 42.4489
## long 72 40' 50" W
## 72.680555

echo "Starting the control file definition."
cat << END > control
&param
kind=7,
span=4464, shift=2016,
lpout=0, filout=1,
igrp=0,
lagp=2, lagint=1,
spectw=1,
lat=42.449, long=-72.681, ht=250.8, grav=0,
year=2017, mon=7, day=03, hr=18, min=0, sec=0,
timsys=4.0d0
ndata=14950, delta=0.16666667,
rlim=9000,
inform=3,
maxjmp=2,
dmin=0.25d0,
weight=0.25d0,
&end
                      Well Tidal Strain

----
MFS-1, Whately, MA              station name
Solinst Levelogger Junior Edge  instrument name
----
Water level in meters                    unit of tidal data
Atmospheric pressure in mbar             title of associated dataset
END

#
# run the program
# The water level and barometric pressure data files have a 1 line header
#
echo "Using Well MFS 1 from MacLeish Field Station"

# make the data file
echo "MFS-1, Whately, MA" > data.mfs1
cat ../Data/MFS1.bay >> data.mfs1

echo "Barometeric pressure, Whately, MA" > baro.mfs2
#cat ../Data/Baro_mfs2.bay >> baro.mfs2
cat ../Data/Baro.bay >> baro.mfs2

echo "Running baytap08."
cat data.mfs1 | /home/wclement/bin/baytap08 control MFS1.results baro.mfs2 > MFS1.out
#cat data.mfs1 | /home/wclement/bin/baytap08 control MFS1.results > MFS1.out

echo "Stripping off the phases."
#awk -f strip.awk < MFS1.results > MFS1.phases
#exit

awk '
{
    if($1 ~ />/ && $1 !~ />S/ && $1 !~ />R/){
        if($5 ~ /Group/){
          printf("%s %s %.7f %s %.7f \t %s %.5f %s %.5f\n",$4, "Amplitude:", $10, "+/-", $11, "Phase:", $8, "+/-", $9)
        }
        else{
          printf("%s %s %.7f %s %.7f \t %s %.5f %s %.5f\n",$4, "Amplitude:", $9, "+/-", $10, "Phase:", $7, "+/-", $8)
        }
    }
    if($1 ~ /"/){
      printf("\n%s %s %s %f\n\n","Hyperparameter", $2, "is", $4)
    }
}
' < MFS1.results > MFS1.phases

awk -f O1.awk < MFS1.phases > MFS1_phases.O1
awk -f M2.awk < MFS1.phases > MFS1_phases.M2
