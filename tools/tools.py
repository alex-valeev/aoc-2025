from typing import List


def parse_file(path_to_file: str) -> List:
    with open(path_to_file) as f:
        return [line.rstrip('\n') for line in f.readlines()]
