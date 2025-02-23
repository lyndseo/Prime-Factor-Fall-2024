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


### TESTS ###
def test_data_type_not_int():
    with pytest.raises(ValueError):
        generate_prime_factors("a")


