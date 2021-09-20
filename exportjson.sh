#!/bin/bash

com=$(ls | grep ".tif")
for i in $(com); do
    name=$(echo "$com" | cut -f1 -d'.')
    extension='.json'
    gdalinfo -json $i > "${name}${extension}"
done;