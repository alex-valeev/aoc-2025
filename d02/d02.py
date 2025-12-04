from tools import read_file_row

TEST = "test.txt"
INPUT = "input.txt"


def part1(file: str) -> int:
    data = read_file_row(file)
    invalid_id: int = 0

    for period in data:
        period_from, period_to = map(int, period.split("-"))

        start = int(10 ** (len(str(period_from)) // 2))
        if len(str(period_from)) % 2 == 1:
            period_from = int(10 ** (len(str(period_from))))
            start *= 10

        end = int(10 ** (len(str(period_to)) // 2))
        if len(str(period_to)) % 2 == 1:
            period_to = int(10 ** (len(str(period_to)) - 1) - 1)

        for i in range(period_from // start, period_to // end + 1, 1):
            current_id = int(str(i) + str(i))
            if int(period_from) <= current_id <= int(period_to):
                invalid_id += current_id

    return invalid_id


def part2(file: str) -> int:
    data = read_file_row(file)
    invalid_id: int = 0

    for period in data:
        period_from, period_to = map(int, period.split("-"))

        for id in range(period_from, period_to + 1):
            id_str = str(id)

            for part in range(1, len(id_str)):
                if len(id_str) % part == 0:
                    if id_str[:part] * (len(id_str) // part) == id_str:
                        invalid_id += id
                        break

    return invalid_id


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
