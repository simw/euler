
from euler96 import transform_coords
from euler96 import Board

def test(ver):
    board = Board()
    for i in range(1,10):
        for j in range(1,10):
            board.set_value(i, j, transform_coords(i-1, j-1, ver), False)

    print('From external to {0}'.format(ver))
    board.print_board()
    print('')

    for i in range(1,10):
        for j in range(1,10):
            coords = board.get_value(i, j, False)
            board.set_value(i, j, transform_coords(coords[0], coords[1], ver), False)

    print('Back to external')
    board.print_board()
    print('')



if __name__ == '__main__':
    test('row')
    print('')
    test('column')
    print('')
    test('square')
