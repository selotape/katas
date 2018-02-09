from itertools import chain


def n_queens(n):
    boards = chain(*(n_queens_req([i], n) for i in range(1, n + 1)))
    return sorted(list(boards))


def n_queens_req(prev, n):
    if len(prev) == n:
        return [prev]
    legal_placements = list(legal_next_placements(prev, n))
    if len(legal_placements) == 0:
        return []
    else:
        return chain(*(n_queens_req(prev + [placement], n) for placement in legal_placements))


def legal_next_placements(prev, n):
    possible_placements = set(range(1, n + 1))
    possible_placements -= set(prev)
    next_pos = len(prev) + 1
    for col, row in enumerate(prev, start=1):
        dist = next_pos - col
        illegal_rows = {row + dist, row - dist}
        possible_placements -= illegal_rows
    return possible_placements
