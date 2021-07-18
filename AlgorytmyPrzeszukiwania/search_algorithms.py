from calculation_algorithms import path_cost, get_children, distance, heuristic

def bfs(state, graph, goal):
    best_path = None
    state = [state]
    while state:
        current_state = state[0]
        state.remove(state[0])

        if len(current_state) == goal:
            current_state += current_state[0]
            cost = path_cost(current_state)

            if not best_path:
                best_path = (current_state, cost)
            
            if best_path[1] > cost:
                best_path = (current_state, cost)
            continue
        
        all_children = get_children(current_state, graph)
        state = state + all_children
    return best_path

def dfs(state, graph, goal):
    best_path = None
    state = [state]
    while state:
        current_state = state[0]
        state.remove(state[0])

        if len(current_state) == goal:
            current_state += current_state[0]
            cost = path_cost(current_state)

            if not best_path:
                best_path = (current_state, cost)
                
            if best_path[1] > cost:
                best_path = (current_state, cost)
            continue
            
        all_children = get_children(current_state, graph)
        state = all_children + state
    return best_path

def nearest_neighbour(state, graph, goal):
    best_path = None
    state = [state]
    open_list = []
    # print(state)
    for i in state:
        open_list += get_children(i, graph)
    state = []
    # print(open_list)
    for i in open_list:
        state += get_children(i, graph)
    # print(state)
    while state:
        state.sort(key = path_cost)
        current_state = state[0]
        state.clear()

        if len(current_state) == goal:
            current_state += current_state[0]
            cost = path_cost(current_state)
            best_path = (current_state, cost)
            
        state = get_children(current_state, graph)
    return best_path

def astar(state, graph, goal, heuristic):
    best_path = None
    state = [state]
    closed_list = []
    while state:
        state.sort(key=lambda state:(path_cost(state) + heuristic(state)))
        current_state = state[0]
        state.remove(state[0])
        closed_list.append(current_state)

        if len(current_state) == goal:
            current_state += current_state[0]
            cost = path_cost(current_state)

            if not best_path:
                best_path = (current_state, cost)
                
            if best_path[1] > cost:
                best_path = (current_state, cost)
            continue
        
        all_children = get_children(current_state, graph)
        for child in all_children:
            if child not in closed_list:
                state.append(child)
    return best_path