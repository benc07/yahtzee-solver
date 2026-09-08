import random
from .constants import CATEGORIES
from .scoring import score_category


class YahtzeeGame:
    def __init__(self):
        self.dice = [0, 0, 0, 0, 0]
        self.rolls_left = 3
        self.scorecard = {}

    def roll(self, keep=None):
        if len(self.scorecard) == len(CATEGORIES):
            raise ValueError("The game is over")
        
        if self.rolls_left <= 0:
            raise ValueError("No rolls left this turn")

        if keep is None:
            keep = [False] * 5

        if (
            not isinstance(keep, (list, tuple))
            or len(keep) != 5
            or any(type(held) is not bool for held in keep)
        ):
            raise ValueError("Keep must contain five boolean values")

        if self.rolls_left == 3 and any(keep):
            raise ValueError("Cannot hold dice before the first roll")

        self.dice = [
            die if held else random.randint(1, 6)
            for die, held in zip(self.dice, keep)
        ]
        self.rolls_left -= 1

        return self.dice.copy()

    def score(self, category):
        if category in self.scorecard:
            raise ValueError("This category has already been used")

        if self.rolls_left == 3:
            raise ValueError("Roll the dice before scoring")

        points = score_category(self.dice, category)
        self.scorecard[category] = points

        self.dice = [0, 0, 0, 0, 0]
        self.rolls_left = 3

        return points

    def upper_score(self):
        upper_categories = (
            "ones", "twos", "threes", "fours", "fives", "sixes"
        )
        return sum(
            self.scorecard.get(category, 0)
            for category in upper_categories
        )

    def upper_bonus(self):
        return 35 if self.upper_score() >= 63 else 0

    def total_score(self):
        return sum(self.scorecard.values()) + self.upper_bonus()

    def get_state(self):
        return {
            "dice": self.dice.copy(),
            "rolls_left": self.rolls_left,
            "scorecard": self.scorecard.copy(),
            "upper_score": self.upper_score(),
            "upper_bonus": self.upper_bonus(),
            "total_score": self.total_score(),
            "game_over": len(self.scorecard) == len(CATEGORIES),
        }