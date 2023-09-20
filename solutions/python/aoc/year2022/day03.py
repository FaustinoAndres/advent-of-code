"""
Day 3: Rucksack Reorganization
"""
from functools import reduce


def get_rucksacks(input_: str) -> list[int]:
    return input_.split('\n')[:-1]


def split_rucksacks(rucksack: str) -> list[str]:
    length = len(rucksack)
    return [rucksack[0:length//2], rucksack[length//2: length]]


def get_coincidence(rucksack: list[str]) -> str:
    item = reduce(lambda a, b: set(list(a)).intersection(set(list(b))), rucksack)
    return list(item)[0]


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
    points = 0
    teams = list(divide_chunks(rucksacks, 3))
    for team in teams:
        item = get_coincidence(team)
        points += get_points(item)
    return points


def divide_chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def solution(input: str) -> tuple[int, int]:
    rucksacks = get_rucksacks(input)
    return part1(rucksacks), part2(rucksacks)
