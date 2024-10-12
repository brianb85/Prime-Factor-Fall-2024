import pytest
import prime


def test_datatype():
    with pytest.raises(ValueError):
        prime.generate_prime_factors("Testing")
