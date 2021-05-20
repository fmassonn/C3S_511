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

# 1. Data availability
# --------------------

countData = np.full((len(hemis), len(years), len(months)), np.nan)
numberMissing = list()
# Data count
for j_hemi, hemi in enumerate(hemis):
  for j_month, month in enumerate(months):
    for j_year, year in enumerate(years):
      myLength = len(glob.glob(root + "ESACCI-SEAICE-L4-SICONC-AMSR_25.0kmEASE2-" + hemi + "-" + str(year) + str(month).zfill(2) + "??-fv2.1.nc"))
      #print(str(year) + "-" + str(month).zfill(2) + ": " + str(myLength))

      # Store information
      countData[j_hemi, j_year, j_month] = myLength

      # How many days missing?
      numberMissing.append(monthrange(year, month)[1] - myLength)
      
# Graphs

# Spatial coverage
fig, ax = plt.subplots(1, 2, figsize=(8, 4), dpi = 300)

sampleFile = root + "ESACCI-SEAICE-L4-SICONC-AMSR_25.0kmEASE2-NH-20050101-fv2.1.nc"
f = Dataset(sampleFile, mode = "r")
lon = f.variables["lon"][:]
lat = f.variables["lat"][:]
f.close()

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
fig.savefig("fig3.png")
stop()


# Histogram

fig, ax = plt.subplots(1, 1, dpi = 300, figsize = (5, 3))
ax.hist(numberMissing, bins = np.arange(0.5, 9.5), lw = 0, color = "black", alpha = 0.5, rwidth = 0.95)
ax.yaxis.grid()
ax.set_axisbelow(True)
ax.set_xlabel("$x$ days of data missing")
ax.set_ylabel("Number of months")
ax.set_title("Distribution of number of days missing")
ax.set_xticks(np.arange(1, 10))
fig.tight_layout()

fig.savefig("./fig2.png")
stop()

# Time series

fig, ax = plt.subplots(1, 1, dpi = 300, figsize = (9, 2))

for j_hemi, hemi in enumerate(hemis):
  sign =  (- 1) ** j_hemi
  for j_month, month in enumerate(months):
    for j_year, year in enumerate(years):

      if year == 2007 and hemi == "NH":
         leg = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"][j_month]
      else:
         leg = None
      ax.bar(year + j_month / 14, sign * countData[j_hemi, j_year, j_month], \
               color = colmonths[j_month], alpha = 0.9, width = 1 / 15, label = leg)

      

ax.legend(loc = "upper center", bbox_to_anchor = (0.5, 1.2), ncol = 12, fontsize = 6)
ax.set_title("Number of daily observations available per month\n")
ax.set_yticks([-30, -20, -10, 10, 20, 30])
ax.set_yticklabels(["30", "20", "10", "10", "20", "30"])

for year in np.arange(2002, 2017 + 1):
  ax.text(year + 6 / 14, -40, str(year), ha = "center", fontsize = 8)

ax.set_xticklabels("")
ax.set_xticks([])
ax.grid()
ax.set_axisbelow(True)
ax.set_ylabel("(SH)   Count   (NH)")
ax.plot((0, 1e9), (0, 0), "k-", lw = 1)
ax.set_xlim(2002, 2018)
fig.tight_layout()
fig.savefig("./fig1.png")




