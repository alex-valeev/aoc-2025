from typing import List
from tools import read_file_labyrinth

TEST = 'test.txt'
INPUT = 'input.txt'
PAPER = '@'
SPACE = '.'
REMOVED = '+'
MAX_ROLLS = 4


def part1(file: str) -> int:
    data = read_file_labyrinth(file)
    h: int = len(data)
    w: int = len(data[0])
    rolls_of_paper: int = 0

    for y in range(h):
        for x in range(w):
            if data[y][x] == PAPER and roll_access(data=data, x_point=x, y_point=y):
                rolls_of_paper += 1

    return rolls_of_paper


def part2(file: str) -> int:
    data = read_file_labyrinth(file)
    h: int = len(data)
    w: int = len(data[0])
    rolls_of_paper: int = 0
    prev_step_rolls: int = -1

    while prev_step_rolls < rolls_of_paper:
        prev_step_rolls = rolls_of_paper

        for y in range(h):
            for x in range(w):
                if data[y][x] == PAPER and roll_access(data=data, x_point=x, y_point=y):
                    rolls_of_paper += 1
                    data[y][x] = REMOVED

        clear_space(data)

    return rolls_of_paper


def clear_space(data: List[List[str]]):
    h: int = len(data)
    w: int = len(data[0])

    for y in range(h):
        for x in range(w):
            if data[y][x] == REMOVED:
                data[y][x] = SPACE

    return


def roll_access(data: List[List[str]], x_point: int, y_point: int) -> bool:
    rolls = 0
    h: int = len(data)
    w: int = len(data[0])

    for y in range(max(0, y_point - 1), min(y_point + 2, h)):
        for x in range(max(0, x_point - 1), min(x_point + 2, w)):
            if data[y][x] != SPACE:
                rolls += 1

    if rolls - 1 < MAX_ROLLS:
        return True

    return False


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
