from app import find_evenly_divisible, is_evenly_divisible


def test_is_evenly_divisible():
    assert(is_evenly_divisible(2520, 10) == True)
    assert(is_evenly_divisible(2521, 10) == False)


def test_find_evenly_divisible():
    assert(find_evenly_divisible(20) == 2520)
