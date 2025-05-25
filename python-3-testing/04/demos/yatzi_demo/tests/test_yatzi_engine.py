import pytest

from yatzi_engine import full_house


@pytest.mark.parametrize(
    "dice,expected_score",
    [
        ([1, 1, 2, 2, 2], 8),
        ([5, 5, 6, 6, 6], 28),
    ]
)
def test_full_house(dice, expected_score):
    assert full_house(dice) == expected_score
