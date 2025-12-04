from tools import read_file_column

TEST = 'test.txt'
INPUT = 'input.txt'


def part1(file: str) -> int:
    data = read_file_column(file)
    batteries = 2

    return sum(find_max_num(row, batteries) for row in data)


def part2(file: str) -> int:
    data = read_file_column(file)
    batteries = 12

    return sum(find_max_num(row, batteries) for row in data)


def find_max_num(bank: str, radix: int) -> int:
    joltage: list = [''] * radix
    idx: int = -1

    for b in range(len(joltage)):
        for i in range(idx + 1, len(bank) - len(joltage) + b + 1):
            if bank[i] > joltage[b]:
                joltage[b] = bank[i]
                idx = i

    return int(''.join(joltage))


if __name__ == '__main__':
    print("---------")
    print("TEST")
    print(f"part1 = {part1(TEST)}")
    print(f"part2 = {part2(TEST)}")
    print("---------")
    print("INPUT")
    print(f"part1 = {part1(INPUT)}")
    print(f"part2 = {part2(INPUT)}")
    print("---------")
