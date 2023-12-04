import re


def get_calibration(input_: str) -> list[int]:
    return input_.split('\n')[:-1]


def get_numerical_values(input_: str) -> str:
    return ''.join(re.findall(r'\d+', input_))


def get_two_digit_number(number: str) -> int:
    if len(number) == 1:
        return int(number+number)
    return int(number[0]+number[-1])


def part1(calibrations):
    number_calibrations = []
    for calibration in calibrations:
        string_number = get_numerical_values(calibration)
        two_digit_number = get_two_digit_number(string_number)
        number_calibrations.append(two_digit_number)
    return sum(number_calibrations)


def part2(calibrations):
    return 0


def solution(input_: str) -> tuple[int, int]:
    calibrations = get_calibration(input_)
    return part1(calibrations), part2(calibrations)
