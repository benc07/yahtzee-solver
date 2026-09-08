def score_upper(dice, face):
    """Add up dice that match the requested face."""
    return sum(die for die in dice if die == face)


def score_ones(dice):
    return score_upper(dice, 1)


def score_twos(dice):
    return score_upper(dice, 2)


def score_threes(dice):
    return score_upper(dice, 3)


def score_fours(dice):
    return score_upper(dice, 4)


def score_fives(dice):
    return score_upper(dice, 5)


def score_sixes(dice):
    return score_upper(dice, 6)