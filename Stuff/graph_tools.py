import re

def parse(fileName):
	readFile = open(fileName, 'r')
	fileString = ""
	for line in readFile:
		fileString = fileString + str(line)
	fileString = re.sub('\s', '', fileString)
	elements = fileString.split(',')
	name = elements[0]
	if re.match("NAME=.+", name):
		name = name[5:]
	else:
		print ("Error: Name cannot be read")
	size = elements[1]
	if re.match("SIZE=\d+", size):
		size = int(size[5:])
	else:
		print ("Error: Size cannot be read")
	elements = elements[2:]
	for element in enumerate(elements):
		elements[element[0]] = int(re.sub('[^\d]', '', element[1]))
	graph = [[-1 for x in range(size)] for y in range(size)]
	i = 0
	for x in range(size):
		for y in range(x+1, size):
			graph[x][y] = elements[i]
			graph[y][x] =	graph[x][y]
			i = i +1
	return (name, size,	graph)

#Calculates the length of a given tour
def tour_length(tour, graph):
	tourLength = graph[tour[-1]-1][tour[0]-1] #Initialise with last -> first edge
	for i in range(len(tour)-1):
		tourLength = tourLength + graph[tour[i]-1][ tour[i+1]-1] #Sum rest of edges
	return tourLength

#Calculates the lower bound for a given graph
def lower_bound(inputGraph, graphSize):
	graph = [] #Copy the graph
	for subList in inputGraph:
		graph.append(subList[:])
	#Remove first node from graph completely
	for i in range(graphSize):
		graph[0][i] = -1
		graph[i][0] = -1
	#Generate minimum spanning tree of graph - node 1
	mst = []
	while len(mst) != graphSize-2:
		minLen = 99999999
		minNode = -1
		for i in range(1,graphSize):
			for j in range (i+1,graphSize):
				if (graph[i][j] < minLen) and (graph[i][j] != -1):
					minLen = graph[i][j]
					minNode = j
		mst.append(minLen)
		for i in range(graphSize):
			graph[i][minNode] = -1
	lowerBound = sum(mst)
	#Add first node by two edges
	lowest1 = 99999999
	lowest2 = 99999999
	for i in range(graphSize):
		edge = inputGraph[0][i]
		if (edge < lowest1) and (edge != -1):
			lowest2, lowest1 = lowest1, edge
		elif (edge < lowest2) and (edge != -1):
			lowest2 = edge
	lowerBound = lowerBound + lowest1 + lowest2
	return lowerBound     