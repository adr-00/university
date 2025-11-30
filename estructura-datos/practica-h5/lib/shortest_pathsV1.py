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

def shortest_path_lengths(g, src):
  """Compute shortest-path distances from src to reachable vertices of g.

  Graph g can be undirected or directed, but must be weighted such that
  e.element() returns a numeric weight for each edge e.

  Return dictionary mapping each reachable vertex to its distance from src.
  """
  d = {}                                        # d[v] is upper bound from s to v
  cloud = {}                                    # map reachable v to its d[v] value
  pq = UnsortedPriorityQueue()                  # vertex v will have key d[v]

  # for each vertex v of the graph, add an entry to the priority queue, with
  # the source having distance 0 and all others having infinite distance
  for v in g.vertices():
    if v is src:
      d[v] = 0
    else:
      d[v] = float('inf')                       # syntax for positive infinity
    #pq.add(d[v], (v,None))                           # save locator for future updates
    pq.add(d[v], v) 

  while not pq.is_empty():

    #key, value = pq.remove_min()
    #u, edge = value
    key, u = pq.remove_min()
    cloud[u] = key                              # its correct d[u] value
    for e in g.incident_edges(u):               # outgoing edges (u,v)
      v = e.opposite(u)
      if v not in cloud:
        # perform relaxation step on edge (u,v)
        wgt = e.element()
        if d[u] + wgt < d[v]:                   # better path to v?
          d[v] = d[u] + wgt                     # update the distance
          #pq.update(v,d[v],(v,edge))            # update the pq entry (solo se modifica la clave key de v)
          pq.update(v,d[v],v)
  
  return cloud                                  # only includes reachable vertices

def shortest_path_tree(g, s, d):
  """Reconstruct shortest-path tree rooted at vertex s, given distance map d.

  Return tree as a map from each reachable vertex v (other than s) to the
  edge e=(u,v) that is used to reach v from its parent u in the tree.
  """
  tree = {}
  for v in d:
    if v is not s:
      for e in g.incident_edges(v, False):       # consider INCOMING edges
        u = e.opposite(v)
        wgt = e.element()
        if d[v] == d[u] + wgt:
          tree[v] = e                            # edge e is used to reach v
  return tree

def construct_path(u,v,discovered):
    path = []
    if v in discovered:
        path.append(v)
        walk = v
        while walk is not u:
            e = discovered[walk]
            parent = e.opposite(walk)
            path.append(parent)
            walk = parent
        path.reverse()
    return path