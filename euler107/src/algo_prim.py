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

# ---------------------------------

from src.graph import Graph
from Queue import PriorityQueue

class Prim(object):
    name = 'prim'

    def __init__(self, save_all_edges=False):
        self.graph = Graph()
        self.logging = False
        self.save_all_edges = save_all_edges
        self.all_edges = []

    def set_logging(self, level):
        if level == 'debug':
            print('Logging turned on')
            self.logging = True

    def add_edge(self, node1, node2, weight, n, n_nodes, n_edges):
        if self.save_all_edges:
            self.all_edges.append((node1, node2, weight))
        if self.logging:
            if n % 200000 == 0:
                print('Importing {0} of {1}'.format(n, n_edges))

    def init_from_file(self, f):
        self.graph.import_data(f, self.add_edge)
    
    def solve(self):
        visited_nodes = set()
        remaining_nodes = set(range(self.graph.n_nodes))
        touching_edges = PriorityQueue()
        res = []
        
        this_node = 0
        while 1:
            # Add new node, finish if no reamining nodes
            visited_nodes.add(this_node)
            remaining_nodes.remove(this_node)
            if len(remaining_nodes) == 0:
                break
            
            # Add new linked nodes to touching_edges
            new_linked_nodes = self.graph.edges[this_node]
            for new_node in new_linked_nodes:
                touching_edges.put((self.graph.weights[(this_node, new_node)], (this_node, new_node)))

            # Pick minimum weight edge to do next
            while 1:
                (new_weight, new_edge) = touching_edges.get()
                if new_edge[1] not in visited_nodes:
                    break
            
            res.append((new_edge[0], new_edge[1], new_weight))
            this_node = new_edge[1]

        return (self.graph.n_nodes, len(res), res)

