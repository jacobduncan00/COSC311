from check_grad import check_grad
from utils import *
from logistic import *

import matplotlib.pyplot as plt
import numpy as np

def run_logistic_regression():
    #train_inputs, train_targets = load_train()
    train_inputs, train_targets = load_train_small()
    valid_inputs, valid_targets = load_valid()
    N, M = train_inputs.shape

    #####################################################################
    # TODO:                                                             #
    # Set the hyperparameters for the learning rate, the number         #
    # of iterations, and the way in which you initialize the weights.   #
    #####################################################################
    hyperparameters = {
    "learning_rate": 0.008,
    "weight_regularization": 0.,
    "num_iterations": 2000
    }
    weights = np.random.randn(len(train_inputs[1])+1, 1) * 0.01
    #####################################################################
    #                       END OF YOUR CODE                            #
    #####################################################################

    # Verify that your logistic function produces the right gradient.
    # diff should be very close to 0.
    run_check_grad(hyperparameters)
    # Begin learning with gradient descent
    #####################################################################
    # TODO:                                                             #
    # Modify this section to perform gradient descent, create plots,    #
    # and compute test error.                                           #
    #####################################################################
    ce_trains = []
    ce_valids = []
    correct_trains = []
    correct_valids = []
    iterations = []
    for t in range(hyperparameters["num_iterations"]):
        f, df, y = logistic(weights, train_inputs, train_targets, hyperparameters)
        ce_train, frac_correct_train = evaluate(train_targets, y)
        ce_trains.append(ce_train)
        correct_trains.append(frac_correct_train)
        weights = weights - hyperparameters['learning_rate'] * df
        y_valid = logistic_predict(weights, valid_inputs)
        ce_valid, frac_correct_valid = evaluate(valid_targets, y_valid)
        ce_valids.append(ce_valid)
        correct_valids.append(frac_correct_valid)
        iterations.append(t)
    train_ce_avg = np.mean(ce_trains, axis=0)
    valid_ce_avg = np.mean(ce_valids, axis=0)
    train_crList_avg = np.mean(correct_trains, axis=0)
    valid_cr_avg = np.mean(correct_valids, axis=0)
    print("AVG_CE: Train %.5f Validation %.5f" %
            (train_ce_avg, valid_ce_avg))
    print("AVG_ERROR: Train {:.5f} Validation {:.5f}".format(
        1-train_crList_avg, 1-valid_cr_avg))
    plt.plot(iterations,ce_trains,label="Train Cross Entropy")
    plt.plot(iterations,ce_valids,label="Valid Cross Entropy")
    plt.xlabel("iterations")
    plt.ylabel("average cross entropy")
    plt.title("Average Cross Entropy")
    plt.legend()
    plt.show()


def run_pen_logistic_regression():
    train_inputs, train_targets = load_train()
    #train_inputs, train_targets = load_train_small()
    valid_inputs, valid_targets = load_valid()
    N, M = train_inputs.shape
    hyperparameters = {
    "learning_rate": 0.008,
    "weight_decay": 0.,
    "num_iterations": 2000
    }
    lambd_list = [0, 0.001, 0.01, 0.1, 1.0]
    run_check_grad(hyperparameters)
    run_time = 1
    for l in range(len(lambd_list)):
        hyperparameters["weight_decay"] = lambd_list[l]
        ce_trains = np.zeros(hyperparameters["num_iterations"])
        ce_valids = np.zeros(hyperparameters["num_iterations"])
        correct_trains = np.zeros(hyperparameters["num_iterations"])
        correct_valids = np.zeros(hyperparameters["num_iterations"])
        iterations = [i for i in range(1,hyperparameters["num_iterations"]+1)]
        for r in range(run_time):
            weights = np.random.randn(len(train_inputs[1]) + 1, 1) * 0.01
            for t in range(hyperparameters["num_iterations"]):
                f, df, y = logistic_pen(weights, train_inputs, train_targets, hyperparameters)
                ce_train, frac_correct_train = evaluate(train_targets, y)
                ce_trains[t] += (ce_train / run_time)
                correct_trains[t] += (frac_correct_train / run_time)
                weights = weights - hyperparameters["learning_rate"] * df
                y_valid = logistic_predict(weights, valid_inputs)
                ce_valid, frac_correct_valid = evaluate(valid_targets, y_valid)
                ce_valids[t] += (ce_valid / run_time)
                correct_valids[t] += (frac_correct_valid / run_time)
        train_ce_avg = np.mean(ce_trains, axis=0)
        valid_ce_avg = np.mean(ce_valids, axis=0)
        train_crList_avg = np.mean(correct_trains, axis=0)
        valid_cr_avg = np.mean(correct_valids, axis=0)
        print("AVG_CE: Train %.5f Validation %.5f" %
            (train_ce_avg, valid_ce_avg))
        print("AVG_ERROR: Train {:.5f} Validation {:.5f}".format(
        1-train_crList_avg, 1-valid_cr_avg))
        plt.plot(iterations,ce_trains,label="Train Cross Entropy")
        plt.plot(iterations,ce_valids,label="Valid Cross Entropy")
        plt.xlabel("iterations")
        plt.ylabel("average cross entropy")
        plt.title("Average Cross Entropy for lamda {}".format(lambd_list[l]))
        plt.legend()
        plt.show()

def run_check_grad(hyperparameters):
    """ Performs gradient check on logistic function.
    :return: None
    """
    # This creates small random data with 20 examples and
    # 10 dimensions and checks the gradient on that data.
    num_examples = 20
    num_dimensions = 10

    weights = np.random.randn(num_dimensions + 1, 1)
    data = np.random.randn(num_examples, num_dimensions)
    targets = np.random.rand(num_examples, 1)

    diff = check_grad(logistic,
                      weights,
                      0.001,
                      data,
                      targets,
                      hyperparameters)

    print("diff =", diff)


if __name__ == "__main__":
    run_logistic_regression()
    run_pen_logistic_regression()