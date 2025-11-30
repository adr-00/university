# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from lib.unsorted_priority_queue import UnsortedPriorityQueue
from lib.graph import Graph

def MST_PrimJarnik(g):
  d = {}                               # d[v] is bound on distance to tree
  tree = []                            # list of edges in spanning tree
  pq = UnsortedPriorityQueue()         # d[v] maps to value (v, e=(u,v))
  vintree = []                         # vertexs in tree
 
  # for each vertex v of the graph, add an entry to the priority queue, with
  # the source having distance 0 and all others having infinite distance
  for v in g.vertices():
    if len(d) == 0:                                 # this is the first node
      d[v] = 0                                      # make it the root
    else:
      d[v] = float('inf')                           # positive infinity
    pq.add(d[v], (v,None))

  while not pq.is_empty():
    key,value = pq.remove_min()
    u,edge = value                                  # unpack tuple from pq
    if edge is not None:
      tree.append(edge)                             # add edge to tree
      vintree.append(u)                             # add vertex to tree
    for link in g.incident_edges(u):
      v = link.opposite(u)
      if not(v in vintree):                         # thus v not yet in tree
        # see if edge (u,v) better connects v to the growing tree
        wgt = link.element()
        if wgt < d[v]:                              # better edge to v?
          d[v] = wgt                                # update the distance
          pq.update(v,d[v],(v,link))               # update the pq entry (modifica la clave y valor de v)

  return tree

from grafo1 import * 

if __name__ == '__main__':

    g = leerGrafo("grafo6.txt")

    print('Numero de vertices ',g.vertex_count())
    print('Numero de ejes',g.edge_count())

    tree = MST_PrimJarnik(g)

    for e in tree:
        (u,v) = e.endpoints()
        print(u,' ',v,' ', e.element())

    