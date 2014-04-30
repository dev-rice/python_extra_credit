class Graph:
	def __init__(self, filename):
		self.filename = filename
		
		try:
			self.load_graph()
		except IOError:
			print "Error opening file, please check the filename you entered is valid."
		except IndexError:
			print "Tried to index node that doesn't exist, check graph file."
		pass

	def load_graph(self):
		f = open(self.filename)

		for line in f:
			line = line.strip('\n').split(' ')
			line = map(int, line)

			if len(line) == 2:
				self.nodes = line[0]
				self.graph = [[None for x in range(self.nodes)] for y in range(self.nodes)]
			else:
				from_node, to_node, weight = line[0], line[1], line[2] 
				
				try:
					self.graph[from_node - 1][to_node - 1] = weight
				except IndexError:
					raise IndexError

		f.close()

	def reverse(self):
		reversed = list()
		for i in range(0, len(self.graph)):
			reversed.append(list())
			for j in range(0, len(self.graph)):
				reversed[i].append(self.graph[j][i])
		
		self.graph = reversed

	def get_size(self):
		return self.nodes

	def display(self):
		for node in self.graph:
			print node
		pass
