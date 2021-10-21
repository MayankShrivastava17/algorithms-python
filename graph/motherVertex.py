from collections import defaultdict

class Graph:

	def __init__(self,vertices):
		self.V = vertices 
		self.graph = defaultdict(list) 

	def DFSUtil(self, v, visited):

		visited[v] = True

		for i in self.graph[v]:
			if visited[i] == False:
				self.DFSUtil(i, visited)

	def addEdge(self, v, w):
		self.graph[v].append(w)

	def findMother(self):

		visited =[False]*(self.V)

		v=0

		for i in range(self.V):
			if visited[i]==False:
				self.DFSUtil(i,visited)
				v = i

		visited = [False]*(self.V)
		self.DFSUtil(v, visited)
		if any(i == False for i in visited):
			return -1
		else:
			return v

g = Graph(7)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(4, 1)
g.addEdge(6, 4)
g.addEdge(5, 6)
g.addEdge(5, 2)
g.addEdge(6, 0)
print ("A mother vertex is " + str(g.findMother()))


