from graph import Graph
import sys
import Queue

class Dijkstra():
	def __init__(self, filename):
		self.graph = Graph(None, filename)

	def run(self, root_node):
		
		self.vertices = self.initialize_single_source(root_node - 1)
		S = set()
		Q = [self.vertices[i] for i in range(0, len(self.vertices))]
		Q.sort()

		while Q != []:
			u = Q[0]
			Q.remove(u)

			for i in range(0, self.graph.get_size()):
				weight = self.graph.get_edge(u[2], i)
				if weight != None:
					self.relax(u[2], i, weight)

			Q.sort()

		self.print_paths(root_node, self.vertices)

	def print_paths(self, root_node, vertices):
		for vertex in vertices:
			path = self.find_path(vertex, [vertex[2]])
			path.reverse()
			path = [x + 1 for x in path]

			print str(root_node) + " to " + str(vertex[2] + 1) + ", length " + str(vertex[0]) + ":",
			print self.str_path(path)

	def str_path(self, path):
		string = ""
		for vertex in path:
			string = string + str(vertex) + " -> "

		string = string[:len(string) - 4]

		return string		

	def find_path(self, vertex, path):
		#print vertex
		if vertex[1] != None:
			path.append(vertex[1])
			self.find_path(self.vertices[vertex[1]], path) 
		return path

	def initialize_single_source(self, root_node):
		# Vertex represented as a list [v.d, v.pi, v.num]
		vertices = [[float("inf"), None, i] for i in range(0, self.graph.get_size())]
		vertices[root_node] = [0, None, root_node]
		return vertices

	def relax(self, fr_index, to_index, weight):
		fr = self.vertices[fr_index]
		to = self.vertices[to_index]

		if to[0] > (fr[0] + weight):
			to[0] = fr[0] + weight
			to[1] = fr[2]


dijkstra = Dijkstra(sys.argv[1])
dijkstra.run(1)