import re


def get_numbers(line):
    atoi = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }
    numbers = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
    return [atoi[n] if n in atoi else n for n in numbers]


_input = open("input.txt", "r").read().splitlines()
numbers = [get_numbers(line) for line in _input]

result = 0
for l in numbers:
    result += int(f'{l[0]}{l[-1]}')
print(result)
