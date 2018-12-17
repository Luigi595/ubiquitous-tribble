import pandas as pd
import urllib.request

# path to csv file with the endpoint coordinates
endpnts = pd.read_csv('hdmexpoints.csv')

# graphhopper API
urlStart = 'http://localhost:8989/route?'
pnt = 'point='
urlEnd = '&type=gpx&instructions=false&vehicle=car'
separator = '%2C'

# Coordinates (lon,lat) of the origin (Zocalo, Mexico City, Mexico)
# Could add more origins, or run the program more times for a different project
startX = '-99.1332' 
startY = '19.4326'

# Individual API calls from origin to endpoint in csv, then writes data in gpx file
for index, row in endpnts.iterrows():
    req = urlStart + pnt + startY + separator + startX + '&' + pnt + str(row['Y']) + separator + str(row['X']) + urlEnd
    #Sometimes the error is not in graphhopper, but in the code, use a fixed working location to test
    #req = "http://localhost:8989/route?point=19.4326%2C-99.1332&point=20.66682%2C-103.39182&type=gpx&instructions=false&vehicle=car"
    try:
        resp = urllib.request.urlopen(req)
        gpxData  = str(resp.read(),'utf-8')
        fileName = 'mexico_' + str(index)
        saveFile = open('gpx_files/{0}.gpx'.format(fileName), 'w')
        print('processed index ' + str(index))
        saveFile.write(gpxData)
        saveFile.close()
    except:
        #Sometimes, a lot of bad requests are generated, it may only mean there's no shortest route
        print('bad request on index ' + str(index))
        pass
