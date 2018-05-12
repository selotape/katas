import bisect
from collections import defaultdict


def catalog_update(catalog_list, updates_list):
    catalog = defaultdict(list, )
    catalog.update({l[0]: l[1:] for l in catalog_list})
    for u in updates_list:
        category = u[0]
        updates = u[1:]
        existing = catalog[category]
        for update in updates:
            bisect.insort(existing, update)

    return sorted([cat] + cats for cat, cats in catalog.items())

from functools import partial
from itertools import combinations
from itertools import chain

def minimal_basket_price(maxPrice, vendorsDelivery, vendorsProducts):
    vendor_ids = range(len(vendorsDelivery))
    all_possibilities = chain.from_iterable(combinations(vendor_ids, i) for i in range(len(vendorsDelivery)))
    sell_all_possibilities = [possibility for possibility in all_possibilities if all_items_are_sold(possibility, vendorsProducts)]
    below_price_possibility = [possibility for possibility in sell_all_possibilities if best_price(possibility, vendorsProducts) <= maxPrice]

    def delivery_time(seller_ids, delivery_times):
        return max(delivery_times[seller] for seller in seller_ids)

    delivery_time = partial(delivery_time, delivery_time=vendorsDelivery)
    return min(below_price_possibility, key=delivery_time)


def all_items_are_sold(seller_ids, all_sellers):
    item_ids = range(len(all_sellers[0]))
    relevant_sellers = {all_sellers[seller_id] for seller_id in seller_ids}
    return all(item_is_sold(item, relevant_sellers) for item in item_ids)


def item_is_sold(item, relevant_sellers):
    return any(seller[item] >= 0 for seller in relevant_sellers)


def best_price(seller_ids, all_sellers):
    item_ids = range(len(all_sellers[0]))
    relevant_sellers = {all_sellers[seller_id] for seller_id in seller_ids}
    price = 0
    for item in item_ids:
        prices = (seller[item] for seller in relevant_sellers if seller[item] >= 0)
        price += min(prices)
    return price
