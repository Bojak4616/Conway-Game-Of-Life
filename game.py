#!/usr/bin/python

from time import sleep

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


if __name__ == '__main__':

	NewGame = Conway(20,20)
	NewGame.generate_world()
	NewGame.print_game_board()

