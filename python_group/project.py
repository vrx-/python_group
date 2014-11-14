#!/usr/bin/env python

from netCDF4 import Dataset
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt

PATH='sst_xyt_dy.cdf'


data=Dataset(PATH)

lat=data.variables['lat'][:]
lon=data.variables['lon'][:]
depth=data.variables['depth'][:]
time=data.variables['time'][:]

T=data.variables['T_20'] #TEMPERATURE
ST=data.variables['ST_6020'] #TEMPERATURE SOURCE
QT=data.variables['QT_5020'] #TEMPERATURE QUALITY

m = Basemap(projection='robin',
            lat_0=0,
            lon_0=-155,
            resolution='c')

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111)

m.fillcontinents()

x, y = m(*np.meshgrid(lon, lat))
m.plot(x,y,'or')

plt.show()