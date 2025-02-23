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
    factor = 2

    if value < 2:
        factors = []
    elif value < 4:
        factors.append(value)
    else:
        while value != 1:
            if value % factor == 0:
                factors.append(factor)
                value = value / factor
            else:
                factor += 1
    return factors


### TESTS ###
def test_data_type_not_int():
    with pytest.raises(ValueError):
        generate_prime_factors("a")

def test_called_1_expect_empty_list():
    assert generate_prime_factors(1) == []

def test_called_2_expect_list_2():
    assert generate_prime_factors(2) == [2]

def test_called_3_expect_list_3():
    assert generate_prime_factors(3) == [3]

def test_called_4_expect_list_2_2():
    assert generate_prime_factors(4) == [2, 2]

def test_called_6_expect_list_3_2():
    assert generate_prime_factors(6) == [2, 3]

def test_called_8_expect_list_2_2_2():
    assert generate_prime_factors(8) == [2, 2, 2]

def test_called_9_expect_list_3_3():
    assert generate_prime_factors(9) == [3, 3]