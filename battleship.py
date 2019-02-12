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

	def add_ship(self, ship, orientation):
		pass

	def display_board(self):

		pass

	def check_hits(self, location, player):
		#if ship at location, hit

		check_win()

	def check_win(self):

		pass

	def __repr__(self):

		return f"<Board of {self.player}>"

class Ship:
	""" A class to represent a ship """
	def __init__(self, num_holes, start_pos, orientation):
		self.num_holes = num_holes
		self.start_pos = start_pos
		self.orientation = orientation

	def __repr__(self):
		return f"holes: {self.num_holes}, start: {self.start_pos}, orient: {self.orientation}>"