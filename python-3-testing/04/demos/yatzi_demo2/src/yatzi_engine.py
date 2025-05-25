from operator import itemgetter


def chance(dice):
    """
    Score the given role in the 'Chance' Yatzy category
    """
    return sum(dice)


def yatzi(dice):
    """
    Score the given roll in the 'Yatzi' category
    """
    counts = dice_counts(dice)
    if 5 in counts.values():
        return 50
    return 0


def small_straight(dice):
    """
    Score the given roll in the 'Small Straight' Yatzy category.
    """
    all_small_straights = {(3, 4, 5, 6): 18, (1, 2, 3, 4): 10, (2, 3, 4, 5): 14}
    dice_as_set = set(dice)
    matches = [score for st, score in all_small_straights.items() if set(st).issubset(dice_as_set)]
    if matches:
        return max(matches)
    else:
        return 0


def large_straight(dice):
    """
    Score the given roll in the 'Large Straight' Yatzy category.
    """
    if sorted(dice) == [2, 3, 4, 5, 6] or sorted(dice) == [1, 2, 3, 4, 5]:
        return sum(dice)
    else:
        return 0


def pair(dice):
    """
    Score the given roll in the 'Pair' category.
    It uses the highest scoring pair if there is more than one pair.
    """
    counts = dice_counts(dice)
    for i in reversed(all_dice_values()):
        if counts[i] >= 2:
            return 2 * i
    return 0


def three_of_a_kind(dice):
    """
    Score the given roll in the 'Three of a kind' category
    """
    counts = dice_counts(dice)
    for i in all_dice_values():
        if counts[i] >= 3:
            return 3 * i
    return 0


def four_of_a_kind(dice):
    """
    Score the given roll in the 'Four of a kind' category
    """
    counts = dice_counts(dice)
    for i in all_dice_values():
        if counts[i] >= 4:
            return 4 * i
    return 0


def two_pairs(dice):
    """
    Score the given roll in the 'Two Pairs' category.

    The score is calculated as the sum of all the dice
    belonging to the two pairs.
    """
    counts = dice_counts(dice)
    pairs = []
    for i in all_dice_values():
        if counts[i] >= 2:
            pairs.append(i)
    if len(pairs) == 2:
        return pairs[0] * 2 + pairs[1] * 2
    return 0


def full_house(dice):
    """
    Score the given roll in the 'Full House' category
    """

    counts = dice_counts(dice)
    if 2 in counts.values() and 3 in counts.values():
        return sum(dice)
    return 0


def ones(dice):
    """
    Score the given roll in the 'Ones' category
    """
    return dice_counts(dice)[1]


def twos(dice):
    """
    Score the given roll in the 'Twos' category
    """
    return dice_counts(dice)[2] * 2


def threes(dice):
    """
    Score the given roll in the 'Threes' category
    """
    return dice_counts(dice)[3] * 3


def fours(dice):
    """
    Score the given roll in the 'Fours' category
    """
    return dice_counts(dice)[4] * 4


def fives(dice):
    """
    Score the given roll in the 'Fives' category
    """
    return dice_counts(dice)[5] * 5


def sixes(dice):
    """
    Score the given roll in the 'Sixes' category
    """
    return dice_counts(dice)[6] * 6


def dice_counts(dice):
    """
    Make a dictionary of how many of each value are in the dice.
    This function accepts collections containing integers.
    """
    return {x: dice.count(x) for x in all_dice_values()}


def all_dice_values():
    """
    Return a list of all possible dice values
    """
    return range(1, 7) #[6, 5, 4, 3, 2, 1]


def scores_in_categories(dice, categories=(yatzi, full_house, four_of_a_kind, three_of_a_kind, two_pairs,
                                           small_straight, large_straight,
                                           ones, twos, threes, fours, fives, sixes,
                                           chance)):
    """
    Score the dice in each category and return those with a non-zero score.
    """
    scores = [(category(dice), category)
              for category in categories]
    non_zero_scores = [(score, category) for (score, category) in scores if score > 0]
    return sorted(non_zero_scores, reverse=True, key=itemgetter(0))
