from typing import List

from utils import get_input


def part1(data: List[int]) -> int:
    increases = 0

    for i in range(1, len(data)):
        if data[i - 1] < data[i]:
            increases += 1

    return increases


def part2(data: List[int]) -> int:
    increases = 0

    previous = data[0] + data[1] + data[2]
    for i in range(len(data) - 2):
        current = data[i] + data[i + 1] + data[i + 2]
        if previous < current:
            increases += 1

        previous = current

    return increases


values = [int(s) for s in get_input(1)]
print(part1(values))
print(part2(values))
