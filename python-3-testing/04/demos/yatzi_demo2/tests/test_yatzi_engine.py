import pytest

from yatzi_engine import *


@pytest.mark.parametrize(
    "dice,expected_score",
    [
        ([2, 3, 4, 5, 1], 15),
        ([3, 3, 4, 5, 1], 16),
    ]
)
def test_chance(dice, expected_score):
    assert chance(dice) == expected_score


@pytest.mark.parametrize(
    "dice,expected_score",
    [
        ([4, 4, 4, 4, 4], 50),
        ([6, 6, 6, 6, 6], 50),
        ([6, 6, 6, 6, 3], 0),
    ]
)
def test_yatzi(dice, expected_score):
    assert yatzi(dice) == expected_score


@pytest.mark.parametrize(
    "dice,expected_score",
    [
        ([1, 2, 3, 4, 5], 1),
        ([1, 2, 1, 4, 5], 2),
        ([6, 2, 2, 4, 5], 0),
        ([1, 2, 1, 1, 1], 4),
    ]
)
def test_ones(dice, expected_score):
    assert ones(dice) == expected_score


@pytest.mark.parametrize(
    "dice,expected_score",
    [
        ([1, 2, 3, 2, 6], 4),
        ([2, 2, 2, 2, 2], 10),
    ]
)
def test_twos(dice, expected_score):
    assert twos(dice) == expected_score


@pytest.mark.parametrize(
    "dice,expected_score",
    [
        ([1, 2, 3, 2, 3], 6),
        ([2, 3, 3, 3, 3], 12),
    ]
)
def test_threes(dice, expected_score):
    assert threes(dice) == expected_score


@pytest.mark.parametrize(
    "dice,expected_score",
    [
        ([4, 4, 4, 5, 5], 12),
        ([4, 4, 5, 5, 5], 8),
        ([4, 5, 5, 5, 5], 4),
    ]
)
def test_fours(dice, expected_score):
    assert fours(dice) == expected_score


@pytest.mark.parametrize(
    "dice,expected_score",
    [
        ([4, 4, 4, 5, 5], 10),
        ([4, 4, 5, 5, 5], 15),
        ([4, 5, 5, 5, 5], 20),
    ]
)
def test_fives(dice, expected_score):
    assert fives(dice) == expected_score


@pytest.mark.parametrize(
    "dice,expected_score",
    [
        ([4, 4, 4, 5, 5], 0),
        ([4, 4, 6, 5, 5], 6),
        ([6, 5, 6, 6, 5], 18),
    ]
)
def test_sixes(dice, expected_score):
    assert sixes(dice) == expected_score


@pytest.mark.parametrize(
    "dice,expected_score",
    [
        ([3, 4, 3, 5, 6], 6),
        ([5, 3, 3, 3, 5], 10),
        ([5, 3, 6, 6, 5], 12),
        ([5, 3, 6, 1, 2], 0),
    ]
)
def test_one_pair(dice, expected_score):
    assert pair(dice) == expected_score


@pytest.mark.parametrize(
    "dice,expected_score",
    [
        ([3, 3, 5, 4, 5], 16),
        ([3, 3, 6, 6, 6], 18),
        ([3, 3, 6, 5, 4], 0),
    ]
)
def test_two_pairs(dice, expected_score):
    assert two_pairs(dice) == expected_score


@pytest.mark.parametrize(
    "dice,expected_score",
    [
        ([3, 3, 3, 4, 5], 9),
        ([5, 3, 5, 4, 5], 15),
        ([3, 3, 3, 3, 5], 9),
    ]
)
def test_three_of_a_kind(dice, expected_score):
    assert three_of_a_kind(dice) == expected_score


@pytest.mark.parametrize(
    "dice,expected_score",
    [
        ([3, 3, 3, 3, 5], 12),
        ([5, 5, 5, 4, 5], 20),
        ([3, 3, 3, 3, 3], 12),
        ([3, 3, 3, 2, 1], 0),
    ]
)
def test_four_of_a_kind(dice, expected_score):
    assert four_of_a_kind(dice) == expected_score


@pytest.mark.parametrize(
    "dice,expected_score",
    [
        ([1, 2, 3, 4, 5], 14),
        ([2, 2, 3, 4, 5], 14),
        ([2, 3, 3, 4, 5], 14),
        ([6, 3, 3, 4, 5], 18),
        ([2, 3, 4, 5, 1], 14),
        ([1, 2, 2, 4, 5], 0),
    ]
)
def test_small_straight(dice, expected_score):
    assert small_straight(dice) == expected_score


@pytest.mark.parametrize(
    "dice,expected_score",
    [
        ([6, 2, 3, 4, 5], 20),
        ([2, 3, 4, 5, 6], 20),
        ([1, 2, 3, 4, 5], 15),
        ([2, 3, 4, 5, 1], 15),
        ([1, 2, 2, 4, 5], 0),
    ]
)
def test_large_straight(dice, expected_score):
    assert large_straight(dice) == expected_score


@pytest.mark.parametrize(
    "dice,expected_score",
    [
        ([6, 2, 2, 2, 6], 18),
        ([2, 3, 4, 5, 6], 0),
    ]
)
def test_full_house(dice, expected_score):
    assert full_house(dice) == expected_score


@pytest.mark.parametrize(
    "dice,expected_categories", [
        ((1, 2, 3, 4, 5),
         [(15, 'large_straight'), (15, 'chance'), (14, 'small_straight'), (5, 'fives'), (4, 'fours'), (3, 'threes'),
          (2, 'twos'), (1, 'ones')]),
        ((2, 2, 3, 3, 3),
         [(13, 'full_house'), (13, 'chance'), (10, 'two_pairs'), (9, 'three_of_a_kind'), (9, 'threes'), (4, 'twos')]),
        ((6, 6, 6, 6, 6),
         [(50, 'yatzi'), (30, 'sixes'), (30, 'chance'), (24, 'four_of_a_kind'), (18, 'three_of_a_kind')]),
    ])
def test_scores_in_categories(dice, expected_categories):
    assert [(score, fun.__name__) for (score, fun) in scores_in_categories(dice)] == expected_categories
