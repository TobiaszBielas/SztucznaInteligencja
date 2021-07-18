import matplotlib.pyplot as plt

def teach_plot(teach_list):
    for point in teach_list:
        x,y,z = point
        if z == 0:
            plt.plot(x,y,'bo')
        else:
            plt.plot(x,y,'m+')
    plt.title("teach Points")
    plt.show() 


def testing_plot(test_list):
    for point in test_list:
        x,y,z = point
        if z == 0:
            plt.plot(x,y,'bo')
        else:
            plt.plot(x,y,'m+')
    plt.title("testing Points")
    plt.show() 

def results_plot(test_results, teach_results):
    x = []
    y_test = []
    y_teach = []
    for result in test_results:
        x.append(result[0])
        y_test.append(result[1])
    for result in teach_results:
        y_teach.append(result[1])
    plt.plot(x, y_test, label="Testing results")
    plt.plot(x, y_teach, label="Teaching results")
    plt.legend()
    plt.title("Results")
    plt.ylabel("Percent")
    plt.xlabel("Epoch")
    plt.show()
