from src.time_range import get_range as rng


def test_no_overlap():
    assert rng([0, 1, 2], [1, 2, 3]) == "No overlap", "Input with no overlap should return [0, 0]"


def test_one_input():
    assert rng([1], [2]) == "Minimum 2 inputs needed", "Input lists must have more than one row"


def test_input_type():
    assert rng(["a", "a"], ["b", "b"]) == "Input float/int data only", "Incorrect handling of strings in input"


def test_input_format():
    assert rng(1, 2) == "Input lists only", "Incorrect handling of strings in input"


def test_input_length():
    assert rng([1, 2], [5, 5, 5]) == "Input lists are not the same length", "Incorrect handling of incorrect input lengths"
