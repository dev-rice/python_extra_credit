from graph import Graph

class SCC(Graph):
	def __init__(self, filename):
		self.graph = Graph(filename)

	def find_sccs(self):
		# Reverse Graph
		self.graph.reverse()
		# Run DFS on reversed graph
		self.dfs()
		self.display_dfs()


	def dfs(self):

		self.visited = [False for i in range(0, self.graph.get_size())]
		self.previsit_nums = [None for i in range(0, self.graph.get_size())]
		self.postvisit_nums = [None for i in range(0, self.graph.get_size())]
		
		self.current_value = 1

		for i in range(0, self.graph.get_size()):
			if (not self.visited[i]):
				self.explore(i)


	def explore(self, node):
		self.visited[node] = True
		self.previsit(node)

		for i in range(0, self.graph.get_size()):
			if (self.graph.get_edge(node, i) != None and not self.visited[i]):
				self.explore(i)

		self.postvisit(node)

	def previsit(self, i):
		self.previsit_nums[i]  = self.current_value
		self.current_value = self.current_value + 1

	def postvisit(self, i):
		self.postvisit_nums[i] = self.current_value
		self.current_value = self.current_value + 1

	def display_dfs(self):
		for i in range(0, self.graph.get_size()):
			print str(i+1) + ":", self.previsit_nums[i], self.postvisit_nums[i]

scc = SCC("scc_test.txt")
scc.find_sccs()
