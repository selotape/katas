import copy

from attr import attrs, attrib, Factory


@attrs
class Node:
    name = attrib()
    children: list = attrib(default=Factory(list))

    @property
    def children_names(self):
        return (child.name for child in self.children)

    @staticmethod
    def try_merging(node1, node2):
        for a, b in ((node1, node2), (node2, node1)):
            if a.name in b.children_names:
                new_b = copy.deepcopy(b)
                new_a = copy.deepcopy(a)
                new_b.children.append(new_a)
                return new_b
