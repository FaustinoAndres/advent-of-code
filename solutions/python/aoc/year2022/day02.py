POINTS = {'rock': 1, 'paper': 2, 'scissors': 3}
POINTS_RESULTS = {'lose': 0, 'draw': 3, 'win': 6}
OPPONENT = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
ME = {'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
RESULTS = {'X': 'lose', 'Y': 'draw', 'Z': 'win'}
RELATIONS = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}


def get_key_from_value(d, val):
    keys = [k for k, v in d.items() if v == val]
    if keys:
        return keys[0]
    return None


def get_rounds(input_: str) -> list[tuple[str, str]]:
    return list(map(lambda line: tuple(line.rstrip('\n').split()), input_.split('\n')[:-1]))


def game_1(round_: tuple[str, str]) -> int:

    score = None
    if RELATIONS[ME[round_[1]]] == OPPONENT[round_[0]]:
        score = POINTS_RESULTS['win']
    elif RELATIONS[OPPONENT[round_[0]]] == ME[round_[1]]:
        score = POINTS_RESULTS['lose']
    else:
        score = POINTS_RESULTS['draw']

    return score


def game_2(round_: tuple[str, str]) -> int:
    score = 0
    if round_[1] == 'Y':
        score = POINTS[OPPONENT[round_[0]]]
    elif round_[1] == 'X':
        score = POINTS[RELATIONS[OPPONENT[round_[0]]]]
    else:
        score = POINTS[get_key_from_value(RELATIONS, OPPONENT[round_[0]])]
    return score


def part2(rounds: list[tuple[str, str]]) -> int:
    score = 0
    for round_ in rounds:
        score += POINTS_RESULTS[RESULTS[round_[1]]]
        score += game_2(round_)
    return score


def part1(rounds: list[tuple[str, str]]) -> int:
    score = 0
    for round_ in rounds:
        score += POINTS[ME[round_[1]]]
        score += game_1(round_)
    return score


def solution(input_: str) -> tuple[int, int]:
    rounds = get_rounds(input_)
    return part1(rounds), part2(rounds)
