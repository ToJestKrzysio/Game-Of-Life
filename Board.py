import numpy as np
from typing import Optional, Tuple


class Board:

    def __init__(self, rows: Optional[int] = 11, columns: Optional[int] = 11, shape: Optional[Tuple[int, int, int, int]] = None):

        if shape is not None and isinstance(shape, tuple) and all(isinstance(item, int) for item in shape):
            self._origin_x, self._origin_y, self._rows_total, self._columns_total = shape
            self._rows_negative = self._origin_y
            self._rows_positive = self._rows_total - 1 - self._rows_negative
            self._columns_negative = self._origin_x
            self._columns_positive = self._columns_total - 1 - self._columns_negative

        elif rows is not None and isinstance(rows, int) and columns is not None and isinstance(columns, int):
            self._rows_total = rows
            self._origin_y = (self._rows_total - 1) // 2
            self._rows_negative = self._origin_y
            self._rows_positive = self._rows_total - 1 - self._rows_negative

            self._columns_total = columns
            self._origin_x = (self._columns_total - 1) // 2
            self._columns_negative = self._origin_x
            self._columns_positive = self._columns_total - 1 - self._columns_negative

        else:
            raise(ValueError("Missing init values"))

        self._field = np.zeros((self._rows_total, self._columns_total), dtype=bool)

    def __str__(self):
        return self._field.astype(int)

    def str(self):
        return self.__str__()

    def update_cell(self, x: int, y: int, value: bool):
        self._update_cell(x, y, value)

    def _update_cell(self, x: int, y: int, value: bool):
        self._field[x, y] = value

    def clear(self):
        self._fill(0)

    def _fill(self, value):
        self._field.fill(value)

    def random(self):
        self._random()

    def _random(self):
        self._field = np.random.choice(a=[True, False], size=(self._rows_total, self._columns_total))

    def _step(self):
        sum_array = np.zeros_like(self._field, dtype=int)

        sum_array[:, 1:] += self._field.astype(int)[:, 0:-1]  # sum for x=+1 and y=0
        sum_array[:, 0:-1] += self._field.astype(int)[:, 1:]  # sum for x=-1 and y=0

        sum_array[1:, :] += self._field.astype(int)[0:-1, :]  # sum for x=0 and y=+1
        sum_array[0:-1, :] += self._field.astype(int)[1:, :]  # sum for x=0 and y=-1

        sum_array[1:, 1:] += self._field.astype(int)[0:-1, 0:-1]  # sum for x=+1 and y=+1
        sum_array[1:, 0:-1] += self._field.astype(int)[0:-1, 1:]  # sum for x=-1 and y=+1
        sum_array[0:-1, 1:] += self._field.astype(int)[1:, 0:-1]  # sum for x=+1 and y=-1
        sum_array[0:-1, 0:-1] += self._field.astype(int)[1:, 1:]  # sum for x=-1 and y=-1

        alive_2 = sum_array == 2
        alive_3 = sum_array == 3
        birth = sum_array == 3
        self._field = np.logical_or(alive_2, alive_3, birth)

    def step(self):
        self._step()


if __name__ == "__main__":
    board = Board()
    board.random()
    print("\n", board.str())
    board.step()
    print("\n", board.str())
