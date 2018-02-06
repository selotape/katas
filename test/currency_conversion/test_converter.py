import pytest

from katas.currency_convertion.converter import Converter


def test_convert():
    converter = Converter()
    ils_100_in_usd = converter.convert('ILS', 340)
    assert 100 == pytest.approx(ils_100_in_usd, abs=10)

    ils_100_in_inr = converter.convert(source_symbol='ILS', amount=100, target_symbol='INR')
    assert 1846 == pytest.approx(ils_100_in_inr, abs=100)

    gbp = converter.convert(source_symbol='GBP', amount=1000, target_symbol='GBP')
    assert 1000 == pytest.approx(gbp, abs=5)
