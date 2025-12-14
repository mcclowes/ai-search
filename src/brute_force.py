from itertools import permutations
from graph_tools import tour_length
from datetime import datetime

#Brute force search method
def brute_force_search(graph, graphSize):
	bestTourLength = tour_length(range(1,graphSize+1), graph)
	bestTour = 0

	for tour in permutations(range(1,graphSize+1), graphSize): #Find the best tour
		tourLength = tour_length(tour, graph)
		if  tourLength <= bestTourLength:
			bestTour, bestTourLength = tour, tourLength

	return (bestTour, bestTourLength) #Return best tour length and the tour