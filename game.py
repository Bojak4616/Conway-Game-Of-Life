#!/usr/bin/python

from time import sleep
from sys  import exit

class Conway:
	def __init__ (self, width, height):
		self.map = []
		self.width  = width
		self.height = height

	def generate_world(self):
		for cell_height in xrange(self.height):
			self.map.append([])
			for cell_width in xrange(self.width):
				self.map[cell_height].append('-')


	def print_game_board(self):
		board = ""
		for cell_height in xrange(self.height):
			for cell_width in xrange(self.width):
				board += self.map[cell_height][cell_width]
			board += '\n'
		print board

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

	def self_alive(self, x, y):
		try:
			return self.map[x][y] == '+'
		except IndexError:
			return False

	def set_cell(self, x, y):
		self.map[x][y] = '+'

	def game_tick(self):
		tmp_map = []
		for y in xrange(self.height):
			tmp_map.append([])
			for x in xrange(self.width):
				tmp_map[y].append('-')

		for y in xrange(self.height):
			for x in xrange(self.width):		
				#Rules
				if self.neighbors_alive(x, y) < 2:
					tmp_map[x][y] = '-'

				if self.self_alive(x, y) == True and (self.neighbors_alive(x, y) == 2 or self.neighbors_alive(x, y) == 3):
					tmp_map[x][y] = '+'

				if self.self_alive(x, y) == True and self.neighbors_alive(x, y) > 3:
					tmp_map[x][y] = '-'

				if self.self_alive(x, y) == False and self.neighbors_alive(x, y) == 3:
					tmp_map[x][y] = '+'

		self.map = tmp_map

if __name__ == '__main__':

	x = int(raw_input("Enter board width: "))
	y = int(raw_input("Enter board height: "))
	if(x < 20 or y < 20):
		print "ERROR: Game board has to be at least 20x20"
		exit(1)

	print "Enter coordinates as 'x,y'[Enter]. A blank line will continue the program. Watch your typing!"
	cords = []
	while(True):
		cord = raw_input()
		if len(cord) != 3:
			break
		cords += str(cord).split(',')

	print(chr(27) + "[2J")
	NewGame = Conway(x,y)
	NewGame.generate_world()
	
	for i in xrange(len(cords)):
		if i % 2 != 0:
			continue
		try:
			NewGame.set_cell(int(cords[i]), int(cords[i+1]))
		except IndexError:
			break

	while(True):
		sleep(.3)
		print(chr(27) + "[2J")
		NewGame.print_game_board()
		NewGame.game_tick()



