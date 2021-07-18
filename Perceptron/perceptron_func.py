from random import uniform

def teach_perceptron(teach_list, weights, teaching_factor):
    teach_error = 0
    for x, y, target in teach_list:
        sum = weights[0] * x + weights[1] * y + weights[2]
        answer = 0
        if sum > 0:
            answer = 1
        if sum < 0:
            answer = 0

        if answer != target:
            teach_error += 1
            e = target - answer
            weight_correction(x, y, e, weights, teaching_factor)
            
    return (len(teach_list) - teach_error) * 100 / len(teach_list)


def testing_perceptron(test_list, weights):
    test_error = 0
    for x, y, target in test_list:
        sum = weights[0] * x + weights[1] * y + weights[2]
        answer = 0
        if sum > 0:
            answer = 1
        if sum < 0:
            answer = 0

        if answer != target:
            test_error += 1
    return (len(test_list) - test_error) * 100 / len(test_list)


def weight_correction(x, y, e, weights, teaching_factor):
    weights[0] += e * x * teaching_factor
    weights[1] += e * y * teaching_factor
    weights[2] += e * teaching_factor