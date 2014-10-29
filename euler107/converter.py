import sys

def main():
    filename = sys.argv[1]
    filename_out = sys.argv[2]

    edges = []
    with open(filename, 'r') as f:
        line_number = 0
        for line in f:
            weights = line.split(',')
            for (i, weight) in enumerate(weights):
                weight = weight.strip()
                if weight != '-' and i > line_number:
                    edges.append((line_number, i, int(weight)))
            line_number += 1 

    n_nodes = len(weights)
    n_edges = len(edges)

    with open(filename_out, 'w') as f:
        f.write('{0}\n'.format(n_nodes))
        f.write('{0}\n'.format(n_edges))
        for edge in edges:
            f.write('{0} {1} {2}\n'.format(edge[0], edge[1], edge[2]))

if __name__ == '__main__':
    main()
