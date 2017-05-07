#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

lastMunicipality = None
lastCount = 0

for line in sys.stdin:
  data_mapped = line.strip().split("\t")
  if len(data_mapped) != 2:
    continue
  municipality, count = data_mapped
  if lastMunicipality and lastMunicipality != municipality:
    print lastMunicipality, "\t", lastCount
    lastCount = 0
  lastMunicipality = municipality
  lastCount += int(count)

if lastMunicipality:
  print lastMunicipality, "\t", lastCount

