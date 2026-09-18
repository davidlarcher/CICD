import pytest

from app.pricing import calculate_price


def test_calculate_price():
    assert calculate_price(100, 3) == 300


def test_quantity_must_be_positive():
    with pytest.raises(ValueError):
        calculate_price(100, 0)