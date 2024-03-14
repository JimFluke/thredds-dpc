import os
from pydap.client import open_url

url = f'http://{os.environ["OPENDAP_SERVER"]}:{os.environ["OPENDAP_PORT"]}'
url = f'{url}/thredds/dodsC/cloudsat-data/2B-GEOPROF.P1_R05/2008/366/2008366031107_14239_CS_2B-GEOPROF_GRANULE_P1_R05_E02_F00.hdf'
print(f'url: {url}\n')
dataset = open_url(url)

#print(dataset)
print(f'dataset.name: {dataset.name}')
print(f'dataset.keys: {list(dataset.keys())}')

UTC_start = dataset['/2B-GEOPROF/Geolocation_Fields/UTC_start'][:]

print(f'UTC_start: {UTC_start}')
print(f'UTC_start.name: {UTC_start.name}')
print(f'UTC_start.data: {UTC_start.data}')

field = '/2B-GEOPROF/Geolocation_Fields/Profile_time'
Profile_time = dataset[field][:]
print('Profile_time[:37]:', Profile_time.data[:37])

field = '/2B-GEOPROF/Data_Fields/MODIS_cloud_flag'
MODIS_cloud_flag = dataset[field][:].data
print('MODIS_cloud_flag[:37]:', MODIS_cloud_flag[:37])
