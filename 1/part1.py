def get_numbers(line):
    return [a for a in line if a.isnumeric()]


_input = open("input.txt", "r").read().splitlines()
numbers = [get_numbers(line) for line in _input]

result = 0
for l in numbers:
    result += int(f'{l[0]}{l[-1]}')
print(result)
