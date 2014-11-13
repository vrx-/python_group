from netCDF4 import Dataset

PATH='/Users/vrx/Desktop/sst_xyt_dy.cdf'
data=Dataset(PATH)

lat=data.variables['lat'][:]
lon=data.variables['lon'][:]
depth=data.variables['depth'][:]
time=data.variables['time'][:]

T=data.variables['T_20'] #TEMPERATURE
ST=data.variables['ST_6020'] #TEMPERATURE SOURCE
QT=data.variables['QT_5020'] #TEMPERATURE QUALITY