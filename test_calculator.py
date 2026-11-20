from calculator import calculate_average

def test_normal_average():
    assert calculate_average([10, 20, 30]) == 20


def test_single_number():
    assert calculate_average([10]) == 10


def test_negative_numbers():
    assert calculate_average([-10, -20, -30]) == -20
