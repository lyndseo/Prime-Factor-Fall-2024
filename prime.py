"""
Lyndsay Walker
prime.py -- Write the application code here
"""
import pytest

def generate_prime_factors(value):
    try:
        value = int(value)
    except ValueError:
        raise ValueError("value must be an integer")

    factors = []
    if value < 2:
        factors = []
    else:
        factors.append(value)
    return factors

### TESTS ###
def test_data_type_not_int():
    with pytest.raises(ValueError):
        generate_prime_factors("a")

def test_called_1_expect_empty_list():
    assert generate_prime_factors(1) == []

def test_called_2_expect_list_2():
    assert generate_prime_factors(2) == [2]