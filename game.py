#!/usr/bin/python
""" Author: Jesse Buonanno
	Purpose: Plays Conway's Game of Life with user provided coordinates and board size
	Output: Terminal ascii representation of Conway's Game of Life
	References: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
"""

from time import sleep
from sys  import exit

class Conway:
	def __init__ (self, width, height):
		self.map = []
		self.width  = width
		self.height = height

	#Initial creation of game board (map) into 2D array
	def generate_world(self):
		for cell_height in xrange(self.height):
			self.map.append([])
			for cell_width in xrange(self.width):
				self.map[cell_height].append('-')

	#Iteration through map and print to terminal
	def print_game_board(self):
		board = ""
		for cell_height in xrange(self.height):
			for cell_width in xrange(self.width):
				board += self.map[cell_height][cell_width]
			board += '\n'
		print board

	#Check each of a cell's 8 neighbors
	def neighbors_alive(self, x, y):
		live_cells = 0
	 
		if self.self_alive(x+1,y-1):
			live_cells += 1
		if self.self_alive(x-1,y+1):
			live_cells += 1
		if self.self_alive(x+1,y+1):
			live_cells += 1
		if self.self_alive(x,y+1):
			live_cells += 1
		if self.self_alive(x+1,y):
			live_cells += 1
		if self.self_alive(x-1,y-1):
			live_cells += 1
		if self.self_alive(x-1,y):
			live_cells += 1
		if self.self_alive(x,y-1):
			live_cells += 1

		return live_cells

	#Is the current cell alive?
	def self_alive(self, x, y):
		#Exception handling in case the user entered coordinates that is not viable for
		#    the game board size
		try:
			return self.map[x][y] == '+'
		except IndexError:
			return False

	#Make a cell alive
	def set_cell(self, x, y):
		self.map[x][y] = '+'

	#Each generation of a new map
	def game_tick(self):
		tmp_map = []

		#Need to populate a tmp_map otherwise rules will affect neighbor cells before 
		#    those cells had rules applied themselves
		for y in xrange(self.height):
			tmp_map.append([])
			for x in xrange(self.width):
				tmp_map[y].append('-')

		for y in xrange(self.height):
			for x in xrange(self.width):		
				#Any live cell with fewer than two live neighbors dies, as if caused by under-population.
				if self.neighbors_alive(x, y) < 2:
					tmp_map[x][y] = '-'

				#Any live cell with two or three live neighbors lives on to the next generation.
				if self.self_alive(x, y) == True and (self.neighbors_alive(x, y) == 2 or self.neighbors_alive(x, y) == 3):
					tmp_map[x][y] = '+'

				#Any live cell with more than three live neighbors dies, as if by over-population.
				if self.self_alive(x, y) == True and self.neighbors_alive(x, y) > 3:
					tmp_map[x][y] = '-'

				#Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
				if self.self_alive(x, y) == False and self.neighbors_alive(x, y) == 3:
					tmp_map[x][y] = '+'

		self.map = tmp_map

if __name__ == '__main__':
	#Make sure your input is valid (Since Chiam has trouble typing)
	try:
		x = int(raw_input("Enter board width: "))
		y = int(raw_input("Enter board height: "))
	except ValueError:
		print "ERROR: Need to enter numbers for a board size"
		exit(1)

	#Min board size
	if(x < 20 or y < 20):
		print "ERROR: Game board has to be at least 20x20"
		exit(1)

	print "Enter coordinates as 'x,y'[Enter]. A blank line or invalid coordinate will \
continue the program.\nWatch your typing!"
	cords = []
	while(True):
		cord = raw_input()
		if len(cord) != 3 or cord.find(',') == -1:
			break
		cords += str(cord).split(',')

	#Print escape char to clear terminal
	print(chr(27) + "[2J")
	NewGame = Conway(x,y)
	NewGame.generate_world()
	
	#Plot the user inputed coordinated
	for i in xrange(len(cords)):
		if i % 2 != 0:
			continue
		try:
			NewGame.set_cell(int(cords[i]), int(cords[i+1]))
		except IndexError:
			break

	#Play the game
	while(True):
		sleep(.5)
		print(chr(27) + "[2J")
		NewGame.print_game_board()
		NewGame.game_tick()



