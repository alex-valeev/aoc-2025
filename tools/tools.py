from time import time
from typing import List


def read_file_column(path_to_file: str) -> List:
    with open(path_to_file) as f:
        return [line.rstrip('\n') for line in f.readlines()]


def read_file_row(path_to_file: str) -> List:
    with open(path_to_file) as f:
        return [line.rstrip('\n').split(',') for line in f.readlines()][0]


def read_file_maze(path_to_file: str) -> List:
    with open(path_to_file) as f:
        return [list(line.rstrip('\n')) for line in f.readlines()]


def read_file_table(path_to_file: str) -> List:
    with open(path_to_file) as f:
        return [list(line.rstrip('\n').split()) for line in f.readlines()]


def duration(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f' ↓ func "{func.__name__}" run {(t2 - t1).__round__(3)} sec')
        return result

    return wrapper
