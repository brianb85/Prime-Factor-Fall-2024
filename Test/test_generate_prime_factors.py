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


def test_step5_four():
    assert prime.generate_prime_factors(4) == [2, 2]


def test_step6_six():
    assert prime.generate_prime_factors(6) == [2, 3]


def test_step7_eight():
    assert prime.generate_prime_factors(8) == [2, 2, 2]


def test_step8_nine():
    assert prime.generate_prime_factors(9) == [3, 3]

def test_step9_850():
    assert prime.generate_prime_factors(850) == [2, 5, 5, 17]
