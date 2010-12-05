=================
ogr2osm for Idjwi
=================

About
=====

Originally developed by Ivan Sanche, the script converts any OGR supported vector format (tested with Shapefiles so far) to OpenStreetMap data.

OpenStreetMap wiki page: http://wiki.openstreetmap.org/wiki/Ogr2osm

The current code is a slightly customized version with the goal to publish Shapefiles for the Island of Idjwi in OpenStreetMap.

It is also part of a RHOK project: http://wiki.rhok.org/Geo_data_file_format_converter

Usage
=====

::

    python ogr2osm.py -t myTranslation path/to/myshapefile.shp

Roadmap
=======

* Migrate to Google's app engine
* Provide a web-interface for creating attribute-tag translation files
