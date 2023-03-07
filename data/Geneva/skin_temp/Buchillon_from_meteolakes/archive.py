#!/usr/bin/env python
# -*- coding: utf-8 -*-
#################
from __future__ import print_function
import os
import csv
import sys
import ast
import json
from datetime import datetime
#################
# Measurement auto-archive script by Martin Zoller/Theo Baracchini

# Print to stderr
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def fail(err):
    eprint(err)
    sys.exit(1)

# Data directory and list of files to archive
datadir = 'M:/Online/localExtraction/wwwroot/meteolac/campbell_buchillon'
datafiles = ['Buchillon_PTB110', 'Buchillon_KT1585', 'Buchillon_LoggerSensor', 'Buchillon_WeatherSensor']
dataext = '.dat'
binfiles = ['mode1a', 'mode11a']
binext = '.000'
statusfile = 'Buchillon_CPIStatus.dat'
avjson = 'available_data.json'

os.chdir(datadir)
try:
    with open(avjson, 'rb') as jsonfile:
        avdata = json.load(jsonfile)
except IOError:
    avdata = {} # No pre-existing available_data file

for myfile in datafiles:
    if not os.path.isfile(myfile + dataext):
        continue
    tempfile = myfile + dataext + '.archiving'

    os.rename(myfile + dataext, tempfile)
    with open(tempfile, 'rb') as csvhandle:
        firstline = csvhandle.readline() # ignore first line as headers are on second one
        rdr = csv.DictReader(csvhandle, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_NONNUMERIC)
        if myfile in avdata:
            if rdr.fieldnames != avdata[myfile]['columns']:
                fail("Error: Columns of " + myfile + dataext + " do not match existing archive data")
        else:
            avdata[myfile] = { 'columns': rdr.fieldnames, 'data': [] }
        lineno = 0
        headerlines = []
        destfile = ''
        for row in rdr:
            lineno += 1
            # Don't parse lines 3 and 4 (units) but save them for later
            if lineno < 3:
                headerlines.append(row)
                continue
            # Avoid treating integers as floats (CSV module default behavior)
            for i, val in row.iteritems():
                try:
                    if val == int(val):
                        row[i] = int(val)
                except ValueError:
                    pass
            # Parse timestamp and create archive files accordingly
            try:
                rdate = datetime.strptime(row['TIMESTAMP'][:19], '%Y-%m-%d %H:%M:%S')
            except KeyError:
                fail('Error: Invalid timestamp data in ' + myfile + dataext)
            yeardir = './' + str(rdate.year)
            monstr = datetime.strftime(rdate,'%Y-%m')
            if not os.path.exists(yeardir):
                os.makedirs(yeardir)
            monfile = yeardir + '/' + myfile + '_' + monstr + dataext
            if destfile != monfile:
                try:
                    desthandle.close()
                except NameError:
                    pass
                if not monstr in avdata[myfile]['data']:
                    avdata[myfile]['data'].append(monstr)
                destfile = monfile
                hasfile = os.path.isfile(destfile)
                desthandle = open(destfile, 'ab')
                wri = csv.DictWriter(desthandle, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_NONNUMERIC, fieldnames=rdr.fieldnames)
                # Start a new file (with complete 4-line header) for every month
                if not hasfile:
                    desthandle.write(firstline)
                    wri.writeheader()
                    wri.writerow(headerlines[0])
                    wri.writerow(headerlines[1])
            wri.writerow(row)
    os.remove(tempfile)
    try:
        desthandle.close()
    except NameError:
        pass

# finally, update list of available data
with open(avjson,'wb') as jsonfile:
    json.dump(avdata, jsonfile)

# Binary files: Just check if they exist and append to monthly file
yeardir = './' + str(datetime.now().year)
monstr = datetime.strftime(datetime.now(),'%Y-%m')
if not os.path.exists(yeardir):
    os.makedirs(yeardir)
for myfile in binfiles:
    if not os.path.isfile(myfile + binext):
	    continue
    tempfile = myfile + binext + '.archiving'
    os.rename(myfile + binext, tempfile)
    monfile = yeardir + '/' + myfile + '_' + monstr + binext
    with open(tempfile, 'rb') as fhandle:
        fcontent = fhandle.read()
        with open(monfile, 'ab') as desthandle:
            desthandle.write(fcontent)
    os.remove(tempfile)

# Status file: No need to archive it, so delete it.
if os.path.isfile(statusfile):
    os.remove(statusfile)