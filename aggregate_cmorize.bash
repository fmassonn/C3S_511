#!/bin/bash
set -x
# F. Massonnet 
# May 2021

# Aggregates ESA CCI AMSR data from daily to monthly
rootdir=/storepelican/CLIMDATA/obs/ice/siconc/ESACCI/AMSR/raw/
#for hemi in NH SH
#do
#  for year in `seq 2002 2017`
#  do
#    echo $year
#    for month in `seq 1 12`
#    do
#      mm=$(printf "%02d" $month)
#      nfiles=`ls ${rootdir}/ESACCI-SEAICE-L4-SICONC-AMSR_25.0kmEASE2-${hemi}-${year}${mm}??-fv2.1.nc | wc -l`
#      if [ $nfiles -ge 20 ]
#      then
#        ncra ${rootdir}/ESACCI-SEAICE-L4-SICONC-AMSR_25.0kmEASE2-${hemi}-${year}${mm}??-fv2.1.nc ./data/${hemi}-${year}${mm}.nc
#      fi
#    done
#  done
#done

# Merge time
for hemi in NH SH
do
  for month in `seq 1 12`
  do
    echo $mon
    mm=$(printf "%02d" $month)
    cdo mergetime ./data/${hemi}-????${mm}.nc ./data/${hemi}-${mm}.nc
  done
done
# Monthly stats
for hemi in NH SH
do
  for month in `seq 1 12`
  do
    echo $mon
    mm=$(printf "%02d" $month)
    cdo timmean ./data/${hemi}-${mm}.nc ./data/${hemi}-${mm}_mean.nc
    cdo timstd  ./data/${hemi}-${mm}.nc ./data/${hemi}-${mm}_std.nc
    cdo trend   ./data/${hemi}-${mm}.nc ./data/${hemi}-${mm}_trend.nc
  done
done
