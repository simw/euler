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

# End of more compatible with python 3
# ---------------------------------

from collections import deque
from collections import defaultdict

class Graph(object):
    def __init__(self):
        self.n_nodes = 0
        self.edges = defaultdict(set)
        self.weights = {}

    def import_data(self, f, callback=None):
        n = 0
        for line in f:
            n += 1
            if n == 1:
                self.n_nodes = int(line)
            elif n == 2:
                self.n_edges = int(line)
            else: 
                words = line.split()
                node1 = int(words[0])
                node2 = int(words[1])
                weight = float(words[2])
                self.add_edge(node1, node2, weight)
                if callback:
                    callback(node1, node2, weight, n-2, self.n_nodes, self.n_edges)

    def add_edge(self, node1, node2, weight=1):
        self.n_nodes = max(self.n_nodes, node1+1, node2+1)
        self.edges[node1].add(node2)
        self.edges[node2].add(node1)
        self.weights[(node1, node2)] = weight
        self.weights[(node2, node1)] = weight
        
    def remove_edge(self, node1, node2):
        # Removes the edge, but doesn't alter n_nodes        
        self.edges[node1].remove(node2)
        self.edges[node2].remove(node1)
        del self.weights[(node1, node2)]
        del self.weights[(node2, node1)]

    def is_connected(self):
        remaining_nodes = set(range(self.n_nodes))
        nodes_queue = deque([0])
        remaining_nodes.remove(0)
        while 1:
            if len(remaining_nodes) == 0:
                return True

            if len(nodes_queue) == 0:
                return False

            this_node = nodes_queue.pop()
            for new_node in self.edges[this_node]:
                if new_node in remaining_nodes:
                    nodes_queue.append(new_node)
                    remaining_nodes.remove(new_node)

    # def is_cyclic(self):
    #     remaining_nodes = set(range(self.n_nodes))
    #     nodes_visited = set()
    #     nodes_to_visit = deque([(0, 0)])

    #     res = False
    #     while 1:
    #         if len(remaining_nodes) == 0 and len(nodes_to_visit) == 0:
    #             break
    #         if len(nodes_to_visit) == 0:
    #             new_node = remaining_nodes.pop()
    #             nodes_to_visit.append((new_node, new_node))

    #         (from_node, this_node) = nodes_to_visit.pop()
    #         nodes_visited.add(this_node)
    #         
    #         for new_node in self.edges[this_node]:
    #             if new_node == from_node:
    #                 continue

    #             if new_node in nodes_visited:
    #                 print(this_node, new_node, nodes_visited, nodes_to_visit, remaining_nodes)
    #                 print('cyclic')
    #                 return True

    #             if new_node in remaining_nodes:
    #                 nodes_to_visit.append((this_node, new_node))
    #                 remaining_nodes.remove(new_node)

    #     print('not cyclic')
    #     return False 

