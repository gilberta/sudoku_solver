#!/usr/bin/env python3
import copy

class SudokuPuzzle:
	def __init__(self,puzzle_file):
		self.puzzle_file = puzzle_file
		self.puzzle = self.import_puzzle(puzzle_file)
		self.solutions = [[ [] for row in range(9)] for col in range(9)]

	def import_puzzle(self,puzzle_file):
		#returns a 2d array of the puzzle
		#formatted as puzzle[row][col]

		# open puzzle file
		puzzle = open(puzzle_file,'r')

		# initalize puzzle array
		array = [[ 0 for row in range(9)] for col in range(9)]

		# fill in array with puzzle values
		lines = puzzle.readlines()
		for row, line in enumerate(lines):
		    if row<9:
		        for col, number in enumerate(line):
		            if col<9:
		                if number == ' ':
		                    array[row][col] = 0 #make empty spots into zeros
		                else:
		                    array[row][col] = int(number) #make numbers into integers
		            else:
		                break
		    else:
		        break
		return array

	def get_row(self,row,output='value'):
		#returns a list of values in the row
		#specify output='solutions' to return lists of solutions
		if output == 'solutions':
			return self.solutions[row]
		return self.puzzle[row]

	def get_col(self,col,output='value'):
		#returns a list of values in the col
		#specify output='solutions' to return lists of solutions
		column = []
		if output == 'solutions':
			for row in range(9):
				column.append(self.solutions[row][col])
			return column
		for row in range(9):
			column.append(self.puzzle[row][col])
		return column

	def get_cell(self,row,col,output='value'):
		#returns a list of values in the cell
		#automatically determines which cell the value is in
		#specify output='solutions' to return lists of solutions
		cell_row = row//3
		cell_col = col//3
		cell = []
		if output == 'solutions':
			for row in range(cell_row*3,(cell_row*3)+3):
				for col in range(cell_col*3,(cell_col*3)+3):
					cell.append(self.solutions[row][col])	
			return cell
		for row in range(cell_row*3,(cell_row*3)+3):
			for col in range(cell_col*3,(cell_col*3)+3):
				cell.append(self.puzzle[row][col])
		return cell

	def check_solns(self,row,col):
		# outputs list of possible solutions for that cell based on found values
		# checks the row, column, and cell
		solns = range(1,10)
		#check row
		solns = list(set(solns)-set(self.get_row(row)))
		#check col
		solns = list(set(solns)-set(self.get_col(col)))
		#check cell
		solns = list(set(solns)-set(self.get_cell(row,col)))

		return solns

	def populate_solns(self):
		# runs through the puzzle once
		# populates each 0 (empty) cell with possible solutions
		# if there is exactly one solution, it replaces that value with the solution found
		counter = 0
		for row in range(9):
			for col in range(9):
				if self.puzzle[row][col]==0:
					self.solutions[row][col] = self.check_solns(row,col)
					if len(self.solutions[row][col]) == 1:
						self.puzzle[row][col] = self.solutions[row][col][0]
						counter += 1
				else: continue

		print('Iteration completed, %i new solutions found.' % counter)

		return None

	def print_puzzle(self):
		# nicely outputs the current puzzle state
		pretty_puzzle = copy.deepcopy(self.puzzle)
		print('Current puzzle: %s' % self.puzzle_file)
		print('.-------.-------.-------.')
		for i in range(3):
			for j in range(3):
				pretty_puzzle[(3*i)+j] = [str(zeros).replace('0','_') for zeros in pretty_puzzle[(3*i)+j]]
				print('| %s %s %s | %s %s %s | %s %s %s |' % tuple(pretty_puzzle[(3*i)+j]))
			print('.-------.-------.-------.')






		