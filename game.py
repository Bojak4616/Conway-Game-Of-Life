#!/usr/bin/python

from time import sleep
from os import system

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

	print(chr(27) + "[2J")
	NewGame = Conway(20,20)
	NewGame.generate_world()
	NewGame.set_cell(2, 1)
	NewGame.set_cell(3, 2)
	NewGame.set_cell(1, 3)
	NewGame.set_cell(2, 3)
	NewGame.set_cell(3, 3)


	while(True):
		sleep(.3)
		print(chr(27) + "[2J")
		NewGame.print_game_board()
		NewGame.game_tick()



