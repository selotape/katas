from collections import defaultdict
from itertools import chain
from collections import deque

def swap_lexical_order(str_, swappable_pairs):
    equivalence_groups = create_equivalence_groups(swappable_pairs)
    print(equivalence_groups)
    str_mapping = dict(enumerate(str_))
    for group in equivalence_groups:
        chars = sorted([str_[i] for i in group], reverse=True)
        positions = sorted(group)
        for i, c in zip(positions, chars):
            str_mapping[i] = c

    result = ""
    for _, c in str_mapping.items():
        result += c

    return result


def bfs(item, reachable):
    pass


def create_equivalence_groups(pairs):
    reachable = defaultdict(set)
    for a,b in pairs:
        reachable[a].add(b)
        reachable[b].add(a)

    all_items = set(chain(pairs))
    remaining_items = all_items.copy()
    groups = []
    while remaining_items:
        item = remaining_items.pop()
        g = set(bfs(item, reachable))
        groups.append(g)
        remaining_items -= g

    return g


def bfs(item, reachable):
    yield item
    visited = {item}
    stack = deque(reachable[item])

    while stack:
        to_visit = stack.pop()
        if to_visit in visited:
            continue
        yield to_visit
        visited.add(to_visit)
        for i in reachable[to_visit]:
            if i not in visited:
                stack.append(i)


#
# def create_equivalence_groups(pairs):
#     eq_groups = sorted([{a - 1, b - 1} for a, b in pairs])
#     for i in range(len(eq_groups)):
#         merged_groups = _single_merge(eq_groups)
#         if len(eq_groups) == len(merged_groups):
#             break
#         eq_groups = merged_groups
#     return eq_groups
#
#
# def _single_merge(eq_groups):
#     merged = []
#     for g in eq_groups:
#         for m in merged:
#             if g & m:
#                 m |= g
#                 break
#         else:
#             merged.append(g)
#     return merged
