import numpy as np
from typing import Optional, Tuple


class BoardEngine:

    def __init__(self, rows: Optional[int] = 11, columns: Optional[int] = 11,
                 shape: Optional[Tuple[int, int, int, int]] = None) -> None:
        """
        Creates Board instance

        :param rows: Number of rows of the matrix
        :param columns: Number of columns of the matrix
        :param shape: Shape parameter accordingly (matrix center x-coordinate, matrix center y-coordinate,
                                                   number of columns, number of rows)
        """
        if shape is not None and isinstance(shape, tuple) and all(isinstance(item, int) for item in shape):
            self._assign_shape(shape)
        elif rows is not None and isinstance(rows, int) and columns is not None and isinstance(columns, int):
            self._assign_dimensions(rows, columns)
        else:
            raise(ValueError("Missing init values"))

        self._row_edges = self._rows_total + 1
        self._column_edges = self._columns_total + 1
        self._field = np.zeros((self._rows_total, self._columns_total), dtype=bool)

    def _assign_shape(self, shape: Optional[Tuple[int, int, int, int]]) -> None:
        """
        Assigns matrix parameters

        :param shape: Shape parameter accordingly (matrix center x-coordinate, matrix center y-coordinate,
                                                   number of columns, number of rows)
        :return: None
        """
        self._origin_x, self._origin_y, self._rows_total, self._columns_total = shape
        self._rows_negative = self._origin_y
        self._rows_positive = self._rows_total - 1 - self._rows_negative
        self._columns_negative = self._origin_x
        self._columns_positive = self._columns_total - 1 - self._columns_negative

    def _assign_dimensions(self, rows, columns) -> None:
        """
        Calculates matrix center and assigns dimensions.

        :param rows: Number of rows of the matrix
        :param columns: Number of columns of the matrix
        :return: None
        """
        self._rows_total = rows
        self._origin_y = (self._rows_total - 1) // 2
        self._rows_negative = self._origin_y
        self._rows_positive = self._rows_total - 1 - self._rows_negative

        self._columns_total = columns
        self._origin_x = (self._columns_total - 1) // 2
        self._columns_negative = self._origin_x
        self._columns_positive = self._columns_total - 1 - self._columns_negative

    @classmethod
    def from_array(cls, array: np.ndarray):
        """
        Create instance of the Board according to passed np.ndarray truth table.

        :param array: np.array

        :return: new instance of the Board
        """
        if not isinstance(array, np.ndarray):
            raise TypeError(f"Wrong type of 'array' parameter. Expected np.ndarray got {type(array)}")
        if not array.ndim == 2:
            raise ValueError(f"wrong shape of 'array' parameter. Expected ndim=2 but gotten ndim={array.ndim}")
        rows, columns = array.shape
        board_instance = cls(rows=rows, columns=columns)
        board_instance._fill_whole_board(array=array)
        return board_instance

    def __str__(self) -> np.ndarray:
        """ Representation of class instance """
        return self._field.astype(int)

    def __repr__(self) -> np.ndarray:
        """ Representation of class instance """
        return self._field

    def update_cell(self, x: int, y: int, value: bool) -> None:
        """ Public implementation of _update_Cell method. """
        self._update_cell(x, y, value)

    def _update_cell(self, x: int, y: int, value: bool) -> None:
        """
        Updates field with the given value

        :param x: x-coordinate of the field
        :param y: y-coordinate of the field

        :param value: value to be assigned to given field of the board
        :return: None
        """
        if type(value) is not bool:
            value = bool(value)
        self._field[x, y] = bool(value)

    def clear(self) -> None:
        """ Clear all of the cells. """
        self._fill(False)

    def _fill(self, value: bool) -> None:
        """
        Assign value to all of the cells.

        :param value: boolean value to be used to fill cell.

        :return: None
        """
        self._field.fill(bool(value))

    def _fill_whole_board(self, array: np.ndarray) -> None:
        """
        Fill the board according to passed truth table.

        :param array: Truth table to be used for filling values.

        :return: None
        """
        self._field = array.astype(bool)

    def fill_whole_board(self, array: np.ndarray) -> None:
        """ Public implementation of _fill_whole_board. """
        if not isinstance(array, np.ndarray):
            raise TypeError(f"Wrong type of 'array' parameter. Expected np.ndarray got {type(array)}")
        if not (self._rows_total, self._columns_total) == array.shape:
            raise ValueError(f"Wrong shape of 'array' parameter. Expected ({self._rows_total}, {self._columns_total}) "
                             f"but gotten {array.shape}")
        self._fill_whole_board(array=array)

    def random(self) -> None:
        """
        Fills cell value randomly with 0 or 1.

        :return: None
        """
        self._field = np.random.choice(a=[True, False], size=(self._rows_total, self._columns_total))

    def step(self) -> None:
        """
        Calculates cell state in next time step and assigns it to _field attribute.

        :return: None
        """
        sum_array = self._sum_array()
        alive_2 = np.logical_and(sum_array == 2, self._field)
        birth = sum_array == 3
        self._field = np.logical_or(alive_2, birth)

    def _sum_array(self) -> np.ndarray:
        """
        Calculates number of alive neighbours of the given cell.

        :return: array, where each cell has assigned number of alive neighbours.
        """
        sum_array = np.zeros_like(self._field, dtype=int)

        sum_array[:, 1:] += self._field.astype(int)[:, 0:-1]  # sum for x=+1 and y=0
        sum_array[:, 0:-1] += self._field.astype(int)[:, 1:]  # sum for x=-1 and y=0

        sum_array[1:, :] += self._field.astype(int)[0:-1, :]  # sum for x=0 and y=+1
        sum_array[0:-1, :] += self._field.astype(int)[1:, :]  # sum for x=0 and y=-1

        sum_array[1:, 1:] += self._field.astype(int)[0:-1, 0:-1]  # sum for x=+1 and y=+1
        sum_array[1:, 0:-1] += self._field.astype(int)[0:-1, 1:]  # sum for x=-1 and y=+1
        sum_array[0:-1, 1:] += self._field.astype(int)[1:, 0:-1]  # sum for x=+1 and y=-1
        sum_array[0:-1, 0:-1] += self._field.astype(int)[1:, 1:]  # sum for x=-1 and y=-1

        return sum_array

    def get_shape(self) -> Tuple[int, int]:
        """
        Returns the dimensions of the current board.

        :return: Tuple(total_rows, total_columns)
        """
        return self._rows_total, self._columns_total
