import pytest
from Board.board_engine import Board
from unittest.mock import Mock
import numpy as np
from constants import board_1, board_2, board_3, board_1_sum, board_2_sum, board_3_sum

BOARD_SHAPE = (3, 3, 7, 7)


class TestBoard:

    def setup(self):
        self.mock_board_obj = Mock()

    @pytest.mark.parametrize("")
    def test_init(self):
        Board.__init__(self=self.mock_board_obj)

    def test_random_seed(self):
        board_instance_1 = Board()
        board_instance_1.random()
        board_instance_2 = Board()
        board_instance_2.random()
        assert bool(np.all(board_instance_1.str() == board_instance_2.str())) is False

    def test_board_step(self, initial_board_step_1, initial_board_step_2, initial_board_step_3):
        board_instance = Board.from_array(array=initial_board_step_1)
        board_state = board_instance.__repr__()
        assert bool(np.all(board_state == initial_board_step_1)) is True
        board_instance.step()
        board_state = board_instance.__repr__()
        assert bool(np.all(board_state == initial_board_step_2)) is True
        board_instance.step()
        board_state = board_instance.__repr__()
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

    @pytest.mark.parametrize("array", [-1, 2.5, 2e6, [1, 1], {2, 3}, {"key": 1}, "String", ""])
    def test_board_from_array__wrong_type(self, array):
        with pytest.raises(TypeError):
            Board.from_array(array=array)

    @pytest.mark.parametrize("dimensions", [1, 3, 4, 5])
    def test_board_from_array__wrong_value(self, dimensions):
        with pytest.raises(ValueError):
            Board.from_array(np.ones((2,) * dimensions))

    @pytest.mark.parametrize("array", [-1, 2.5, 2e6, [1, 1], {2, 3}, {"key": 1}, "String", ""])
    def test_board_fill_whole_board__wrong_type(self, array):
        board_instance = Board()
        with pytest.raises(TypeError):
            board_instance.fill_whole_board(array=array)

    @pytest.mark.parametrize("rows", [value for value in range(1, BOARD_SHAPE[2] + 5) if value != BOARD_SHAPE[2]])
    @pytest.mark.parametrize("columns", [value for value in range(1, BOARD_SHAPE[3] + 5) if value != BOARD_SHAPE[3]])
    def test_board_fill_whole_board__wrong_value(self, rows, columns):
        board_instance = Board(shape=BOARD_SHAPE)
        with pytest.raises(ValueError):
            board_instance.fill_whole_board(array=np.ones((rows, columns)))
