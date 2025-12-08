from typing import List

import tools

TEST = "test.txt"
INPUT = "input.txt"


def part1(file: str) -> int:
    data = tools.read_file_table(file)
    h, w = len(data), len(data[0])
    total: list = [0 if oper == "+" else 1 for oper in data[-1]]

    for y in range(h - 1):
        for x in range(w):
            match data[-1][x]:
                case "*":
                    total[x] *= int(data[y][x])
                case "+":
                    total[x] += int(data[y][x])

    return sum(total)


def part2(file: str) -> int:
    data = tools.read_file_maze(file)
    h, w = len(data), len(data[0])
    operations: List = ''.join(data[-1]).split()
    total: List = [0 if oper == "+" else 1 for oper in operations]
    k: int = 0

    for x in range(w):
        num: int = 0

        for y in range(h - 1):
            if data[y][x] != " ":
                num *= 10
                num += int(data[y][x])

        if num == 0:
            k += 1
            continue

        match operations[k]:
            case "+":
                total[k] += num
            case "*":
                total[k] *= num

    return sum(total)


if __name__ == "__main__":
    print("---------")
    print("TEST")
    print(f"part1 = {part1(TEST)}")
    print(f"part2 = {part2(TEST)}")
    print("---------")
    print("INPUT")
    print(f"part1 = {part1(INPUT)}")
    print(f"part2 = {part2(INPUT)}")
    print("---------")
