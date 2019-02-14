# Need:
# A board
  # Attributes:
  #   in_play = true
  # Actions:
  # 	create board
  # 	display board
  # 	check for hits
  # 	check for wins

# Ships
	# Need to know:
	# 	num holes - 5 holes, 3 holes, 3 holes, 2 holes
	# 	orientation - horizontal or vertical
# Players
	# player_1 - create a board
	# player_2 - create a board

class Board:
	""" A class to represent a board for each player """
	

	def __init__(self, player):
		""" Instantiate each new board with a player and a board
			consisting of 10 rows and columns of zeros: 

			[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

		"""
		self.player = player
		self.board = [[0] * 10 for i in range(10)]
		self.ships = []


	def display_board(self):
		""" Print the board """

		print(self.board)


	def add_ship(self, num_holes, start_pos_row, start_pos_colmn, orientation):

		# instantiate a ship
		ship = Ship(num_holes, start_pos, orientation)

		# check if there's a ship already
		if self.board[num_holes[1]][num_holes[0]] != 0:

		
		# check that hole ship added to are not already taken
		# check that no holes in ship are off the board.
		# change board to reflect added ship
		if orientation == "horizontal":


		if orientation == "vertical"
		# add ship to ships list
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
	def __init__(self, num_holes, start_pos_row, start_pos_colmn, orientation):
		self.num_holes = num_holes
		# start pos is a tuple with (x, y) dimenstions
		self.start_pos_row = start_pos_row
		self.start_pos_colmn = start_pos_colmn
		self.orientation = orientation

		if self.orientation.lower() == "horizontal" or self.orientation.lower == "vertical": 
			self.orientation = orientation.lower()
		else:
			print("Orientation must be vertical or horizontal")


	def __repr__(self):
		return f"holes: {self.num_holes}, start: {self.start_pos}, orient: {self.orientation}>"


# player1_board = Board("player1")
# player1_board.display_board()
