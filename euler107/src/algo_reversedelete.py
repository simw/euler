# ---------------------------------
# More compatible with python 3 code
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

try:
    range = xrange
except NameError:
    pass

from Queue import PriorityQueue
from src.graph import Graph

class ReverseDelete(object):
    name = 'reversedelete'

    def __init__(self, save_all_edges=False):
        self.queue = PriorityQueue()
        self.graph = Graph()
        self.logging = False
        self.save_all_edges = save_all_edges
        self.all_edges = []
    
    def set_logging(self, level):
        if level == 'debug':
            self.logging = True

    def add_edge(self, node1, node2, weight, n, n_nodes, n_edges):
        self.queue.put((-weight, (node1, node2)))
        if self.save_all_edges:
            self.all_edges.append((node1, node2, weight))

    def init_from_file(self, f):
        self.graph.import_data(f, self.add_edge)

    def solve(self):
        res = []
        while not self.queue.empty():
            (weight, edge) = self.queue.get()
            self.graph.remove_edge(edge[0], edge[1])
            if not self.graph.is_connected():
                self.graph.add_edge(edge[0], edge[1], -weight)
                res.append((edge[0], edge[1], -weight))
                continue
        
        return (self.graph.n_nodes, len(res), res)
