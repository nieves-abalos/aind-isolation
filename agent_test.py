"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest
import isolation
import game_agent

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)
        print("setup")

    # @unittest.skip("Skip eval function test.")  # Uncomment this line to skip test
    def test_heuristic(self):
        """ Test output interface of heuristic score function interface."""
        self.player1 = "Player1"
        self.player2 = "Player2"
        p1_location = (0, 0)
        p2_location = (1, 1)  # top left corner
        self.game = isolation.Board(self.player1, self.player2)
        self.game.apply_move(p1_location)
        self.game.apply_move(p2_location)
        self.assertIsInstance(game_agent.custom_score(self.game, self.player1), float,
            "The heuristic function should return a floating point")

    def test_minimax_interface(self):
        """ Test CustomPlayer.minimax interface with simple input """
        h, w = 7, 7  # board size
        test_depth = 1
        starting_location = (5, 3)
        adversary_location = (0, 0)  # top left corner
        iterative_search = False
        search_method = "minimax"
        heuristic = lambda g, p: 0.  # return 0 everywhere

        # create a player agent & a game board
        agentUT = game_agent.MinimaxPlayer()
        agentUT.time_left = lambda: 99  # ignore timeout for fixed-depth search
        board = isolation.Board(agentUT, 'null_agent', w, h)

        # place two "players" on the board at arbitrary (but fixed) locations
        board.apply_move(starting_location)
        board.apply_move(adversary_location)

        for move in board.get_legal_moves():
            next_state = board.forecast_move(move)
            v, _ = agentUT.minimax(next_state, test_depth)

            self.assertTrue(type(v) == float,
                            ("Minimax function should return a floating " +
                             "point value approximating the score for the " +
                             "branch being searched."))

if __name__ == '__main__':
    unittest.main()
