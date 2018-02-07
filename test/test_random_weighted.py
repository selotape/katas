from collections import Counter
from katas.random_weighted import RandomWeighted
from pytest import approx

sample_weights = [0.2, 0.3, 0.4, 0.1]
sample_items = ['north', 'south', 'east', 'west']


def test_random_weighted():
    random_weighted = RandomWeighted(sample_items, sample_weights)
    num_samples = 100000
    samples = (random_weighted.get() for _ in range(num_samples))
    ctr = Counter(samples)
    for item, weight in zip(sample_items, sample_weights):
        assert weight == approx(ctr[item] / num_samples, rel=0.1)
