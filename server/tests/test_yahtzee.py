import unittest
from unittest.mock import patch

from server.game.yahtzee import YahtzeeGame


class TestYahtzeeGame(unittest.TestCase):
    def test_holding_dice(self):
        game = YahtzeeGame()

        with patch(
            "server.game.yahtzee.random.randint",
            side_effect=[1, 2, 3, 4, 5],
        ):
            self.assertEqual(game.roll(), [1, 2, 3, 4, 5])

        with patch(
            "server.game.yahtzee.random.randint",
            side_effect=[6, 6, 6],
        ):
            dice = game.roll([True, False, True, False, False])

        self.assertEqual(dice, [1, 6, 3, 6, 6])
        self.assertEqual(game.rolls_left, 1)

    def test_scoring_starts_next_turn(self):
        game = YahtzeeGame()

        with patch(
            "server.game.yahtzee.random.randint",
            side_effect=[5, 5, 5, 4, 4],
        ):
            game.roll()

        self.assertEqual(game.score("full_house"), 25)
        self.assertEqual(game.scorecard["full_house"], 25)
        self.assertEqual(game.rolls_left, 3)
        self.assertEqual(game.dice, [0, 0, 0, 0, 0])

    def test_cannot_roll_four_times(self):
        game = YahtzeeGame()

        for _ in range(3):
            game.roll()

        with self.assertRaises(ValueError):
            game.roll()