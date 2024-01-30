import pytest
from main import calculate_mean

def test_calculate_mean():
    data = [1, 2, 3, 4, 5]
    assert calculate_mean(data) == 3

def test_calculate_mean_with_empty_list():
    data = []
    with pytest.raises(ZeroDivisionError):
        calculate_mean(data)
