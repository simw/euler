from __future__ import unicode_literals
from __future__ import absolute_import

from src.algo_prim import Prim
from src.algo_reversedelete import ReverseDelete
from src.algo_kruskal import Kruskal

algorithms = {
    '1': Prim,
    '2': ReverseDelete,
    '3': Kruskal
}

def choose_algorithm(choice):
    choice = '{0}'.format(choice).strip()
    algo = algorithms[choice]
    return algo

def print_algorithms():
    for i in enumerate(algorithms):
        print('  {0}: {1}'.format(i, algorithms[i].name))
