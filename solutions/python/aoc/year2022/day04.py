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


def fully_contains(pair: str) -> int:
    elf_1, elf_2 = get_team_assignments(pair)
    elf_1_assignments = get_assignments(elf_1)
    elf_2_assignments = get_assignments(elf_2)
    total_assignments = elf_1_assignments.union(elf_2_assignments)
    return int(len(total_assignments) == len(elf_1_assignments) or len(total_assignments) == len(elf_2_assignments))


def part1(pairs: list[str]) -> int:
    total = 0
    for pair in pairs:
        total += fully_contains(pair)
    return total


def part2(pairs: list[str]) -> int:
    return 0


def solution(input_: str) -> tuple[int, int]:
    pairs = get_pairs(input_)
    return part1(pairs), part2(pairs)
