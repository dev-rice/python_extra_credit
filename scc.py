from graph import Graph
import heapq
import sys

class SCC(Graph):
	def __init__(self, filename):
		self.graph = Graph(None, filename)
		self.components = list()

	def find_sccs(self):
		# 1. Call DFS(G) to find post[u]
		self.current_component = None
		self.dfs(range(0,self.graph.get_size()))
		
		# 2. computer transpose of G, G^T
		self.graph.reverse()
		
		# 3. Call DFS(G^T) with order of
		#	  decreasing post[u]
		self.current_component = 0
		order = self.reverse_sort()
		self.dfs(order)
		
		# 4. Output vertices of each tree in dfs
		#	  of G^T
		for index, component in enumerate(self.components):
			print str(index + 1) + ":", 
			for node in component:
				print node + 1, 
			print

		self.create_metagraph(self.components)
		self.metagraph.display()


	def reverse_sort(self):
		# Method for sorting the nodes u in U, in order of
		# decreasing post[u]
		order = list()
		heap = list()
		for i in range(0, self.graph.get_size()):
			# The negative 1 allows for a max heap
			heap.append((-1 * self.post[i], i))

		heapq.heapify(heap)
		for i in range(0, self.graph.get_size()):
			current = heapq.heappop(heap)
			order.append(current[1])

		return order

	def create_metagraph(self, components):
		# Terribly inefficient way to construct the metagraph
		# this looks for any edges connecting any two components
		# I couldn't think of a better way to accomplish this, but
		# the way I did it just seems wrong.
		self.metagraph = Graph(len(components))
		for index, component in enumerate(components):
			other_components = [x for x in components if x != component]
			for other_index, other_component in enumerate(other_components):
				for node in other_component:
					for i in range(0, self.graph.get_size()):
						if (self.graph.get_edge(index, other_index) != None):
							self.metagraph.add_edge(index, other_index, 1)

	def dfs(self, order):
		# Initialize visited, pre, and post to all
		# False, None, and None at the start of the search.
		self.visited = [False for i in range(0, self.graph.get_size())]
		self.pre = [None for i in range(0, self.graph.get_size())]
		self.post = [None for i in range(0, self.graph.get_size())]
		
		self.current_value = 1

		for i in order:
			if (not self.visited[i]):
				# Workaround to add components to list
				# using the same dsf method.
				if (self.current_component != None):
					self.components.append(list())
					self.components[self.current_component].append(i)
					self.explore(i)
					self.current_component = self.current_component + 1
				else:
					self.explore(i)

	def explore(self, node):
		# The explore method of dfs, as defined in 
		# the lecture slides. Includes the workaround
		# to find sccs.
		self.visited[node] = True
		self.previsit(node)

		for i in range(0, self.graph.get_size()):
			if (self.graph.get_edge(node, i) != None and not self.visited[i]):
				if (self.current_component != None):
					self.components[self.current_component].append(i)
				self.explore(i)

		self.postvisit(node)

	def previsit(self, i):
		self.pre[i]  = self.current_value
		self.current_value = self.current_value + 1

	def postvisit(self, i):
		self.post[i] = self.current_value
		self.current_value = self.current_value + 1

	def display_dfs(self):
		# Displays the dfs, for debugging purposes
		for i in range(0, self.graph.get_size()):
			print str(i+1) + ":", self.pre[i], self.post[i]

# Takes the first argument as the filename to load in
scc = SCC(sys.argv[1])
scc.find_sccs()
