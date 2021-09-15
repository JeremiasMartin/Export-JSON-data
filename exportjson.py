import sys
import os
from osgeo import gdal
from pathlib import Path
import json
import params as params

kwargs = {
    'allMetadata':True,
    'format':'json',
}

for subdir, dirs, files in os.walk(params.input_folder):
    for file in files:
        filepath = subdir + os.sep + file

        if (filepath.endswith(".tif") | filepath.endswith(".tiff")):
            
            try:
            
                ds = gdal.Open(filepath, gdal.GA_ReadOnly)
                data = gdal.Info(ds,**kwargs)
                file = open('{}.json'.format(filepath),'w')
                json.dump(data,file)
            
            except RuntimeError as e:
                print('Unable to open {}'.format(filepath))
                print(e)
                sys.exit(1)


file.close()