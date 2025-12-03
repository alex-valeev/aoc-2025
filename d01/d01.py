from tools import parse_file

TEST = "test.txt"
INPUT = "input.txt"


def part1(file: str) -> int:
    data = parse_file(file)
    position: int = 50
    password: int = 0

    for action in data:
        match (action[0]):
            case "L":
                position -= int(action[1:]) % 100
            case "R":
                position += int(action[1:]) % 100

        if position < 0:
            position += 100
        elif position >= 100:
            position -= 100

        if position == 0:
            password += 1

    return password


def part2(file: str) -> int:
    data = parse_file(file)
    position: int = 50
    password: int = 0
    prev_pos: int = 50

    for action in data:
        password += int(action[1:]) // 100

        match (action[0]):
            case "L":
                position -= int(action[1:]) % 100
            case "R":
                position += int(action[1:]) % 100

        if position <= -100:
            position += 100
            password += 1

        elif position >= 100:
            position -= 100
            password += 1

        elif position == 0:
            password += 1

        if position > 0 > prev_pos or position < 0 < prev_pos:
            password += 1

        prev_pos = position

    return password


if __name__ == "__main__":
    print("---------")
    print("TEST DATA")
    print(f"part1 = {part1(TEST)}")
    print(f"part2 = {part2(TEST)}")
    print("---------")
    print("INPUT DATA")
    print(f"part1 = {part1(INPUT)}")
    print(f"part2 = {part2(INPUT)}")
    print("---------")