import unittest
import battleship

class Test_Board(unittest.TestCase):

	def test_create_board(self):
		self.assertEqual(battleship.player1_board.create_board(), [
																	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
																	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
																	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
																	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
																	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
																	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
																	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
																	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
																	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
																	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
																	])

if __name__ == '__main__':
	unittest.main()