import json
from sys import exit, argv, stderr
import urllib2

if len(argv) < 2:
	stderr.write('Not enough params')
	exit(-1)

json_file = argv[1]

with open(json_file, "r") as fh:
	d = json.load(fh)
	url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins="
	for portal in d['portals'][:10]:
		plong = portal['long']
		plat = portal['lat']
		name = portal['name']
		url += '%f,%f|' % (plong, plat)

	print url