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

import sys
import os

from src.chooser import choose_algorithm, print_algorithms

def print_usage():
    print('Minimum spanning tree solver:')
    print('Usage:')
    print('  python main.py X Y')
    print()
    print('  where:')
    print('    X is the filename of mst data')
    print('    Y is an integer 1,2,3 ...')
    print()
    print('Available solvers:')
    print_solvers()
    print()

def get_opts():
    algo = sys.argv[2]
    filename = sys.argv[1]
    return (algo, filename)

def print_results(n_nodes, n_edges, edges, all_edges, algo_name):
    total_weight = sum([edge[2] for edge in edges])
    total_all_weight = sum([edge[2] for edge in all_edges])

    print('MST {0} algorithm:'.format(algo_name))
    print('Original weight = {0}'.format(total_all_weight))
    print('Total weight = {0}'.format(total_weight))
    print('Diff = {0}'.format(total_all_weight-total_weight))
    print('Number of nodes = {0}'.format(n_nodes))
    print('Number of edges = {0}'.format(n_edges))

def main():
    if len(sys.argv) < 3:
        print_usage()
        return

    (algo_choice, file_in) = get_opts()
    Algo = choose_algorithm(algo_choice)

    algo = Algo(True)
    with open(file_in, 'r') as f:
        algo.init_from_file(f)
    (n_nodes, n_edges, edges) = algo.solve()
    
    print_results(n_nodes, n_edges, edges, algo.all_edges, algo.name)

if __name__ == '__main__':
    main()
