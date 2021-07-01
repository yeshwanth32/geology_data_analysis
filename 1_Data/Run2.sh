#! /bin/sh
##
\rm MFS2.out
\rm control
\rm MFS2.results
\rm baro.mfs2
\rm data.mfs2

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
year=2017, mon=7, day=03, hr=18, min=00, sec=0,
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
MFS-2, Whately, MA              station name
Solinst Levelogger Junior Edge  instrument name
----
Water level in meters                    unit of tidal data
Atmospheric pressure in mbar             title of associated dataset
END

echo "Now to run the program."

#
# run the program
# The water level and barometric pressure data files have a 1 line header
#
echo "Using Well MFS 2 from MacLeish Field Station"

# make the data file
echo "MFS-2, Whately, MA" > data.mfs2
cat ../Data/MFS2.bay >> data.mfs2
#cat ../Data/MFS2_temp.bay >> data.mfs2


echo "Barometeric pressure, Whately, MA" > baro.mfs2
## Baro_mfs2.bay has only 6168 samples
#cat ../Data/Baro_mfs2.bay >> baro.mfs2
## Baro.bay has 14950 samples
cat ../Data/Baro.bay >> baro.mfs2

cat data.mfs2 | /home/wclement/bin/baytap08 control MFS2.results baro.mfs2 > MFS2.out
#cat data.mfs2 | /home/wclement/bin/baytap08 control MFS2.results > MFS2.out

#echo "Running awk script"
#awk -f strip.awk < MFS2.results > MFS2.phases

echo "Stripping off the phases."
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
' < MFS2.results > MFS2.phases

awk -f O1.awk < MFS2.phases > MFS2_phases.O1
awk -f M2.awk < MFS2.phases > MFS2_phases.M2

