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

from datetime import datetime
from Queue import PriorityQueue

class Kruskal(object):
    name = 'kruskal'

    def __init__(self, save_all_edges=False):
        self.edges = PriorityQueue()
        self.logging = False
        self.save_all_edges = save_all_edges
        self.all_edges = []
    
    def set_logging(self, level):
        if level == 'debug':
            print('Logging turned on')
            self.logging = True

    def init_from_file(self, f):
        n = 0
        for line in f:
            n += 1
            if n == 1:
                self.n_nodes = int(line)
            elif n == 2:
                self.n_edges = int(line)
            else:
                words = line.split()
                self.edges.put((float(words[2]), (int(words[0]), int(words[1]))))
                if self.save_all_edges:
                    self.all_edges.append((int(words[0]), int(words[1]), float(words[2])))
                if self.logging:
                    if n % 200000 == 0:
                        print('{0}: Importing {1} of {2}'.format(str(datetime.now()), n, self.n_edges))

    def solve(self):
        res = []
        trees = [set([i]) for i in range(self.n_nodes)]
        node_to_tree_map = list(range(self.n_nodes))

        n = 0
        while 1:
            n += 1
            (weight, edge) = self.edges.get()
            if node_to_tree_map[edge[0]] != node_to_tree_map[edge[1]]:
                # Add edge and merge trees
                res.append((edge[0], edge[1], weight))
                tree1 = node_to_tree_map[edge[0]]
                tree2 = node_to_tree_map[edge[1]]
                for node in trees[tree2]:
                    node_to_tree_map[node] = tree1
                trees[tree1] = trees[tree1].union(trees[tree2])
                trees[tree2].clear()

                if self.logging:
                    if n % 100000 == 0:
                        print('{0}: Completed {1} of {2} nodes, {3} of {4} edges'.format(
                            str(datetime.now()), len(res), self.n_nodes-1, n, self.n_edges))

                if len(trees[tree1]) == self.n_nodes:
                    break

        return (self.n_nodes, len(res), res)

