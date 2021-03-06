import numpy as np

board_1 = np.array([
    [1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0]
], dtype=bool)

board_1_sum = np.array([
    [1, 2, 1, 1, 3, 3, 3],
    [3, 2, 1, 1, 2, 3, 2],
    [2, 3, 2, 1, 2, 3, 2],
    [2, 1, 1, 0, 0, 0, 0],
    [2, 2, 2, 1, 2, 3, 2],
    [2, 2, 2, 2, 1, 2, 1],
    [1, 3, 1, 2, 2, 3, 2]
], dtype=int)

board_2 = np.array([
    [0, 0, 0, 0, 1, 1, 1],
    [1, 1, 0, 0, 1, 1, 1],
    [1, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0]
], dtype=bool)

board_2_sum = np.array([
    [2, 2, 1, 2, 3, 5, 3],
    [3, 3, 2, 2, 4, 6, 4],
    [3, 3, 2, 1, 3, 3, 3],
    [2, 2, 1, 0, 2, 2, 2],
    [1, 1, 1, 0, 2, 1, 2],
    [2, 1, 2, 0, 3, 2, 3],
    [2, 1, 2, 0, 2, 1, 2]
], dtype=int)

board_3 = np.array([
    [0, 0, 0, 0, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0]
], dtype=bool)

board_3_sum = np.array([
    [2, 2, 1, 1, 0, 2, 0],
    [3, 3, 2, 2, 3, 5, 3],
    [3, 3, 2, 1, 1, 2, 1],
    [2, 2, 1, 1, 2, 3, 2],
    [0, 0, 0, 1, 2, 3, 2],
    [0, 0, 0, 1, 1, 2, 1],
    [0, 0, 0, 1, 2, 3, 2]
], dtype=int)
