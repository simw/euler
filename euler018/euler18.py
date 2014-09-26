
import sys

def get_data(filename):
    nums = []
    with open(filename, 'r') as f:
        for line in f:
            nums.append([int(word) for word in line.strip().split()])
    return nums

def find_max_route(data):
    max_vals = data[len(data)-1]
    max_routes = [[i] for i in data[len(data)-1]]
    for i in reversed(range(len(data)-1)):
        old_max_vals = max_vals[:]
        old_max_routes = max_routes[:]

        max_vals = []
        max_routes = []
        
        for j in range(i+1):
            if old_max_vals[j] > old_max_vals[j+1]:
                max_vals.append(data[i][j] + old_max_vals[j])
                max_routes.append([data[i][j]] + old_max_routes[j])
            else:
                max_vals.append(data[i][j] + old_max_vals[j+1])
                max_routes.append([data[i][j]] + old_max_routes[j+1])

    return (max_vals, max_routes)

def main():
    data = get_data(sys.argv[1])
    route = find_max_route(data) 

    print(route)
    
if __name__ == '__main__':
    main()
