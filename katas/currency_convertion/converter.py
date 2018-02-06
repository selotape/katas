# class converter:
#
#     def __init__(self):
#         self._fixer_oi
#
#     def
#
#
import string
import sys
from collections import defaultdict
from itertools import combinations_with_replacement, chain

import requests


def _rates_from_api_fixer(base_symbol):
    try:
        return requests.get('https://api.fixer.io/latest', params={'base': base_symbol}).json()['rates']
    except:
        return {}


class Converter(object):

    def __init__(self):
        self.rates = defaultdict(dict)
        self.rates['USD'] = _rates_from_api_fixer('USD')
        self.rates['USD']['USD'] = 1.0
        self.rates['EUR'] = _rates_from_api_fixer('EUR')
        self.rates['EUR']['EUR'] = 1.0
        self.supported_pairs = combinations_with_replacement(chain(self.rates['USD'].keys(), self.rates['EUR'].keys()), 2)

        for source, target in self.supported_pairs:
            for source_base, target_base in (('USD', 'EUR'), ('EUR', 'USD'), ('EUR', 'EUR'), ('USD', 'USD'),):

                if source in self.rates[source_base] and target in self.rates[target_base]:
                    source_to_source_base_ratio = 1 / self.rates[source_base][source]
                    source_to_target_base_ratio = source_to_source_base_ratio * self.rates[source_base][target_base]
                    source_to_target_ratio = source_to_target_base_ratio * self.rates[target_base][target]
                    self.rates[source][target] = source_to_target_ratio
                    self.rates[target][source] = 1.0 / source_to_target_ratio

    def convert(self, source_symbol: string, amount: float, target_symbol='USD'):
        return amount * self.rates[source_symbol][target_symbol]


def convert_file(file_path):
    converter = Converter()
    with open(file_path) as currencies:
        for i, line in enumerate(currencies):
            try:
                amount, symbol = line.strip().split(',')
                amount_in_usd = converter.convert(symbol, float(amount))
                print(amount_in_usd)
            except Exception as e:
                print(f'failed converting currency at line {i}. error: {str(e)}', file=sys.stderr)


if __name__ == '__main__':
    convert_file('/home/ron/dev/deployer/private/katas/currency_convertion/sample_monies.txt')
