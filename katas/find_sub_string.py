from itertools import groupby


def findSubstrings(words, parts):
    parts = sorted(parts, key=len, reverse=True)
    grouped_parts = {i: list(group) for i, group in groupby(parts, key=len)}
    print(f"grouped_parts: {grouped_parts}")
    return [findWordSubstrings(word, grouped_parts) for word in words]


def findWordSubstrings(word, sorted_grouped_parts):
    for _, parts in sorted_grouped_parts.items():
        part = find_min_index_part(word, parts)
        if part:
            return word.replace(part, '[%s]' % part, 1)
    return word


def find_min_index_part(word, parts):
    parts_in = (part for part in parts if part in word)

    def part_index(part):
        return word.index(part)

    return min(parts_in, key=part_index, default=None)


words = ["Aaaaaaaaa",
         "bcdEFGh"]
parts = ["aaaaa",
         "Aaaa",
         "E",
         "z",
         "Zzzzz"]

# parts_grouped = list(groupby(sorted(parts, key=len) , key=len))
# for i, grouper in parts_grouped:
#     grouper_l = list(grouper)
#     print(f"i:{i}, grouper:{grouper_l}")
#


print(findSubstrings(words, parts))
