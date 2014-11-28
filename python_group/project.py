#!/usr/bin/env python
#plt.ion()

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


from netCDF4 import Dataset
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# load the data
PATH='sst_xyt_dy.cdf'

data=Dataset(PATH)

#define dimensions
lat=data.variables['lat'][:] #degrees_north
lon=data.variables['lon'][:] #degrees_east
time=data.variables['time'][:] # Centered Time

TIME = [datetime(1979,1,20,12,0,0)+int(i)*timedelta(days=1) for i in time]

#define variables
T=data.variables['T_20'][:,0,:,:] #TEMPERATURE degree_C
ST=data.variables['ST_6020'][:,0,:,:] #TEMPERATURE SOURCE
QT=data.variables['QT_5020'][:,0,:,:] #TEMPERATURE QUALITY 

#only "good data"
tq=np.ma.masked_where(QT==0, np.ma.masked_where(QT>2, T))

#how many
points=np.zeros(len(time))
for t in range(len(time)):
    points[t]=sum(sum(~tq.mask[t,:,:]))
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111)
plt.plot(TIME,points)

#map
m = Basemap(projection='robin',
            lat_0=0,
            lon_0=-155,
            resolution='c')

fig2 = plt.figure(figsize=(10, 7))
ax2 = fig2.add_subplot(111)

m.fillcontinents()


'''
colors = np.array(['#ffffff','#00cc00','#99ff66','#ffff00','#ff9933','#ff0000'])
x, y = m(*np.meshgrid(lon, lat))
plt.scatter(x,y,c=colors[QT[0,:,:]])
plt.show()
'''


