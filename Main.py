from Board.board_engine import Board

board = Board(rows=11, columns=11)
print(board.str())
board.random()
print(board.str())
