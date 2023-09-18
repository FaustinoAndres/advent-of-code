def parse_total_calories(input: str) -> list[int]:
    return [sum(map(int, elf.split())) for elf in input.strip().split("\n\n")]


def part1(calories: list[int]) -> int:
    return max(calories)


def part2(calories: list[int]) -> int:
    return sum(sorted(calories, reverse=True)[:3])


def solution(input: str) -> tuple[int, int]:
    calories = parse_total_calories(input)
    return part1(calories), part2(calories)
