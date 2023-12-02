from functools import reduce
from operator import mul


def parse(line):
    _id = line.split(':')[0].split(' ')[1]
    clues = [clue.strip() for clue in line.split(':')[1].split(';')]
    max_count = {}

    for clue in clues:
        cubes = clue.split(', ')
        for cube in cubes:
            number, color = cube.split(' ')
            number = int(number)
            if not max_count.get(color, None) or max_count[color] < number:
                max_count.update({color: number})
    return {'id': int(_id), 'max_count': max_count}


rules = {
    'red': 12,
    'green': 13,
    'blue': 14
}
_input = open('input.txt').read().splitlines()
parsed_lines = [parse(line) for line in _input]

result = 0
for line in parsed_lines:
    _max = line['max_count']
    result += reduce(mul, _max.values())

print(result)
