"""
Day 4: Camp Cleanup
"""


def get_pairs(input_: str) -> list[int]:
    return input_.split('\n')[:-1]


def get_assignments(assignment_range: str) -> set[int]:
    assignments = list(map(lambda x: int(x), assignment_range.split('-')))
    return set(range(assignments[0], assignments[1] + 1))


def get_team_assignments(pair: str) -> tuple[str]:
    team_assignments = pair.split(',')
    return team_assignments[0], team_assignments[1]


def fully_contains(pair: str) -> bool:
    elf_1, elf_2 = get_team_assignments(pair)
    elf_1_assignments = get_assignments(elf_1)
    elf_2_assignments = get_assignments(elf_2)
    return elf_1_assignments.issubset(elf_2_assignments) or elf_2_assignments.issubset(elf_1_assignments)


def union(pair: str) -> bool:
    elf_1, elf_2 = get_team_assignments(pair)
    elf_1_assignments = get_assignments(elf_1)
    elf_2_assignments = get_assignments(elf_2)
    return len(elf_1_assignments.intersection(elf_2_assignments)) > 0


def part1(pairs: list[str]) -> int:
    total = 0
    for pair in pairs:
        total += fully_contains(pair)
    return total


def part2(pairs: list[str]) -> int:
    total = 0
    for pair in pairs:
        total += union(pair)
    return total


def solution(input_: str) -> tuple[int, int]:
    pairs = get_pairs(input_)
    return part1(pairs), part2(pairs)
