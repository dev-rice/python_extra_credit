from graph import Graph

class SCC(Graph):
	def dfs(self):
		self.visited = [False for i in range(0, self.nodes)]
		self.previsit_nums = [None for i in range(0, self.nodes)]
		self.postvisit_nums = [None for i in range(0, self.nodes)]
		
		self.current_value = 1

		for i in range(0, self.nodes):
			if (not self.visited[i]):
				self.explore(i)


	def explore(self, node):
		self.visited[node] = True
		self.previsit(node)

		for i in range(0, self.nodes):
			if (self.graph[node][i] != None and not self.visited[i]):
				self.explore(i)

		self.postvisit(node)

	def previsit(self, i):
		self.previsit_nums[i]  = self.current_value
		self.current_value = self.current_value + 1

	def postvisit(self, i):
		self.postvisit_nums[i] = self.current_value
		self.current_value = self.current_value + 1

	def display_dfs(self):
		for i in range(0, self.nodes):
			print str(i) + ":", self.previsit_nums[i], self.postvisit_nums[i]

scc = SCC("example_graph.txt")
scc.dfs()
scc.display_dfs()
