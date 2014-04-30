import sys

class EdgeException(Exception):
	pass

class BadFormatException(Exception):
	pass

class Graph:

	def __init__(self, size, filename=None):
		self.filename = filename
		
		if (size != None):
			self.graph = [[None for x in range(size)] for y in range(size)]
		elif (filename != None):
			try:
				self.load_graph()
			except IOError:
				print "Error opening file, please check the filename you entered is valid."
				sys.exit()

			except IndexError:
				print "Tried to index node that doesn't exist, check graph file."
				sys.exit()

			except BadFormatException:
				print "Invalid format in graph file."
				sys.exit()
				
			except EdgeException:
				print "Number of edges does not match values defined in graph file."
				sys.exit()

	def load_graph(self):
		# Loads graph into an adjacency matrix from file.
		f = open(self.filename)

		edges = 0

		for line in f:
			line = line.strip('\n').split(' ')
			line = map(int, line)

			if len(line) == 2:
				self.nodes = line[0]
				edges = line[1]
				self.graph = [[None for x in range(self.nodes)] for y in range(self.nodes)]
			elif len(line) == 3:
				edges = edges - 1
				from_node, to_node, weight = line[0], line[1], line[2] 
				try:
					self.graph[from_node - 1][to_node - 1] = weight
				except IndexError:
					raise IndexError
			else:
				raise BadFormatException

		if (edges != 0):
			raise EdgeException

		f.close()

	def reverse(self):
		reversed = list()
		for i in range(0, len(self.graph)):
			reversed.append(list())
			for j in range(0, len(self.graph)):
				reversed[i].append(self.graph[j][i])
		
		self.graph = reversed

	def add_edge(self, fr, to, weight):
		self.graph[fr][to] = weight

	def get_size(self):
		return self.nodes

	def get_edge(self, fr, to):
		return self.graph[fr][to]

	def display(self):
		for node in self.graph:
			print node
		pass
