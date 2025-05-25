def dice_counts(dice):
    """
    Make a dictionary of how many of each value are in the dice
    """
    return {x: dice.count(x) for x in range(1, 6)}


def full_house(dice):
    """
    Score the given roll in the 'Full House' category
    """
    counts = dice_counts(dice)
    if 2 in counts.values() and 3 in counts.values():
        return sum(dice)
    return 0
