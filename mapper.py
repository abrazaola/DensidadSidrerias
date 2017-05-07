#!/usr/bin/python

import sys
from xml.etree import ElementTree as ET

root = ET.parse(sys.stdin).getroot()
print root
print '\n'

rows = root.findall('row')
for row in rows:
	if row.find('restorationtype').text == 'Sidreria':
		municipality = row.find('municipality').text.encode('utf-8')
		print "{0}\t1".format(municipality)
