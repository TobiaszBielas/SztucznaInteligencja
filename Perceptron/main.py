import sys
from random import uniform
import plot_generator as pg
from data_generator import data_generator, clear_files
from perceptron_func import teach_perceptron, testing_perceptron
import pickle

clear_files()
try:
    epochs = int(sys.argv[1])
except:
    epochs = 10
weights = [uniform(-1, 1), uniform(-1, 1), uniform(-1, 1)]
# weights = [5,3,1]
try:
    A = int(sys.argv[2])
    B = int(sys.argv[3])
    C = int(sys.argv[4])
    min_x = int(sys.argv[5])
    max_x = int(sys.argv[6])
    min_y = int(sys.argv[7])
    max_y = int(sys.argv[8])
    teach_list_amount = int(sys.argv[9])
    test_list_amount = int(sys.argv[10])
except:
    A = 5
    B = 3
    C = 1
    min_x = -200
    max_x = 200
    min_y = -200
    max_y = 200
    teach_list_amount = 80
    test_list_amount = 20

teach_list = []
test_list = []

new_data = input("Czy wylosować nowy zestaw danych? (tak/nie)")
if new_data == "nie":
    with open("teach_data", 'rb') as file:
        teach_list = pickle.load(file)
    with open("test_data", 'rb') as file:
        test_list = pickle.load(file)
else:
    teach_list = data_generator(teach_list_amount, A,B,C, min_x,max_x, min_y,max_y)
    with open("teach_data", 'wb') as file:
        pickle.dump(teach_list, file)
    test_list = data_generator(test_list_amount, A,B,C, min_x,max_x, min_y,max_y)
    with open("test_data", 'wb') as file:
        pickle.dump(test_list, file)
# print(teach_list)
# print("========================================")
# print(test_list)

teach_results = []
test_results = []
for epoch in range(epochs):
    teaching_factor = 0.001 * (epochs - epoch)
    result = teach_perceptron(teach_list, weights, teaching_factor)
    teach_results.append((epoch+1,result))
    with open("teach_result.txt", 'a') as file:
        file.write(f"{epoch+1}, {result}%\nweights: {weights}\n\n")
    result = testing_perceptron(test_list, weights)
    test_results.append((epoch+1,result))
    with open("testing_result.txt", 'a') as file:
        file.write(f"{epoch+1}, {result}%\n")

pg.teach_plot(teach_list)
pg.testing_plot(test_list)
pg.results_plot(test_results, teach_results)