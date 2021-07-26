import pygame
import Board
from Constants import CellParameters, CellColors


class Game:

    def __init__(self):
        """ Initialize the new board instance. """
        self._board = Board.BoardSurface(shape=(11, 11, 21, 21))
        self._window_width, self._window_height = self._board.get_board_size()
        self._board.random()
        self._init_pygame()
        self._grid_surface = self._board.generate_grid()

    def _draw(self) -> None:
        """
        Draw new frame.

        :return: None
        """
        self._window.blit(self._grid_surface, (0, 0))
        self._window.blit(self._board.draw_cells(), (0, 0))
        pygame.display.update()

    # def _generate_grid(self) -> None:
    #     """ Draw grid onto _grid_surface according to specified number of rows and columns. """
    #     self._grid_surface = pygame.Surface(size=(self._window_width, self._window_height))
    #     self._grid_surface.fill(CellColors.GRAY.value)
    #     for column_index in range(self._columns):
    #         for row_index in range(self._rows):
    #             rect = pygame.Rect(column_index * (CellParameters.CELL_SIZE.value + CellParameters.EDGE_SIZE.value) +
    #                                CellParameters.EDGE_SIZE.value,
    #                                row_index * (CellParameters.CELL_SIZE.value + CellParameters.EDGE_SIZE.value) +
    #                                CellParameters.EDGE_SIZE.value,
    #                                CellParameters.CELL_SIZE.value,
    #                                CellParameters.CELL_SIZE.value)
    #             pygame.draw.rect(self._grid_surface, CellColors.WHITE.value, rect)
    #
    # def _calculate_board_size(self) -> None:
    #     self._window_width = self._columns * CellParameters.CELL_SIZE.value + \
    #         self._column_edges * CellParameters.EDGE_SIZE.value
    #     self._window_height = self._rows * CellParameters.CELL_SIZE.value + \
    #         self._row_edges * CellParameters.EDGE_SIZE.value

    # def _count_grid_edges(self) -> None:
    #     self._rows, self._columns = self._board.get_shape()
    #     self._row_edges = self._rows + 1
    #     self._column_edges = self._columns + 1

    def _init_pygame(self) -> None:
        pygame.display.init()
        self._window = pygame.display.set_mode((self._window_width, self._window_height))
        pygame.display.update()

    def _randomize(self) -> None:
        self._board.random()


if __name__ == "__main__":
    game = Game()
    clock = pygame.time.Clock()
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        game._draw()
