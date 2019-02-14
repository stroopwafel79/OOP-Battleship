import unittest
from battleship import Board

class Test_Board(unittest.TestCase):

	def test_create_board(self):
		board = Board("player1")
		self.assertEqual(board.display_board(), [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
											     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
											     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
											     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
											     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
											     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
											     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
											     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
											     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
											     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

if __name__ == '__main__':
	unittest.main()