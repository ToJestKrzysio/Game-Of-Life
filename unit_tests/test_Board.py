import pytest
import numpy as np
from Board import Board
from fixture_constants import board_1, board_2, board_3, board_1_sum, board_2_sum, board_3_sum


class TestBoard:

    def test_random_seed(self):
        board_instance_1 = Board()
        board_instance_1.random()
        board_instance_2 = Board()
        board_instance_2.random()
        assert bool(np.all(board_instance_1.str() == board_instance_2.str())) is False

    def test_board_step(self, initial_board_step_1, initial_board_step_2, initial_board_step_3):
        board_1 = Board.from_array(array=initial_board_step_1)
        board_state = board_1.__repr__()
        assert bool(np.all(board_state == initial_board_step_1)) is True
        board_1.step()
        board_state = board_1.__repr__()
        assert bool(np.all(board_state == initial_board_step_2)) is True
        board_1.step()
        board_state = board_1.__repr__()
        assert bool(np.all(board_state == initial_board_step_3)) is True

    @pytest.mark.parametrize("fields, sum_array", [
        (board_1, board_1_sum),
        (board_2, board_2_sum),
        (board_3, board_3_sum)
    ])
    def test_board_neighbour_values(self, fields, sum_array):
        board = Board.from_array(array=fields)
        obtained_sum = board._sum_array()
        assert bool(np.all(obtained_sum == sum_array)) is True
