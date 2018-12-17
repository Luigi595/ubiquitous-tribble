
Visualisation of shortest routes from an origin point to endpoints uniformly distributed in a geographic area

### Prerequisites

Python 3
* Pandas
* gpxpy

QGIS

Graphhopper
* Latest JDK

### Usage
Find the OSM (Open Street Map) of the area you going to map and download it, I used [Geofabrik.de](http://download.geofabrik.de/)

Have a csv file with the coordinates of the endpoints you want, they could be fixed coordinates (e.g. counties) or a grid of points  
The latter one being the one used for this output, to do this, find the coordinates polygon of the area you want to map,
you can try [here](https://www.naturalearthdata.com)  
Now, open the .shp file in QGIS, in the processing toolbox select the create regular points tool,
use the bounds of the file and create as many points as you need.  
Finally, export the created points as a csv file

Moving on, it's time to use Graphhopper, just execute it with the OSM file we downloaded earlier  
(A word of notice, the file I used was too big for the default limit so I had to use the command 
export JAVA_OPTS="-Xmx10g -Xms10g" before running graphhopper)

With graphhoper running, modify the file apiCalling.py so that it has the correct origin and filenames, and then run it.

We now have a folder with gpx files that we will parse into a single csv file; just run parsing.py

We have now calculated the shortest routes from the origin point to the endpoints and they are contained in a single csv file, in order to visualize this,
open QGIS and select Layer > Add Layer > Add Delimited Text Layer...

Select the merged.csv file with the appropriate X,Y coordinates, accept and you should see the routes on the map

At last, style the points and the background, export it to the image file of your preference and we're done.
