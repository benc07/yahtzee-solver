class YahtzeeGame:
    def __init__(self):
        self.dice = [0, 0, 0, 0, 0]
        self.rolls_left = 3
        self.scorecard = {}