"""
Day 3: Rucksack Reorganization
"""


def get_rucksacks(input_: str) -> list[int]:
    return input_.split('\n')[:-1]


def split_rucksacks(rucksack: str) -> list[str]:
    length = len(rucksack)
    return [rucksack[0:length//2], rucksack[length//2: length]]


def get_coincidence(rucksack: list[str]) -> str:
    a = set(list(rucksack[0]))
    b = set(list(rucksack[1]))
    return list(a.intersection(b))[0]


def get_points(item: str) -> int:
    if 'a' <= item <= 'z':
        point = ord(item) - ord("a") + 1
    elif 'A' <= item <= 'Z':
        point = ord(item) - ord("A") + 27
    else:
        raise ValueError
    return point


def part1(rucksacks: list[str]) -> int:
    points = 0
    for rucksack in rucksacks:
        pockets = split_rucksacks(rucksack)
        item = get_coincidence(pockets)
        points += get_points(item)
    return points


def part2(rucksacks: list[str]) -> int:
    return 0


def solution(input: str) -> tuple[int, int]:
    rucksacks = get_rucksacks(input)
    return part1(rucksacks), part2(rucksacks)
