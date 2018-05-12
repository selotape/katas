import sys
from collections import namedtuple

NodeStat = namedtuple("NodeStat", "max_subtree_weight,subtree_weight")


def find_max_subtree_val(root):
    max_subtree_weight, _ = _find_max_subtree_val(root)
    return max_subtree_weight


def _find_max_subtree_val(node):
    if node is None:
        return NodeStat(-sys.maxsize, 0)

    left_stat = _find_max_subtree_val(node.left) #  TODO - makesure left & right are always assigned (even to None)
    right_stat = _find_max_subtree_val(node.right)

    subtree_weight = left_stat.subtree_weight + right_stat.subtree_weight + node.weight
    max_subtree_weight = max(left_stat.max_subtree_weight, right_stat.max_subtree_weight, subtree_weight)
    return NodeStat(max_subtree_weight, subtree_weight)



