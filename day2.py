from typing import List, Dict

from utils import get_input


def part1(data: List[List[str]]) -> int:
    horizontal_pos = 0
    depth = 0
    for command in data:
        if command[0] == 'forward':
            horizontal_pos += int(command[1])
        elif command[0] == 'up':
            depth -= int(command[1])
        else:
            depth += int(command[1])

    return horizontal_pos * depth


def part2(data: List[List[str]]) -> int:
    horizontal_pos = 0
    depth = 0
    aim = 0
    for command in data:
        if command[0] == 'forward':
            horizontal_pos += int(command[1])
            depth += aim * int(command[1])
        elif command[0] == 'up':
            aim -= int(command[1])
        else:
            aim += int(command[1])

    return horizontal_pos * depth


values = [s.split(' ') for s in get_input(2)]
print(part1(values))
print(part2(values))
