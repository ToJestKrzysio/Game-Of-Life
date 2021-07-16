import pytest
import numpy as np
from fixture_constants import board_1, board_2, board_3, board_1_sum, board_2_sum, board_3_sum

@pytest.fixture()
def initial_board_step_1():
    return board_1


@pytest.fixture()
def initial_board_step_1__neighbour_count():
    return board_1_sum


@pytest.fixture()
def initial_board_step_2():
    return board_2


@pytest.fixture()
def initial_board_step_2__neighbour_count():
    return board_2_sum


@pytest.fixture()
def initial_board_step_3():
    return board_3


@pytest.fixture()
def initial_board_step_3__neighbour_count():
    return board_3_sum
