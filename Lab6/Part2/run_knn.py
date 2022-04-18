from l2_distance import l2_distance
from utils import load_train, load_valid, load_test

import matplotlib.pyplot as plt
import numpy as np


def knn(k, train_data, train_labels, valid_data):
    """ Uses the supplied training inputs and labels to make
    predictions for validation data using the K-nearest neighbours
    algorithm.

    Note: N_TRAIN is the number of training examples,
          N_VALID is the number of validation examples,
          M is the number of features per example.

    :param k: The number of neighbours to use for classification
    of a validation example.
    :param train_data: N_TRAIN x M array of training data.
    :param train_labels: N_TRAIN x 1 vector of training labels
    corresponding to the examples in train_data (must be binary).
    :param valid_data: N_VALID x M array of data to
    predict classes for validation data.
    :return: N_VALID x 1 vector of predicted labels for
    the validation data.
    """
    dist = l2_distance(valid_data.T, train_data.T)
    nearest = np.argsort(dist, axis=1)[:, :k]

    train_labels = train_labels.reshape(-1)
    valid_labels = train_labels[nearest]

    # Note this only works for binary labels:
    valid_labels = (np.mean(valid_labels, axis=1) >= 0.5).astype(np.int32)
    valid_labels = valid_labels.reshape(-1, 1)

    return valid_labels


def run_knn():
    train_inputs, train_targets = load_train()
    valid_inputs, valid_targets = load_valid()
    test_inputs, test_targets = load_test()

    def start(ks, train_inputs, train_targets, pred_inputs, pred_targets):
        class_rates = []

        for k in ks:
            corrects = 0
            predict_labels = knn(k, train_inputs, train_targets, pred_inputs)
            for i in range(0, len(predict_labels)):
                if predict_labels[i]==pred_targets[i]:
                    corrects+=1
            class_rates.append(corrects/len(predict_labels))

        x_point = ks
        y_point = class_rates

        return x_point, y_point

    #####################################################################
    # TODO:                                                             #
    # Implement a function that runs kNN for different values of k,     #
    # plots the classification rate on the validation set, and etc.     #
    #####################################################################

    ks = [1, 3, 5, 7, 9]

    xpoints, ypoints = start(ks,train_inputs,train_targets,valid_inputs,valid_targets)

    plt.title("Classification Rate on Validation Set")
    plt.xlabel("Value of k")
    plt.ylabel("Classification Rate")
    plt.plot(xpoints, ypoints)
    for a,b in zip(xpoints, ypoints): 
        plt.text(a, b, str(b))
    plt.show()

    plt.savefig('q31a.png')

    plt.clf()


    xpoints, ypoints = start(ks, train_inputs, train_targets, test_inputs, test_targets)

    plt.title("Classification Rate on Test Set")
    plt.xlabel("Value of k")
    plt.ylabel("Classification Rate")
    plt.plot(xpoints, ypoints)
    for a,b in zip(xpoints, ypoints): 
        plt.text(a, b, str(b))
    plt.show()
   
    #####################################################################
    #                       END OF YOUR CODE                            #
    #####################################################################


if __name__ == "__main__":
    run_knn()





"""
Question (b)
Comment on the performance of the classifier and argue which value of k you would choose. What is the classification rate for k*, your chosen value of k? Also report the classification rate for k* + 2 and k* - 2. How does the test performance of these values of k correspond to the validation performance? 

The classifier performs pretty good on the validation set K = [1, 3, 5, 7, 9]. As you can see in the plot, 
the classifier predicts correctly about 82% of the data points. However, different K values do perform differently.
I think a good value to choose for K would be 5. The classification rate for k* is 0.86. 
The classification rate for K* + 2 is 0.86 and K* - 2 is 0.86. The test performance of the values of K are similar.
~5.7 or 5.8 would still be the best choice where as 3 seems to be a worse choise but better than 1 and 9. 
However, we can expect these because we know that K goes to 0, the model underfits the data and when k goes to infinity, 
the model overfits the data. Both won't result in the best rate, therefore a middle value of K is preferred.
"""
