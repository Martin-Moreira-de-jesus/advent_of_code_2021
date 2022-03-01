def get_input(day):
    with open(f'inputs/input_day{day}.txt') as file:
        return [s.replace('\n', '') for s in file.readlines()]
