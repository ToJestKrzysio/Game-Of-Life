import pygame
from .board_engine import BoardEngine
from typing import Tuple
from Constants import CellParameters, CellColors


class BoardSurface(BoardEngine):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._board_width = self._columns_total * CellParameters.CELL_SIZE.value + \
            self._column_edges * CellParameters.EDGE_SIZE.value
        self._board_height = self._rows_total * CellParameters.CELL_SIZE.value + \
            self._row_edges * CellParameters.EDGE_SIZE.value

    def get_board_size(self) -> Tuple[int, int]:
        """
        Returns shape of the board surface as a tuple.

        :return: (width, height)
        """
        return self._board_width, self._board_height

    def draw_cells(self) -> pygame.Surface:
        """
        Generates board representation as pygame.Surface object.

        :return: Surface drawn according to values of cells.
        """
        board_surface = pygame.Surface(size=self.get_board_size(), flags=pygame.SRCALPHA)
        # board_surface.convert_alpha()
        for column_index in range(self._columns_total):
            for row_index in range(self._rows_total):
                if self._field[row_index, column_index]:
                    self._draw_cell(board_surface, row_index, column_index, CellColors.BLACK)
        return board_surface

    def generate_grid(self) -> pygame.Surface:
        """ Draw grid onto _grid_surface according to specified number of rows and columns. """
        grid_surface = pygame.Surface(size=self.get_board_size())
        grid_surface.fill(CellColors.GRAY.value)
        for column_index in range(self._columns_total):
            for row_index in range(self._rows_total):
                self._draw_cell(grid_surface, row_index, column_index, CellColors.WHITE)
        return grid_surface

    @staticmethod
    def _draw_cell(surface, row, column, color: CellColors = CellColors.WHITE):
        rect = pygame.Rect(column * (CellParameters.CELL_SIZE.value + CellParameters.EDGE_SIZE.value) +
                           CellParameters.EDGE_SIZE.value,
                           row * (CellParameters.CELL_SIZE.value + CellParameters.EDGE_SIZE.value) +
                           CellParameters.EDGE_SIZE.value,
                           CellParameters.CELL_SIZE.value,
                           CellParameters.CELL_SIZE.value)
        pygame.draw.rect(surface, color.value, rect)
