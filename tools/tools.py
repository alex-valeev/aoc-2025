from typing import List


def read_file_column(path_to_file: str) -> List:
    with open(path_to_file) as f:
        return [line.rstrip('\n') for line in f.readlines()]


def read_file_row(path_to_file: str) -> List:
    with open(path_to_file) as f:
        return [line.rstrip('\n').split(',') for line in f.readlines()][0]
