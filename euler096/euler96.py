from __future__ import print_function
from copy import deepcopy

constraint = range(9)

class ConflictException(Exception):
    pass

def transform_coords(x, y, ver):
    if ver == 0:
        xbar = x
        ybar = y 

    elif ver == 1:
        xbar = y 
        ybar = x

    elif ver == 2:
        xbar = int(x / 3) * 3 + int(y / 3)
        ybar = (x % 3) * 3 + (y % 3)

    else:
        raise Exception('transform called with invalid version {0}'.format(ver))

    return (xbar, ybar)

class Constraint(object):
    def __init__(self, size=9):
        self.values = tuple(([-1 for y in range(size)] for x in range(size)))
        self.constraints = tuple(([range(size) for y in range(size)] for x in range(size)))

    def set_value(self, x, y, value):
        self.values[x][y] = value
        

class Board(object):
    def __init__(self):
        self.values = tuple(([-1 for x in range(9)] for x in range(9))) 
        self.constraints = tuple(([constraint[:] for x in range(9)] for x in range(9)))
        
        self.value_maps = tuple(([[-1 for x in range(9)] for x in range(9)] for x in range(3)))
        self.value_map_constraints = tuple(([[constraint[:] for x in range(9)] for x in range(9)] for x in range(3)))
        
        self.unknowns = 81
    
    def set_value(self, x, y, value):
        if value >= 0:
            self.values[x][y] = value
            self.unknowns = self.unknowns - 1
            if self.unknowns == 0:
                return 0
            
            for i in range(3):
                for ybar in range(9):
                    xbar = transform_coords(x, y, i)[0]
                    (xprime, yprime) = transform_coords(xbar, ybar, i)
                    if self.values[xprime][yprime] < 0 and value in self.constraints[xprime][yprime]:
                        self.constraints[xprime][yprime].remove(value)

            for i in range(3):
                (xbar, ybar) = transform_coords(x, y, i)
                self.value_maps[i][xbar][value] = ybar

            for i in range(3):
                (xbar, ybar) = transform_coords(x, y, i)
                for j in [j for j in range(3) if j != i]:
                    for zbar in range(9):
                        (xprime, zprime) = transform_coords(xbar, zbar, i)
                        (xbarbar, zprimebarbar) = transform_coords(xprime, zprime, j)
                        if zprimebarbar in self.value_map_constraints[j][xbarbar][value] and self.value_maps[j][xbarbar][value] < 0:
                            self.value_map_constraints[j][xbarbar][value].remove(zprimebarbar)
                            if len(self.value_map_constraints[j][xbarbar][value]) < 1:
                                raise ConflictException('value_maps conflict when setting {0}, {1} to be {2}'.format(x, y, value))
                    
        return self.unknowns

    def get_value(self, row, col):
        return self.values[row][col]

    def check_possibilities(self):
        for x in range(9):
            for y in range(9):
                if len(self.constraints[x][y]) < 1:
                    raise ConflictException('Less than 1 value left')
                if len(self.constraints[x][y]) == 1 and self.values[x][y] < 0:
                    self.set_value(x, y, self.constraints[x][y][0])

        for i in range(3):
            for zbar in range(9):
                for value in range(9):
                    if len(self.value_map_constraints[i][zbar][value]) < 1:
                        raise ConflictException('value_maps: less than 1 value')
                        pass
                    elif self.value_maps[i][zbar][value] < 0 and len(self.value_map_constraints[i][zbar][value]) == 1:
                        (x, y) = transform_coords(zbar, self.value_map_constraints[i][zbar][value][0], i)
                        if self.values[x][y] < 0:
                            self.set_value(x, y, value)
                        
    def read_text(self, txt):
        txt = txt.replace(' ', '').replace('\n', '').replace('\r', '')

        for i in range(len(txt)):
            row = int(i/9)
            col = i % 9
            self.set_value(row, col, int(txt[i])-1)

    def get_topleft(self):
        return (self.values[0][0]+1) * 100 + (self.values[0][1]+1) * 10 + (self.values[0][2]+1)

    def print_board(self):
        print_vals = [self.values[i][:] for i in range(9)]
        # print_vals = self.values[:][:]
        for i in range(9):
            for j in range(9):
                if print_vals[i][j] < 0:
                    print_vals[i][j] = ' '
                else:
                    print_vals[i][j] = print_vals[i][j] + 1

        for row in range(9):
            if row != 0 and (row)%3 == 0:
                print('------+-------+-------')

            print('{0} {1} {2} | {3} {4} {5} | {6} {7} {8}'.format(print_vals[row][0],
                print_vals[row][1], print_vals[row][2], print_vals[row][3],
                print_vals[row][4], print_vals[row][5], print_vals[row][6],
                print_vals[row][7], print_vals[row][8]))
    
    def print_constraints(self):
        for x in range(9):
            for y in range(9):
                if self.values[x][y] < 0:
                    print(len(self.constraints[x][y]), end='')
                else:
                    print('-', end='')
            print('')

def guess(board):
    original_board = deepcopy(board)

    for x in range(9):
        for y in range(9):
            if board.values[x][y] < 0:
                break
        if board.values[x][y] < 0:
            break

    if len(board.constraints[x][y]) == 0:
        return False

    this_guess = board.constraints[x][y][0]
    # print('Guessing {0} in ({1}, {2}) with {3} unknowns remaining'.format(this_guess, x, y, board.unknowns))
    try:
        board.set_value(x, y, this_guess)
        res = go(board)

        if res:
            return res
        # print('Stalled') 
    except ConflictException as e:
        # print('Conflict')
        pass
            
    original_board.constraints[x][y].remove(this_guess)
    return guess(original_board)

def go(board):
    unknowns = board.unknowns
    board.check_possibilities()

    # print('{0} unknowns'.format(board.unknowns))
    if board.unknowns == 0:
        return board
    elif board.unknowns == unknowns:
        return guess(board)

    return go(board)

def main():
    f = open('p096_sudoku.txt', 'r')

    total = 0
    for i in range(50):
        f.readline()
        prob = ''
        for j in range(9):
            prob = prob + f.readline()

        x = Board()
        x.read_text(prob)

        print('{0}) Starting board, {1} unknowns'.format(i, x.unknowns), end=' ')
        res = go(x)

        if res.unknowns == 0:
            print('Solved board')
        
        total = total + res.get_topleft()
    print(total)

if __name__ == '__main__':
    main() 
