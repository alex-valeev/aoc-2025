from typing import List
import tools

TEST = "test.txt"
INPUT = "input.txt"


def part1(file: str) -> int:
    data = tools.read_file_maze(file)
    start, splitter = 'S', '^'

    start_position = data[0].index(start)
    tachyon_beams = {start_position}
    total_split: int = 0
    
    for y in range(1, len(data)):
        for x_beam in list(tachyon_beams):
            if data[y][x_beam] == splitter:
                tachyon_beams.add(x_beam - 1)
                tachyon_beams.add(x_beam + 1)
                tachyon_beams.remove(x_beam)

                total_split += 1
                
    return total_split


def part2(file: str) -> int:
    data = tools.read_file_maze(file)
    start, splitter = 'S', '^'

    start_position = data[0].index(start)
    tachyon_beams = {start_position}
    timelines: List = [1 if i == start_position else 0 for i in range(len(data[0]))]

    for y in range(1, len(data)):
        for x_beam in list(tachyon_beams):
            if data[y][x_beam] == splitter:
                tachyon_beams.add(x_beam - 1)
                tachyon_beams.add(x_beam + 1)
                tachyon_beams.remove(x_beam)

                timelines[x_beam - 1] += timelines[x_beam]
                timelines[x_beam + 1] += timelines[x_beam]
                timelines[x_beam] = 0
    
    return sum(timelines)


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
