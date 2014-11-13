import numpy as np
import netCDF4
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

m = Basemap(projection='robin',
            llcrnrlon=120,
            urcrnrlon=-70, 
            llcrnrlat=-15, 
            urcrnrlat=15,
            lat_0=0,
            lon_0=-155,
            resolution='c')

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111)

m.fillcontinents()
plt.show()