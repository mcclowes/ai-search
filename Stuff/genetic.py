from random import shuffle
from random import randint, randrange
from graph_tools import tour_length
from datetime import datetime
from nearest_neighbour import search_from_start

#Genetic algorithm main method
def genetic_search(graph, graphSize):
	#Step 1 : Create initial sorted population
	population = sorted(gen_population(graph, graphSize), key = lambda x: tour_length(x, graph))
	startTime = datetime.now() #Start timer

	while (((datetime.now() - startTime).total_seconds()) < (graphSize**2)): #Until timer reaches n seconds (n = graphSize)
		parent1 = []
		parent2 = []
		child1 = []
		child2 = []
		similarityCount = 0
		#Choose parents
		while (parent2 == []) or (parent1 == []) or (parent2 == parent1):
			parent1 = gen_parent(population, graphSize)
			parent2 = gen_parent(population, graphSize)
			if (parent2 == parent1):
				similarityCount = similarityCount + 1
			if (similarityCount > graphSize/2):
				shuffle(parent1)
				shuffle(parent2)
				similarityCount = 0
		#Crossover -> Create children
		(child1, child2) = gen_children(parent1, parent2, graphSize)
		#Mutate children
		mutateRoll1 = randint(1, 10)
		mutateRoll2 = randint(1, 10)
		if (mutateRoll1 <= 2):
			child1 = gen_mutation1(child1, graph)
		elif (mutateRoll1 > 2) and (mutateRoll1 <= 5):
			child1 = gen_mutation2(child1)
		if (mutateRoll2 <= 2):
			child2 = gen_mutation1(child2, graph)
		elif (mutateRoll2 > 2) and (mutateRoll2 <= 5):
			child2 = gen_mutation2(child2)
		#Check child is bigger than worst population and add
		population = population + [child1]
		population = population + [child2]
		population = sorted(population, key = lambda x: tour_length(x, graph))
		population = population[:graphSize]
	return best_tour(population, graph)

#Generate an initial tours population a given size
def gen_population(graph, graphSize):
	population =[]
	tour = list(range(1,graphSize+1))
	for i in range(graphSize):
		shuffle(tour)
		population.append(list(tour))
	population[0] = search_from_start(graph, graphSize, [1])
	return list(population)

#Selects a parent from population (weighted towards best)
def gen_parent(population, graphSize):
	parent = []
	roll = randint(1,10)
	if (roll >= 1) and (roll <= 4): #first quarter -> 4/10
		pRoll = randint(0, int(graphSize/4))
	elif (roll >= 5) and (roll <= 7): #second quarter -> 3/10
		pRoll = randint(int(graphSize/4), int(graphSize/4)*2)
	elif (roll >= 8) and (roll <= 9): #third quarter -> 2/10
		pRoll = randint(int(graphSize/4)*2, int(graphSize/4)*3)
	elif (roll == 10): #4th quarter - 1/10
		pRoll = randint(int(graphSize/4)*3,graphSize-1)
	else:
		print("error")
	parent = population[pRoll]
	return parent

#Generate 2 children from 2 parents using crossover
def gen_children(parent1, parent2, graphSize):
	#Pass first half of respective parent
	child1 = parent1[:randrange(1,graphSize-3)]
	child2 = parent2[:randrange(1,graphSize-3)]
	for node in parent2:
		if node not in child1:
			child1.append(node)
	for node in parent1:
		if node not in child2:
			child2.append(node)
	return (child1, child2)

#Mutates a child through tour improvement
def gen_mutation1(tour, graph):
	bestTour = list(tour)
	for i in range(len(bestTour)-1):
		tempTour= list(bestTour)
		tempTour[i], tempTour [i+1] = bestTour[i+1], bestTour[i]
		if (tour_length(tempTour, graph) < tour_length(bestTour, graph)):
			bestTour = list(tempTour)
	return bestTour

#Mutates a child by reversing a section of the list
def gen_mutation2(tour):
	start = randint(1,len(tour)-1)
	stop = randint(start,len(tour))
	tour[start:stop] = reversed(tour[start:stop]) #improve!
	return tour

#Finds the best tour of the population
def best_tour(population, graph):
	bestTourLength = 9999999999
	bestTour = 0
	for tour in population: #For each start node
		tourLength = tour_length(tour, graph)
		if tourLength < bestTourLength:
			bestTour, bestTourLength = tour, tourLength
	return (bestTour, bestTourLength)

