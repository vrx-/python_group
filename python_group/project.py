#!/usr/bin/env python
#plt.ion()

from netCDF4 import Dataset
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt

PATH='sst_xyt_dy.cdf'


data=Dataset(PATH)

lat=data.variables['lat'][:] #degrees_north
lon=data.variables['lon'][:] #degrees_east
time=data.variables['time'][:] # Centered Time

T=data.variables['T_20'][:,0,:,:] #TEMPERATURE degree_C
ST=data.variables['ST_6020'][:,0,:,:] #TEMPERATURE SOURCE
QT=data.variables['QT_5020'][:,0,:,:] #TEMPERATURE QUALITY 


'''
QT (Quality Codes): 
0=missing data
1=highest
2=standard
3=lower
4=questionable
5=bad

ST (Source Codes):
0 = No Sensor, No Data
1 = Real Time (Telemetered Mode) *
2 = Derived from Real Time *
3 = Temporally Interpolated from Real Time
4 = Source Code Inactive at Present
5 = Recovered from Instrument RAM (Delayed Mode) *
6 = Derived from RAM *
7 = Temporally Interpolated from RAM
'''

#only "good data"
tq=np.ma.masked_where(QT>3, T)
tq=np.ma.masked_where(QT==0, tq)

m = Basemap(projection='robin',
            lat_0=0,
            lon_0=-155,
            resolution='c')

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111)

m.fillcontinents()

colors = np.array(['#ffffff','#00cc00','#99ff66','#ffff00','#ff9933','#ff0000'])
x, y = m(*np.meshgrid(lon, lat))
plt.scatter(x,y,c=colors[QT[0,:,:]])
plt.show()

#indx=np.asarray(np.where((QT>0)&(QT<3)))

