from typing import List, Union, Tuple, Any, Dict

from utils import get_input


def show_boards(boards) -> None:
    for board in boards:
        for i in range(5):
            print(board['data'][i], ' ', board['valid_data'][i])
        print()


def get_numbers_and_board(data: List[str]) -> Tuple:
    numbers_called = [int(s) for s in data[0].split(',')]

    data = data[2:]

    board_list = []
    temp_board = []
    for entry in data:
        if entry == '':
            board_list.append({'data': temp_board, 'valid_data': [[0 for i in range(5)] for i in range(5)]})
            temp_board = []
        else:
            temp_board.append([int(s) for s in entry.split()])

    board_list.append({'data': temp_board, 'valid_data': [[0 for i in range(5)] for i in range(5)]})

    return numbers_called, board_list


def check_for_number(board, number: int) -> None:
    for i in range(5):
        for j in range(5):
            if board['data'][i][j] == number:
                board['valid_data'][i][j] = 1
                return


def bingo(board) -> bool:
    for i in range(5):
        for j in range(5):
            if board['valid_data'][i][j] == 0:
                break
            if j == 4:
                return True

    for i in range(5):
        for j in range(5):
            if board['valid_data'][j][i] == 0:
                break
            if j == 4:
                return True

    return False


def part1(numbers: List[int], boards):
    for number in numbers:
        for board in boards:
            check_for_number(board, number)

            if bingo(board):
                return board, number


lines = get_input(4)
numbers, boards = get_numbers_and_board(lines)
show_boards(boards)
winning_board, number = part1(numbers, boards)
show_boards([winning_board])
print(number)
