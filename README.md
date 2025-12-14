# AI Search Algorithms for Traveling Salesman Problem

This project implements and compares various search algorithms for solving the Traveling Salesman Problem (TSP), including brute force, modified brute force, nearest neighbor, and genetic algorithms.

## Project Overview

The Traveling Salesman Problem is a classic optimization problem where the goal is to find the shortest possible route that visits each city exactly once and returns to the starting city. This project implements four different approaches to solve this NP-hard problem:

1. **Brute Force Search** - Exhaustive search through all possible permutations
2. **Modified Brute Force Search** - Time-limited random search with early termination
3. **Nearest Neighbor Search** - Greedy heuristic with tour improvement
4. **Genetic Algorithm** - Evolutionary approach with crossover and mutation

## File Structure

```
ai-search/
├── src/                        # Source code
│   ├── __init__.py            # Package initialization
│   ├── brute_force.py         # Brute force implementation
│   ├── modified_brute_force.py# Modified brute force with time limits
│   ├── nearest_neighbour.py   # Nearest neighbor heuristic
│   ├── genetic.py             # Genetic algorithm implementation
│   ├── graph_tools.py         # Utility functions for graph operations
│   └── main.py                # Main program interface
├── data/                       # Test data files
│   └── AISearchfile*.txt      # Test case files (8-535 cities)
├── docs/                       # Documentation
│   ├── AISearchAssignment.pdf # Assignment specification
│   └── DENLN_Heuristic.pdf    # Research paper on heuristics
└── Submit/                     # Academic submission results
    ├── cityfiles/             # Input city files
    ├── pvxf29/                # Student submission
    │   ├── TourfileA/         # Algorithm A results
    │   ├── TourfileB/         # Algorithm B results
    │   └── TourfileC/         # Algorithm C results
    └── validtourcheck.py      # Tour validation script
```

## Algorithms Implemented

### 1. Brute Force Search (`brute_force.py`)
- **Approach**: Generates all possible permutations of city visits
- **Time Complexity**: O(n!)
- **Space Complexity**: O(n!)
- **Best for**: Small graphs (n ≤ 10)
- **Limitations**: Exponential growth makes it impractical for larger instances

### 2. Modified Brute Force Search (`modified_brute_force.py`)
- **Approach**: Time-limited random permutation testing
- **Time Limit**: n seconds (where n = graph size)
- **Optimization**: Early termination when lower bound is reached
- **Best for**: Medium-sized graphs with time constraints

### 3. Nearest Neighbor Search (`nearest_neighbour.py`)
- **Approach**: Greedy heuristic starting from each city
- **Time Complexity**: O(n²)
- **Features**: 
  - Tests all possible starting cities
  - Includes tour improvement via 2-opt swaps
  - Early termination when optimal solution found
- **Best for**: Quick solutions for medium to large graphs

### 4. Genetic Algorithm (`genetic.py`)
- **Approach**: Evolutionary computation with population-based search
- **Time Limit**: n² seconds (where n = graph size)
- **Features**:
  - Population size = graph size
  - Weighted parent selection (biased toward better solutions)
  - Two-point crossover
  - Two mutation strategies (2-opt improvement and segment reversal)
  - Population replacement with elitism
- **Best for**: Large graphs where near-optimal solutions are acceptable

## Input Format

The program expects input files in the following format:
```
NAME = [filename],
SIZE = [number_of_cities],
[distance_matrix_upper_triangle]
```

Example:
```
NAME = AISearchtestcase,
SIZE = 8,
2,6,8,9,8,6,3,
4,8,10,
10,7,5,
5,6,8,8,9,
4,6,7,8,
3,5,9,
3,6,
4
```

## Usage

### Running the Main Program
```bash
python src/main.py
```

The program provides an interactive interface with the following commands:
- `help` - Display available commands and list available data files
- `brute` - Run brute force search
- `modified` - Run modified brute force search
- `nearest` - Run nearest neighbor search
- `genetic` - Run genetic algorithm

### Example Usage
1. Start the program: `python src/main.py`
2. Choose an algorithm: `genetic`
3. Select a graph file: `AISearchfile012.txt`
4. The program will generate a tour file with results

## Output Format

The program generates tour files with the following format:
```
NAME = [filename],
TOURSIZE = [number_of_cities],
LENGTH = [tour_length],
[tour_sequence]
```

## Key Features

### Graph Tools (`graph_tools.py`)
- **`parse(fileName)`**: Parses input files and constructs adjacency matrix
- **`tour_length(tour, graph)`**: Calculates total distance of a tour
- **`lower_bound(graph, graphSize)`**: Computes theoretical minimum tour length using MST

### Tour Improvement
- **2-opt swaps**: Local optimization to improve tour quality
- **Segment reversal**: Alternative mutation strategy in genetic algorithm

### Performance Optimizations
- **Early termination**: Stop when optimal solution is found
- **Lower bound checking**: Theoretical minimum for validation
- **Time limits**: Prevent infinite execution on large instances

## Algorithm Comparison

| Algorithm | Time Complexity | Space Complexity | Solution Quality | Best Use Case |
|-----------|----------------|------------------|------------------|---------------|
| Brute Force | O(n!) | O(n!) | Optimal | Small graphs (n ≤ 10) |
| Modified Brute Force | O(n) | O(n) | Good | Medium graphs with time limits |
| Nearest Neighbor | O(n²) | O(n) | Good | Quick solutions |
| Genetic Algorithm | O(n²) | O(n) | Very Good | Large graphs |

## Dependencies

- Python 3.x
- Standard library modules:
  - `itertools` (for permutations)
  - `random` (for genetic algorithm)
  - `datetime` (for timing)
  - `re` (for file parsing)

## Testing

The project includes multiple test cases with varying graph sizes:
- Small graphs (8-12 cities): Suitable for brute force
- Medium graphs (17-26 cities): Good for heuristic algorithms
- Large graphs (42-535 cities): Requires efficient algorithms

## Results

The project generates three sets of results (TourfileA, TourfileB, TourfileC) representing different algorithm implementations or parameter configurations, allowing for comprehensive comparison of solution quality and performance.

## Validation

Use the included `validtourcheck.py` script to validate that generated tours:
- Visit each city exactly once
- Return to the starting city
- Calculate correct tour length

## Academic Context

This project appears to be part of an AI/Computer Science course assignment focusing on search algorithms and optimization techniques for NP-hard problems. The implementation demonstrates understanding of:

- Algorithm design and analysis
- Heuristic search methods
- Evolutionary computation
- Problem complexity analysis
- Performance optimization techniques
