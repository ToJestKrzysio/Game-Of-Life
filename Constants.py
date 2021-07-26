from enum import Enum


class CellColors(Enum):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (128, 128, 128)


class CellParameters(Enum):
    CELL_SIZE = 20
    EDGE_SIZE = 2

