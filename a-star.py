import random
from math import hypot

class node():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.wall = False
		#if random.randint(0,100) < 30:
		#    self.wall = True
		self.start = False
		self.end = False

	def getG(self, start):
		return EuclideanDistance(self, start)
		#return ManhattanDistance(self, start)

	def getH(self, end):
		return EuclideanDistance(self, end)
		#return ManhattanDistance(self, end)

	def getF(self, start, end):
		return self.getG(start) + self.getH(end)

	def getNeighbours(self, grid):
		self.neighbours=[]
		if self.x < cols-1:
			self.neighbours.append(grid[self.x+1][self.y])
		if self.y < rows-1:
			self.neighbours.append(grid[self.x][self.y+1])
		if self.x > 0:
			self.neighbours.append(grid[self.x-1][self.y])
		if self.y > 0:
			self.neighbours.append(grid[self.x][self.y-1])
		return self.neighbours

	def setPrevious(self, previous):
		self.cameFrom = previous

	def __repr__(self):
		if current == self:
			return '( * )'
		return '({0}, {1})'.format(self.x, self.y)

	def __iter__(self):
		return self.f

def ManhattanDistance(a,b):
	return (a.x-b.x)+(a.y-b.y)

def EuclideanDistance(a,b):
	x, y = (a.x-b.x), (a.y-b.y)
	return hypot(x, y)

def reconstructed_path(cameFrom, current):
	path = [current]
	while current in cameFrom.keys():
		current = cameFrom[current]
		path.append(current)
	return path

def printGrid(grid):
	for y in range(rows):
		for x in range(cols):
			print(grid[x][y], end='')
		print('')
	print('-'*30)

def Astar(cols, rows, endx, endy, startx, starty):
	global current
	grid = []
	for x in range(cols):
		col = []
		for y in range(rows):
			col.append(node(x,y))
		grid.append(col)

	grid[endx][endy].end = True
	end = grid[endx][endy]

	grid[startx][starty].start = True
	start = grid[startx][starty]

	closedSet = []
	openSet = [start]
	cameFrom = {}

	while len(openSet) > 0:
		current = openSet[0]
		for x in openSet:
			if x.getF(start, end) < current.getF(start, end):
				current = x
		if current == end:
			return reconstructed_path(cameFrom, current)
		openSet.remove(current)
		closedSet.append(current)
		for neighbour in current.getNeighbours(grid):
			if neighbour in closedSet:
				continue
			tentative_g = current.getG(start) + neighbour.getG(start)
			if neighbour not in openSet:
				openSet.append(neighbour)
			elif tentative_g >= neighbour.getG(start):
				continue
			cameFrom[neighbour] = current
			neighbour.g = tentative_g
			neighbour.f = neighbour.g + neighbour.getF(start, end)

cols = 30
rows = 30
endx = 29
endy = 29
startx = 0
starty = 0
print(Astar(cols, rows, endx, endy, startx, starty))


#print(grid[2][3])

"""
What i want:
	3 rows with 6 collumns
	How do we do that?

	for x in range(rows):
		row = []
		for y in range(cols):
			row.append(node(x, y))
		grid.append(row)
	rows = range in y
	cols = range in x
"""