from itertools import combinations_with_replacement, chain


def subset_sum_mem(arr, target, mem):
    key = (tuple(arr), target)
    if key in mem:
        return mem[key]
    if target == 0:
        return [[]]
    if target < 0 or len(arr) == 0:
        return []
    first = arr[0]
    with_first = [sorted([first] + subset) for subset in subset_sum_mem(arr[1:], target - first, mem)]
    wo_first = subset_sum_mem(arr[1:], target, mem)
    subsets = with_first + wo_first
    mem[key] = subsets
    return subsets


def subsets_sum(arr, target):
    mem = {}
    solutions_with_dups = subset_sum_mem(arr, target, mem)
    solutions = {tuple(solution) for solution in solutions_with_dups}
    return sorted(list(solution) for solution in solutions)


def combination_sum(a, sum_):
    unique_values = set(a)
    all_combinations = chain.from_iterable(combinations_with_replacement(unique_values, i) for i in range(sum_ + 1))
    valid_combinations = [sorted(combination) for combination in all_combinations if sum(combination) == sum_]
    if len(valid_combinations) == 0:
        return 'Empty'
    else:
        return join_combinations(sorted(valid_combinations))


def join_combinations(combinations):
    printable_combinations = (printable_combination(combination) for combination in combinations)
    return ''.join(printable_combinations)


def printable_combination(combination):
    joined = ' '.join(str(item) for item in combination)
    return f'({joined})'
