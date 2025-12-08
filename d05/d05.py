from typing import List, Tuple
import tools

TEST = "test.txt"
INPUT = "input.txt"


def part1(file: str) -> int:
    data = tools.read_file_column(file)
    fresh_diap, all_id = prepare_data(data)
    fresh_ingredient: int = 0

    for id in all_id:
        for fresh in fresh_diap:
            if fresh[0] <= id <= fresh[1]:
                fresh_ingredient += 1
                break

    return fresh_ingredient


def part2(file: str) -> int:
    data = tools.read_file_column(file)
    fresh_diap, _ = prepare_data(data)
    fresh_ingredient: int = 0
    segments: List = [fresh_diap[0]]

    for diap in fresh_diap:
        if segments[-1][1] >= diap[0]:
            segments[-1][1] = max(segments[-1][1], diap[1])
        else:
            segments.append(diap)

    for seg in segments:
        fresh_ingredient += seg[1] - seg[0] + 1

    return fresh_ingredient


def prepare_data(raw: List[str]) -> (List[Tuple[int]], List[int]):
    empty: str = ""

    empty_idx = raw.index(empty)
    fresh_id = sorted(list(map(int, el.split('-'))) for el in raw[:empty_idx])
    id_list = list(map(int, raw[empty_idx+1:]))

    return fresh_id, id_list


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
