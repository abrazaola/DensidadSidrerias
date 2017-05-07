#!/usr/bin/python

#import urllib
import sys
from xml.etree import ElementTree as ET

#requestURL = 'http://opendata.euskadi.eus/contenidos/ds_recursos_turisticos/restaurantes_asador_sidrerias/opendata/restaurantes.xml'
#print requestURL;

#root = ET.parse(urllib.urlopen(requestURL)).getroot()
root = ET.parse(sys.stdin).getroot()
print root
print '\n'

rows = root.findall('row')
for row in rows:
	if row.find('restorationtype').text == 'Sidreria':
		municipality = row.find('municipality').text.encode('utf-8')
		print "{0}\t1".format(municipality)
