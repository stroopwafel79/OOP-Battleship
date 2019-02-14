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
		self.in_play = True


	def display_board(self):
		""" Print the board """

		print(self.board)


	def add_ship(self, num_holes, start_pos_row, start_pos_colmn, orientation):
		""" 
		Add a ship to the board. A ship on the board will be represented by
		the number of holes it has. A ship will not be added if part of it
		hangs off the board or if another ship is already there.
		Ex: 
			[[5, 5, 5, 5, 5, 0, 0, 0, 0, 0], 
		     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		     [0, 0, 0, 0, 0, 2, 0, 0, 0, 0], 
		     [0, 0, 0, 0, 0, 2, 0, 0, 0, 0], 
		     [0, 3a, 0, 0, 0, 0, 0, 0, 0, 0], 
		     [0, 3a, 0, 0, 0, 0, 0, 0, 0, 0], 
		     [0, 3a, 0, 0, 0, 3b, 3b, 3b, 0, 0], 
		     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
		     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
		"""

		# instantiate a ship
		ship = Ship(num_holes, start_pos_row, start_pos_colmn, orientation)
		
		# change board to reflect added ship
		for i in range(ship.num_holes):
			num_holes = ship.num_holes

			# because there are two ships with 3 holes, we need to know
			# if the ship being added is 3a or 3b
			if num_holes == 3:
			for ship in self.ships:
				if ship.num_holes == 3:
					num_holes = "3b"
				else:
					num_holes = "3a"

			# make sure ship all holes of the ship will be on the board
			if i < 10:			 
				if orientation == "horizontal":
					# make sure there's not a ship already there
					if self.board[start_pos_row][start_pos_colmn + i] == 0:
						self.board[start_pos_row][start_pos_colmn + i] = num_holes
					
				elif orientation == "vertical":
					if self.board[start_pos_row + i][start_pos_colmn] == 0:
						self.board[start_pos_row + i][start_pos_colmn] = num_holes
			else:
				print("This ship is off the board. Please choose a new start position")

		# add new ship to the ships list
		self.ships.append(ship)


	def shoot_missle(self, row, column):
		""" Shoot a missle at opponents board. """

	def play_game(self, ):
		pass

	def check_hit(self, row, column):
		""" check if the ship has been hit """
		board_val = self.board[row][column]
		if board_val != 0:
			if board_val == "X":
				print("Ship has previously been hit")
			else:
				# update board with an X
				board_val = "X"
				print("HIT!")

				# check if ship is sunk
				if check_ship_sunk():
					print("You sunk my battleship!")
					# check if player is the winner
					if check_win():
						print("You are the winner!")
		else:
			print("Miss")


	def check_ship_sunk(self):

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
		self.sunk = False

		if self.orientation.lower() == "horizontal" or self.orientation.lower == "vertical": 
			self.orientation = orientation.lower()
		else:
			print("Orientation must be vertical or horizontal")


	def __repr__(self):
		return f"holes: {self.num_holes}, start: {self.start_pos}, orient: {self.orientation}>"


# player1_board = Board("player1")
# player1_board.display_board()
