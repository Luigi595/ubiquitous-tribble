import gpxpy
import csv   
import os
import re

#create csv file called merged.csv to working directory
with open(r'mexico.csv', 'a') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_NONE, escapechar=' ', lineterminator='\n')
    writer.writerow('yxt')
    
#This requires a folder named gpx_files in the working directory
for file in os.listdir('gpx_files'):
    filePath = 'gpx_files/' + file
    print(filePath)  
    gpx_file = open(filePath, 'r')
    gpx = gpxpy.parse(gpx_file)
    count = 0
    
    #iterate through rows and append each gpx row to merged csv
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                fields=['{0},{1},{2}'.format(point.latitude, point.longitude, point.time)] 
                #Here double whitespace is removed so QGIS accepts the time format
                re.sub(' +',' ',fields[0])
                #Use every other GPX point
                count += 1
                if count % 2 == 0: 
                    with open(r'merged.csv', 'a') as f:
                        writer = csv.writer(f, quoting=csv.QUOTE_NONE, escapechar=' ', lineterminator='\n')
                        writer.writerow(fields)
