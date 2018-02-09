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
