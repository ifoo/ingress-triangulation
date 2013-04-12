import json
from sys import argv, stderr, exit
import csv
import urllib2
import pylab
from scipy.cluster.vq import kmeans2
import numpy
import matplotlib.delaunay as triang
from scipy import spatial

def read_from_csv(csv_file_name):
	portals = set()
	with open(csv_file_name, 'r') as fh:
		reader = csv.reader(fh)
		for row in reader:
			portal = (float(row[1]), float(row[0]))
			portals.add(portal)
	return portals

def generate_unique_hash(portals):
	hv = 0
	for portal in portals:
		hv ^= hash(portal)
	return hv

def create_numpy_array(portals):
	return numpy.array(list(portals))

def get_map_borders(array):
	omin, omax = array[:,0].min(), array[:,0].max()
	amin, amax = array[:,1].min(), array[:,1].max()
	return (omin, omax, amin, amax)

def kmeans_cluster(array, n=10):
	return kmeans2(array, n)

def get_nearest_portal_for_center_of_mass(com_list, array):
	return array[:][spatial.cKDTree(array).query(com_list)[1]]

def google_distance_matrix(cluster_points):
	origins = '|'.join(('%f,%f' %(p[1], p[0]) for p in cluster_points))
	destinations = '|'.join(('%f,%f' %(p[1], p[0]) for p in reversed(cluster_points)))
	url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=%s&destinations=%s&language=de&sensor=false" % (origins, destinations)
	data = urllib2.urlopen(url).read()
	return json.loads(data)


if len(argv) < 2:
	stderr.write('Not enough params')
	exit(-1)

csv_file = argv[1]

portals = read_from_csv(csv_file)
a = create_numpy_array(portals)

res, idx = kmeans_cluster(a)

nearest = get_nearest_portal_for_center_of_mass(res, a)
#google_distance_matrix(nearest)

colors = ['blue', 'red', 'green', 'yellow', 'orange', 'purple', 'brown', 'black', 'gray', 'cyan']
pcols = [colors[i] for i in idx]

cens, edg, tri, neig = triang.delaunay(a[:,0], a[:,1])

pylab.scatter(res[:,0], res[:,1], marker='o', c=colors)
pylab.scatter(a[:,0],a[:,1], c=pcols, marker='x')
pylab.scatter(nearest[:,0], nearest[:,1], c='black', marker='+')
#print get_map_borders(a)

print "found %d triangles .." %(len(tri), )

for t in tri:
	ti = [t[0], t[1], t[2], t[0]]
	pylab.plot(a[:,0][ti], a[:,1][ti])
#pylab.savefig('foo.svg', tranparent=True)
pylab.show()

#print google_distance_matrix(res)
# http://parent.tile.openstreetmap.org/cgi-bin/export?bbox=13.189897,47.291773999999997,13.494532,47.48698199999999&scale=59000&format=svg
