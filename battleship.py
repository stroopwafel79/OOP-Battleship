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
		# add new ship to the ships list
		ships.append(ship)


		# change board to reflect added ship
		for i in range(num_holes):
			# make sure ship all holes of the ship will be on the board
			if i < 10:			 
				if orientation == "horizontal":
					# make sure there's not a ship already there
					if board[start_pos_row][start_pos_colmn + i] == 0:
						board[start_pos_row][start_pos_colmn + i] = num_holes
					
				elif orientation == "vertical":
					if boardboard[start_pos_row + 1][start_pos_colmn] == 0:
						board[start_pos_row + i][start_pos_colmn] = num_holes
			else:
				print("This ship is off the board. Please choose a new start position")


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
