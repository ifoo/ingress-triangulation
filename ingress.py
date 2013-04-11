from math import sin, cos

import matplotlib.delaunay as triang
import pylab
import numpy
import matplotlib.pyplot as plt
from sys import exit


DATA_FILE ='/home/ifoo/Desktop/ingress/coords.data'

def read_file(filename):
    portals = []
    with open(filename, 'r') as fh:
        for line in fh.readlines():
            pid, coord_name = line.strip().split(':')
            coord, name = coord_name.split(';')
            clong, clat = coord.split(',')
            name = name.decode('utf-8')
            portals.append({'id': pid, 'coords': {'gmaps': {'long': float(clong), 'lat': float(clat)}}, 'name': name})
    return portals

def delaunay_triangulation(portals):
    xx = []
    yy = []
    ids = []
    names = []

    for p in portals:
        ids.append(p['id'])
        names.append(p['name'])
        xx.append(p['coords']['gmaps']['lat'])
        yy.append(p['coords']['gmaps']['long'])

    xx = numpy.array(xx)
    yy = numpy.array(yy)

    cens,edg,tri,neig = triang.delaunay(xx,yy)

    print min(xx), max(xx)
    print min(yy), max(yy)

    return {'cens': cens, 'edg': edg, 'tri': tri, 'neig': neig, 'xx': xx, 'yy': yy, 'id': ids, 'names': names}


portals = read_file(DATA_FILE)
tris = delaunay_triangulation(portals)

fig, ax = plt.subplots()
im = plt.imread('map.png')
y, x, z = im.shape
exit()
for t in tris['tri']:
    #t[0], t[1], t[2] are the points indexes of the triangle
    t_i = [t[0], t[1], t[2], t[0]]
    ax.plot(tris['xx'][t_i], tris['yy'][t_i])

ax.plot(tris['xx'], tris['yy'],'o')

lpoints = []
lnames = []
for x,y, pid, nm in zip(tris['xx'], tris['yy'], tris['id'], tris['names']):
    ax.annotate(pid, xy=(x,y), xytext=(5, 5), ha='right', textcoords='offset points')
    p = pylab.Rectangle((0, 0), 1, 1, fc="black")
    lnames.append('%s - %s' % (pid, unicode(nm)))
    lpoints.append(p)



#ax.legend((p1, p2, p3), ('proj1','proj2','proj3'), loc=2)
pylab.legend(lpoints, lnames, bbox_to_anchor=(1.05, 1), loc=2, fontsize='x-small', frameon=True, borderaxespad=0.)

#pylab.xlim((13.201563, 13.494532))
#pylab.ylim((47.291774, 47.425084))
implot = plt.imshow(im)

pylab.show()


