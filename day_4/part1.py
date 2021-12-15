from collections import Counter
from math import floor

def binary_search_set(draw, board):
    if not board:
        return

    if len(board) == 1:
        if board[0]['draw'] == draw:
            board[0]['selected'] = True
        return

    middle = floor(len(board)/2)

    if board[middle]['draw'] == draw:
        board[middle]['selected'] = True
        return
    
    if draw < board[middle]['draw']:
        left = board[:middle]
        return binary_search_set(draw, left)
    
    if draw > board[middle]['draw']:
        right = board[middle:]
        return binary_search_set(draw, right)


def generate_boards(f):
    boards = []
    f.readline()
    board = []
    row = 0
    for line in f.readlines():
        line = line.strip()
        if line:
            # We are generating a new board
            index = 0
            for item in line.split(' '):
                if item.strip():
                    board.append({'draw': int(item), 'selected': False, 'index': index, 'row': row})
                    index += 1
            row += 1
        else:
            # Ensure this is sorted in order for the binary search set method
            board = sorted(board, key=lambda item: item['draw'])
            boards.append(board)
            board = []
            row = 0
    boards.append(board)
    return boards


def scan_board(board):
    for row in range(5):
        items = [item for item in board if item['row'] == row]
        result = all(item['selected'] == True for item in items)
        if result: return result

    for col in range(5):
        items = [item for item in board if item['index'] == col]
        result = all(item['selected'] == True for item in items)
        if result: return result


if __name__ == '__main__':
    with open('./sample.txt') as f:
        bingo_sequence = f.readline().rstrip('\n').split(',')
        bingo_sequence = [int(item) for item in bingo_sequence]
        
        boards = generate_boards(f)
        result = None
        for draw in bingo_sequence:
            for index, board in enumerate(boards):
                binary_search_set(draw, board)
                result = scan_board(board)
                if result:
                    # compute the sum of all squares in the thing
                    board_sum = sum(item['draw'] for item in board if item['selected'] == False)
                    result = board_sum * draw
                    break

            if result: break
            # Scan the boards for a winning sequence (row or column only)   
        print(result)