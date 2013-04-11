import json
from sys import argv, stderr, exit
import csv

if len(argv) < 2:
	stderr.write('Not enough params')
	exit(-1)

csv_file = argv[1]

portals = []

with open(csv_file, "r") as fh:
	reader = csv.reader(fh)
	for row in reader:
		portal = {'name': row[2].decode('utf-8'), 'long': float(row[0]), 'lat': float(row[1])}
		portals.append(portal)

portal_dict = {'portals': portals}

print json.dumps(portal_dict)