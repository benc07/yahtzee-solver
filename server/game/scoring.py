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


def score_three_of_a_kind(dice):
    if any(dice.count(face) >= 3 for face in range(1, 7)):
        return sum(dice)
    return 0


def score_four_of_a_kind(dice):
    if any(dice.count(face) >= 4 for face in range(1, 7)):
        return sum(dice)
    return 0


def score_full_house(dice):
    counts = sorted(dice.count(face) for face in set(dice))
    return 25 if counts == [2, 3] else 0


def score_small_straight(dice):
    faces = set(dice)
    straights = [
        {1, 2, 3, 4},
        {2, 3, 4, 5},
        {3, 4, 5, 6},
    ]
    return 30 if any(straight.issubset(faces) for straight in straights) else 0


def score_large_straight(dice):
    faces = set(dice)
    return 40 if faces == {1, 2, 3, 4, 5} or faces == {2, 3, 4, 5, 6} else 0


def score_yahtzee(dice):
    return 50 if len(set(dice)) == 1 else 0


def score_chance(dice):
    return sum(dice)

SCORERS = {
    "ones": score_ones,
    "twos": score_twos,
    "threes": score_threes,
    "fours": score_fours,
    "fives": score_fives,
    "sixes": score_sixes,
    "three_of_a_kind": score_three_of_a_kind,
    "four_of_a_kind": score_four_of_a_kind,
    "full_house": score_full_house,
    "small_straight": score_small_straight,
    "large_straight": score_large_straight,
    "yahtzee": score_yahtzee,
    "chance": score_chance,
}


def validate_dice(dice):
    if not isinstance(dice, (list, tuple)):
        raise ValueError("Dice must be a list or tuple")

    if len(dice) != 5:
        raise ValueError("Exactly five dice are required")

    if any(type(die) is not int or not 1 <= die <= 6 for die in dice):
        raise ValueError("Each die must be an integer from 1 to 6")
    

def score_category(dice, category):
    validate_dice(dice)

    if category not in SCORERS:
        raise ValueError(f"Unknown category: {category}")

    return SCORERS[category](dice)