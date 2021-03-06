import sys
import os
from osgeo import gdal
import json

INPUT_FOLDER = 'input'

kwargs = {
    'allMetadata':True,
    'format':'json',
}

for subdir, dirs, files in os.walk(INPUT_FOLDER):
    for file in files:
        
        filepath = '{}{}{}'.format(subdir, os.sep, file)

        if (filepath.endswith(".tif") | filepath.endswith(".tiff")):
            
            try:
            
                ds = gdal.Open(filepath, gdal.GA_ReadOnly)
                data = gdal.Info(ds,**kwargs)
                filedata = open('{}.json'.format(filepath.split('.')[0]),'w')
                json.dump(data,filedata)
                print('Pid {} was completed successfully'.format(file.split('.')[0]))
            
            except RuntimeError as e:
                print('Unable to open {}'.format(filepath))
                print(e)
                sys.exit(1)


filedata.close()