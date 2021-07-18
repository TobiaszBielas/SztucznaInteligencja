
from random import uniform

def data_generator(amount, A, B, C, min_x,max_x, min_y,max_y):
    points_list = []
    for i in range(amount):
        x = uniform(min_x, max_x)
        y = uniform(min_y, max_y)
        while A*x + B*y + C == 0:
            x = uniform(min_x, max_x)
            y = uniform(min_y, max_y)
        if A*x + B*y + C > 0:
            points_list.append((x, y, 1))
        if A*x + B*y + C < 0:
            points_list.append((x, y, 0))
    return points_list

def clear_files():
    with open("teach_result.txt", 'w') as file:
            file.write("")
    with open("testing_result.txt", 'w') as file:
            file.write("")
