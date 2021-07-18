import sys
from itertools import islice
from search_algorithms import bfs, dfs, nearest_neighbour, astar
from calculation_algorithms import heuristic, path_cost
from data import cities
from time import perf_counter_ns
import tracemalloc
from tracemalloc import get_tracemalloc_memory

number_of_cities = 5
graph = None
snapshots = 0
print(path_cost('ABCDE'))
for i in range(number_of_cities + 1):
    if i < 2:
        continue
    graph = dict(islice(cities.items(), i))

    time = perf_counter_ns()
    tracemalloc.start()
    path, cost = bfs('', graph, i)
    snapshots = get_tracemalloc_memory()
    time = perf_counter_ns() - time
    tracemalloc.stop()
    print("=======================================================================================================================")
    print(f"Breadth First Search:   Cities: {i} || Path: {path} || Cost: {cost} || Time: {time} || Memory: {snapshots}")

#     time = perf_counter_ns()
#     tracemalloc.start()
#     path, cost = dfs('', graph, i)
#     snapshots = get_tracemalloc_memory()
#     time = perf_counter_ns() - time
#     tracemalloc.stop()
#     print(f"Depth First Search:     Cities: {i} || Path: {path} || Cost: {cost} || Time: {time} || Memory: {snapshots}")
            
#     time = perf_counter_ns()
#     tracemalloc.start()
#     path, cost = nearest_neighbour('', graph, i)
#     snapshots = get_tracemalloc_memory()
#     time = perf_counter_ns() - time
#     tracemalloc.stop()
#     print(f"Nearest Neighbour:      Cities: {i} || Path: {path} || Cost: {cost} || Time: {time} || Memory: {snapshots}")

#     time = perf_counter_ns()
#     tracemalloc.start()
#     path, cost = astar('', graph, i, heuristic)
#     snapshots = get_tracemalloc_memory()
#     time = perf_counter_ns() - time
#     tracemalloc.stop()
#     print(f"Astar:                  Cities: {i} || Path: {path} || Cost: {cost} || Time: {time} || Memory: {snapshots}")
#     print("=======================================================================================================================")

