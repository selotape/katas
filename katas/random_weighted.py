from collections import OrderedDict
from itertools import accumulate
from random import random


class RandomWeighted:
    def __init__(self, items, weights):
        total_weight = sum(weights)
        normalized_weights = [w / total_weight for w in weights]
        cum_weights = accumulate(normalized_weights)
        self.items = OrderedDict(zip(cum_weights, items))

    def get(self):
        draw = random()
        for range_top, item in self.items.items():
            if draw < range_top:
                return item
