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
fig, ax = plt.subplots(2, 2, figsize=(8, 8), dpi = 50)

# NH March
thisAx = ax[0, 0]
f = Dataset("./data/NH-03.nc" , mode = "r")
lon = f.variables["lon"][:]
lat = f.variables["lat"][:]
sic = f.variables["ice_conc"][0, :, :]
f.close()
m = Basemap(projection='npstere',boundinglat=60,lon_0=0,resolution='l') # for North
mapped = m.pcolormesh(lon, lat, sic,
             latlon=True, cmap='Blues_r', ax = thisAx, vmin = 0, vmax = 100)
thisAx.set_title("March, NH")
m.drawcoastlines(color='lightgray', linewidth=0.7, ax = thisAx)
m.fillcontinents(color='gray', ax = thisAx)
m.drawparallels(np.arange(-80.,81.,20.), labels=[1,0,0,0], ax = thisAx )
m.drawmeridians(np.arange(-180.,181.,20.), labels=[1,0,0,0], ax = thisAx)

# NH September
thisAx = ax[0, 1]
f = Dataset("./data/NH-09.nc" , mode = "r")
lon = f.variables["lon"][:]
lat = f.variables["lat"][:]
sic = f.variables["ice_conc"][0, :, :]
f.close()
m = Basemap(projection='npstere',boundinglat=60,lon_0=0,resolution='l') # for North
mapped = m.pcolormesh(lon, lat, sic,
             latlon=True, cmap='Blues_r', ax = thisAx, vmin = 0, vmax = 100)
thisAx.set_title("September, NH")
m.drawcoastlines(color='lightgray', linewidth=0.7, ax = thisAx)
m.fillcontinents(color='gray', ax = thisAx)
m.drawparallels(np.arange(-80.,81.,20.), labels=[1,0,0,0], ax = thisAx )
m.drawmeridians(np.arange(-180.,181.,20.), labels=[1,0,0,0], ax = thisAx)

# SH March
thisAx = ax[1, 0]
f = Dataset("./data/SH-02.nc" , mode = "r")
lon = f.variables["lon"][:]
lat = f.variables["lat"][:]
sic = f.variables["ice_conc"][0, :, :]
f.close()
m = Basemap(projection='spstere',boundinglat=-50,lon_0=180,resolution='l') # for South
mapped = m.pcolormesh(lon, lat, sic,
             latlon=True, cmap='Blues_r', ax = thisAx, vmin = 0, vmax = 100)
thisAx.set_title("February, SH")
m.drawcoastlines(color='lightgray', linewidth=0.7, ax = thisAx)
m.fillcontinents(color='gray', ax = thisAx)
m.drawparallels(np.arange(-80.,81.,20.), labels=[1,0,0,0], ax = thisAx )
m.drawmeridians(np.arange(-180.,181.,20.), labels=[1,0,0,0], ax = thisAx)

# SH September
thisAx = ax[1, 1]
f = Dataset("./data/SH-09.nc" , mode = "r")
lon = f.variables["lon"][:]
lat = f.variables["lat"][:]
sic = f.variables["ice_conc"][0, :, :]
f.close()
m = Basemap(projection='spstere',boundinglat=-50,lon_0=180,resolution='l') # for South
mapped = m.pcolormesh(lon, lat, sic,
             latlon=True, cmap='Blues_r', ax = thisAx, vmin = 0, vmax = 100)
thisAx.set_title("September, SH")
m.drawcoastlines(color='lightgray', linewidth=0.7, ax = thisAx)
m.fillcontinents(color='gray', ax = thisAx)
m.drawparallels(np.arange(-80.,81.,20.), labels=[1,0,0,0], ax = thisAx )
m.drawmeridians(np.arange(-180.,181.,20.), labels=[1,0,0,0], ax = thisAx)


fig.colorbar(mapped, orientation='horizontal', label='% (Fraction)', ax = ax.ravel().tolist(), pad = 0.8)

fig.savefig("fig4.png")



