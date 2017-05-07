#!/usr/bin/python

import urllib
import sys
from xml.etree import ElementTree as ET

requestURL = 'http://opendata.euskadi.eus/contenidos/ds_recursos_turisticos/restaurantes_asador_sidrerias/opendata/restaurantes.xml'
print requestURL;

root = ET.parse(urllib.urlopen(requestURL)).getroot()
tree = ET.ElementTree(root)
tree.write("restaurantes.xml")
print 'Dataset downloaded successfully.\n'
