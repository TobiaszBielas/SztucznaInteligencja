from math import sqrt
from data import cities

def heuristic(path):
    try:
        x1, y1 = cities.get(path[-2])
        x2, y2 = cities.get(path[-1])
        return abs(x1 - x2) + abs(y1 - y2)
    except:
        return 0

def distance(first_city, second_city):
    x1, y1 = cities.get(first_city)
    x2, y2 = cities.get(second_city)
    return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

def path_cost(path):
    cost = 0
    current_path = []
    for point in path:
        print(point)
        
        current_path.append(point)
        print(current_path)
        
        if len(current_path) > 1:
            cost += distance(current_path[-2], current_path[-1])
        print(cost)
    return cost

def get_children(state, graph):
    if not state:
        return list(graph.keys())
    
    children = []
    for city_name in graph.keys():
        if city_name not in state:
            children.append(state + city_name)

    # print(children) # należy zakoentować jeżeli nie chcemy widoku kolejnych stanów
    return children