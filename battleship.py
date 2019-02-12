# Need:
# A board
  Attributes:
    in_play = true
  Actions:
  	create board
  	display board
  	check for hits
  	check for wins

# Ships
	Need to know:
		num holes - 5 holes, 3 holes, 3 holes, 2 holes
		orientation - horizontal or vertical
# Players
	player_1 - create a board
	player_2 - create a board

class Board:
	""" A class to represent a board for each player """
	def __init__(self, player):
		self.player = player

	def create_board(self):

		pass

	def display_board(self):

		pass

	def check_hits(self, location, player):
		#if ship at location, hit

		check_win()

	def check_win(self):

		pass