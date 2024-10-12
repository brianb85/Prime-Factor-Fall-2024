import pytest
import prime


def test_step1_datatype():
    with pytest.raises(ValueError):
        prime.generate_prime_factors("Testing")

def test_step2_one():
    assert prime.generate_prime_factors(1) == []

def test_step3_two():
    assert prime.generate_prime_factors(2) == [2]

def test_step4_three():
    assert prime.generate_prime_factors(3) == [3]
