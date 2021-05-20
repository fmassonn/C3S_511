# AUTHOR      F. Massonnet
# DATE        18 May 2021


import numpy as np
import glob
import matplotlib.pyplot as plt
from   calendar import monthrange
from mpl_toolkits.basemap import Basemap
from netCDF4 import Dataset


plt.close("all")
hemis = ["NH", "SH"]
years = np.arange(2002, 2021 + 1)
months = np.arange(1, 12 + 1)

root = "/storepelican/CLIMDATA/obs/ice/siconc/ESACCI/AMSR/raw/"

colmonths = ["#1898e0", "#00b2ed", "#00bb62", \
             "#8bcd45", "#dbe622", "#f9c410", \
             "#f89e13", "#fb4c27", "#fb4865", \
             "#d24493", "#8f57bf", "#645ccc",]

colmonths = ["#664a97", "#4b69c8", "#27c5ef", \
             "#207567", "#358873", "#4E9C81", \
             "#FF4E50", "#FC913A", "#F9D62E"   , \
             "#3A1105", "#832E04", "#C46A08",]
alphas    = [1, 0.7, 0.5, 
             1, 0.7, 0.5,
             1, 0.7, 0.5,
             1, 0.7, 0.5]

# Graphs

# Spatial coverage
fig, ax = plt.subplots(2, 2, figsize=(8, 8), dpi = 300)

filein = ""
f = Dataset("./data/NH-03.nc" , mode = "r")
lon = f.variables["lon"][:]
lat = f.variables["lat"][:]
sic = f.variables["ice_conc"][:]
f.close()
stop()
m = Basemap(projection='npstere',boundinglat=30,lon_0=0,resolution='l') # for North
m.drawcoastlines(color='lightgray', linewidth=0.7, ax = ax[0])
#m.fillcontinents(color='gray', ax = ax[0])
m.pcolormesh(lon, lat, np.ones(lon.shape), ax = ax[0], latlon = True)

m.drawparallels(np.arange(-80.,81.,20.), labels=[1,0,0,0], ax = ax[0] )
m.drawmeridians(np.arange(-180.,181.,20.), labels=[1,0,0,0], ax = ax[0])

# Repeat with SH
sampleFile = root + "ESACCI-SEAICE-L4-SICONC-AMSR_25.0kmEASE2-SH-20050101-fv2.1.nc"
f = Dataset(sampleFile, mode = "r")
lon = f.variables["lon"][:]
lat = f.variables["lat"][:]
f.close()

m = Basemap(projection='spstere',boundinglat=-30,lon_0=180,resolution='l')
m.drawcoastlines(color='lightgray', linewidth=0.7, ax = ax[1])
#m.fillcontinents(color='gray', ax = ax[1])
m.pcolormesh(lon, lat, np.ones(lon.shape), ax = ax[1], latlon = True)

m.drawparallels(np.arange(-80.,81.,20.), labels=[1,0,0,0], ax = ax[1] )
m.drawmeridians(np.arange(-180.,181.,20.), labels=[1,0,0,0], ax = ax[1])


fig.tight_layout()
fig.savefig("fig4.png")

