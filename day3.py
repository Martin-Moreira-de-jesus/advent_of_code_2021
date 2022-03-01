from typing import List

from utils import get_input

from copy import copy


def part1(data: List[str]) -> int:
    list_size = len(data)

    gamma_rate = ''
    epsilon_rate = ''
    ones = 0
    zeroes = 0
    for i in range(len(data[0])):
        ones = len([number for number in data if number[i] == '1'])
        zeroes = list_size - ones

        if ones > zeroes:
            gamma_rate += '1'
            epsilon_rate += '0'
        else:
            gamma_rate += '0'
            epsilon_rate += '1'

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def part2(data: List[str]) -> int:
    o2_gen_rating = 0
    co2_scrub_rating = 0

    o2_digits = copy(data)
    for i in range(len(data[0])):
        ones = len([number for number in o2_digits if number[i] == '1'])
        zeroes = len(o2_digits) - ones

        if ones >= zeroes:
            o2_digits = [number for number in o2_digits if number[i] == '1']
        else:
            o2_digits = [number for number in o2_digits if number[i] == '0']

        if len(o2_digits) == 1:
            o2_gen_rating = o2_digits[0]

    co2_digits = copy(data)
    for i in range(len(data[0])):
        ones = len([number for number in co2_digits if number[i] == '1'])
        zeroes = len(co2_digits) - ones

        if ones >= zeroes:
            co2_digits = [number for number in co2_digits if number[i] == '0']
        else:
            co2_digits = [number for number in co2_digits if number[i] == '1']

        if len(co2_digits) == 1:
            co2_scrub_rating = co2_digits[0]

    return int(o2_gen_rating, 2) * int(co2_scrub_rating, 2)


values = get_input(3)
print(part1(values))
print(part2(values))
